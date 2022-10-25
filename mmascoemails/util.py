import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    print("begin function")
    # password = "umeellggmztagttd"
    # user_email = "sanelemngadi17@gmail.com"   
    # password = "EQ=#b64wSj"
    # user_email = "private.socialworker@xolanibukhosini.co.za"   
    password = "Sisanda$360"
    user_email = "hello@sanelemngadi.com"   
    # password = "xolanibukhosini"

    smtp = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
    # smtp = smtplib.SMTP_SSL("smtp.office365.com", 465)
    # smtp = smtplib.SMTP("pop.secureserver.net", 995)
    # smtp = smtplib.SMTP("smtpout.secureserver.net", 465)
    print("server")
    # smtp = smtplib.SMTP("smtp.gmail.com", 587)
    # smtp = smtplib.SMTP_SSL("smtp.office365.com", 587)
    # smtp.ehlo()  
    # smtp.starttls()  
    # smtp.ehlo()  
    log =smtp.login(user_email, password)  
    print(f"log: {log}")  

    msg = EmailMessage()
    msg["Subject"] = "Just a subject"
    msg["From"] = "hello@sanelemngadi.com"
    msg["To"] = ["sanelemngadi17@gmail.com", "218014972@stu.ukzn.ac.za"]
    msg.set_content("this is the message I sent")

    print(f"smtp: {str(msg)}")  
    # msg= f"Just a subject\n\nthis is the message I sent"

    # smtp.sendmail(user_email,["sanelemngadi17@gmail.com"], msg)
    # smtp.sendmail

    sm = smtp.send_message(msg)
    print(f"msg status: {str(sm)}")  

send_email()
# password = "Sisanda$360"
# user_email = "hello@sanelemngadi.com" 
# password = "EQ=#b64wSj"
# user_email = "private.socialworker@xolanibukhosini.co.za" 

# msg = MIMEMultipart()
# msg.set_unixfrom('author')

# msg["Subject"] = "Simple message subject"
# msg["From"] = "hello@sanelemngadi.com"
# # msg["From"] = "private.socialworker@xolanibukhosini.co.za"
# msg["To"] = "sanelemngadi17@gmail.com"
# message = "This is the actual body of an email"
# msg.attach(MIMEText(message))

# mailserver = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
# mailserver.ehlo()
# mailserver.login(user_email, password) 
# mailserver.sendmail(user_email,user_email,msg.as_string())
# mailserver.quit()

