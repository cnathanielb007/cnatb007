#this is for gmail
import smtplib
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('hydragons.com', 80))#instead of hydragons put your website name
if result == 0:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("your email", "your password")

  msg = "Server is down"
  server.sendmail("your email", "sender email", msg)
  server.quit()
  


