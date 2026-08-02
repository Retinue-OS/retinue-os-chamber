# c391 — issue body, retinue: attachments stored without an extension

Filed 2026-08-02 against `retinue-os/retinue`. Text below is verbatim as filed.

---

**Title:** Thread attachments are stored without a file extension, so a session reads a PDF as mojibake

**Body:**

`_store_attachments()` writes each file as `CONVERSATION_ATTACHMENTS_DIR/<cid>/<att_id>`, where `att_id` is a bare `uuid4().hex` — deliberately, so an untrusted filename never becomes a path component. The original name survives only as metadata, used for the download's `Content-Disposition`. `_conv_attachment_note()` then hands Ara that same extensionless path so she can open the file.

That works for images and silently fails for PDFs. Measured in a container with the same `Read` tool a conversation session gets:

| file | what `Read` returned |
|---|---|
| PNG, no extension | rendered as an image |
| PDF, uncompressed content stream, no extension | the PDF source as text |
| PDF, `/FlateDecode` content stream, no extension | `x?s\nQ?w3T04RIS02P05PIQ?p??-(J-.NMQ` … as text |
| the same PDF bytes, named `doc.pdf` | rendered as a document |

Images are content-sniffed; PDFs are keyed on the extension. Real-world PDFs compress their content streams, so the third row is the ordinary case: the agent gets mojibake, and neither layer emits an error saying so. It looks like the file was read.

This matters for the case `CLAUDE.md` names explicitly — "an e-mail attachment (a PDF invoice) forwarded into a thread, so it's reachable without an e-mail client". #64 removes the permission prompt on that path; this is what is left behind it. A prompt is at least visible.

**Suggested fix**, keeping the property that motivated the opaque id: derive a suffix from the stored `content_type` through a small allowlist (`application/pdf` → `.pdf`, the image types, `text/csv`, …) and append it to the generated id, so the stored name is `<att_id>.pdf`. The extension then comes from an allowlist rather than from the user's string, so no traversal or extension-confusion is reintroduced, and `_serve_conversation_attachment()`'s existing `realpath` containment check is unaffected. Files whose type is not on the allowlist keep today's behaviour.

Found while reviewing #64; kept separate so it does not hold that one up.

*Filed by Aros — the project's AI agent account, operated under human oversight.*
