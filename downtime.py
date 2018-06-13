#this is for gmail
#it check if the server is live or no if not it sence an autimated email
import smtplib
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

starttime=time.time()
while True:
    req = Request("hydragons.com")
    try:
        response = urlopen(req)
    except HTTPError as e:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your email, "your email password")
        msg = 'The server couldn\'t fulfill the request'
        msg_2=('Error code: ', e.code)
        fin=msg+msg_2

        server.sendmail("your email", "reciver email", fin)
        server.quit()

    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print ('Website is working fine')
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

