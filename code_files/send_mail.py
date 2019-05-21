import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# starts connection mailserver
def startServer(login):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    try:
        server.login(login[0], login[1])
        print("login successful")

    except Exception as error:
        print("login Error")

    return server

# closes connection to mailserver
def closeServer(server):
    server.quit()
    print("logging out")

# sends an mail with the details imported
def sendMail(template, subject, sender, receiver, server):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Attaches template to mail
    content = MIMEText(template, 'html')
    msg.attach(content)
    # sends the mail
    server.send_message(msg)
    print("Subject: " + subject + " sent to " + receiver)
    del msg
