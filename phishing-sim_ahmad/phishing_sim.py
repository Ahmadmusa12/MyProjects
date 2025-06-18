import smtplib
from email.message import EmailMessage

# Credentials
email_address = email_address = 'your_icloud_email@icloud.com'
app_password = app_password = 'YOUR_APP_SPECIFIC_PASSWORD_HERE'

# Create email
msg = EmailMessage()
msg['Subject'] = 'iCloud SMTP Test'
msg['From'] = email_address
msg['To'] = 'ahmadmusa1066@gmail.com'  # or any email you want to receive it
msg.set_content('This is a test email sent using iCloud SMTP.')

# Send email using iCloud's SMTP server
try:
    with smtplib.SMTP('smtp.mail.me.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_address, app_password)
        smtp.send_message(msg)
        print("✅ Email sent successfully.")
except Exception as e:
    print("❌ Failed to send email.")
    print(e)
