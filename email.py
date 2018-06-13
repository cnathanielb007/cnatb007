#this is for gmail
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your email", "your password")

msg = "Python msg"
server.sendmail("your email", "sender email", msg)
server.quit()


