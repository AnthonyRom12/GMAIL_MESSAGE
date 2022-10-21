import smtplib

sender_email = 'PUT HERE EMAIL, FROM WHERE YOU WILL SEND MESSAGES'
re_email = 'EMAIL ADDRESS TO RECEIVE MESSAGES'
password = 'GENERATED PASSWORD FROM GOOGLE'

# create SMTP session
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
smtpObj.starttls()

# Authentication
smtpObj.login(sender_email, password)
print("Login success")

# message to send
message = 'This is an automated message. Do not reply'

# Sending the mail
smtpObj.sendmail(sender_email, re_email, message)
print("Email has been sent to", re_email)
# Termination of the session
# smtpObj.quit()

