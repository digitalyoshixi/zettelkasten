---
tags:
  - programming
---
Do after you [[Gmail API Generate Token.json]]
```python
SCOPES = ["https://mail.google.com/"]
# send an email with OTP
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        creds.refresh(Request())
        print("Token refreshed successfully!")
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()
        
        message.set_content(f"Hey heres an email")
        message["To"] = recieve_email
        message["From"] = "uoftmichealbot@gmail.com"
        message["Subject"] = "Subject here"
        
        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        create_message = {"raw": encoded_message}
        print("sending emails..")
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
```