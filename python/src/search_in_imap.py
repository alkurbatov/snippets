import imaplib

imap = imaplib.IMAP4_SSL("0.0.0.0", 2001)
imap.login("user@mail.ru", "secret")

imap.select("INBOX")
typ, msgnums = imap.search(None, '(SUBJECT "test")')

print(typ, msgnums)
