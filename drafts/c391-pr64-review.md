# c391 — review comment on retinue#64

Posted 2026-08-02 on `retinue-os/retinue` PR #64 ("Grant conversation sessions
read access to thread attachments"). Text below is verbatim as posted.

---

Reviewed against the branch head, with both findings measured in a running container rather than read off the diff.

**The fix is right, and it should go in.** `CONVERSATION_ATTACHMENTS_DIR` is created at import time (`web-gateway.py`, next to its definition), so the second `--add-dir` can never point at a path that does not exist yet, and it is the only tree stored attachments ever land in.

**One correction to the Cause section, for the sake of the git history.** `/root/.claude/uploads` is not where composer uploads land. On this branch that path appears in exactly three places, none of them an upload handler:

- `.claude/settings.json` → `permissions.additionalDirectories`
- `scripts/entrypoint.sh` → `--add-dir` on the `--remote-control` session
- `scripts/web-gateway.py` → the line this PR extends

It is the Claude *app*'s upload directory for the remote-control session. Dashboard composer uploads take the same route as agent-pushed ones: `POST /conversations/<id>/messages` → `_conv_add_message(..., attachments=…)` → `_store_attachments()` → `CONVERSATION_ATTACHMENTS_DIR/<cid>/<att_id>`. Same tree, same grant — so before this PR a composer upload was as unreadable as a pushed one, and after it both are readable. The patch's behaviour is unaffected; only the reason recorded for it is. If a composer upload really did open without a prompt while a pushed one did not, the cause is somewhere other than `--add-dir`, and worth knowing, because whatever explains it will explain the next surprise too.

**The grant is necessary and not sufficient, and the remaining gap is silent.** `_store_attachments()` writes each file as a bare `uuid4().hex` with no extension, and `_conv_attachment_note()` hands the session exactly that path. Measured just now with the same `Read` tool a session gets:

| file | what `Read` returned |
|---|---|
| PNG, no extension | rendered as an image |
| PDF, uncompressed content stream, no extension | the PDF source as text |
| PDF, `/FlateDecode` content stream, no extension | `x?s\nQ?w3T04RIS02P05PIQ?p??-(J-.NMQ` … as text |
| the same PDF bytes, named `doc.pdf` | rendered as a document |

Images are content-sniffed; PDFs are keyed on the extension. So for the case `CLAUDE.md` names — a PDF invoice forwarded into a thread — this PR removes the permission prompt and the session then reads mojibake, with no error at either layer to say so. The prompt was at least visible.

Filed separately as #65, with a fix that keeps the untrusted filename out of the path, so it does not hold this one up.

*Aros — the project's AI agent account, operated under human oversight. Not a human.*
