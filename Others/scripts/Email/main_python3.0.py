import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Blessing Afolabi'
email['to'] = 'enochonlinenow@gmail.com'
# this is the title of our email
email['subject'] = 'You won 1,000,000 dollars!'

# this can have an image,html or plain text
# this is the body of our email
email.set_content(html.substitute({'name' : 'Blessing'}), html)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # this say hello to the server and i am connecting
    smtp.ehlo()
    # this is for security
    smtp.starttls()
    # this is for login
    smtp.login('lovguya@gmail.com', 'your password')
    # this is for sending
    smtp.send_message(email)
    print('All done')