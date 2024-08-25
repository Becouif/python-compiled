import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Blessing Afolabi'
email['to'] = 'lovguya@gmail.com'
# this is the title of our email
email['subject'] = 'You won 1,000,000 dollars!'

# this can have an image,html or plain text
# this is the body of our email
email.set_content('i am a programmer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # this say hello to the server and i am connecting
    smtp.ehlo()
    # this is for security
    smtp.starttls()
    # this is for login
    smtp.login('your email', 'your password')
    # this is for sending
    smtp.send_message(email)
    print('All done')