import requests
import base64
from plyer import notification

#put your username and password
username ="PUT USERNAME"
password = "PUT PASSWORD"

#NERD SHIT

#Base64 encoder (username)
username_Byte = base64.b64encode(username.encode("utf-8"))
username64 = str(username_Byte, "utf-8")
#(password)
password_Byte = base64.b64encode(password.encode("utf-8"))
password64 = str(password_Byte, "utf-8")

url = "http://webauth.education.tas.gov.au"
 
headers = {"Content-Type": "application/json; charset=utf-8", "password": password64, "username": username64}

response = requests.post(url, headers=headers)

if response.status_code == 403:
    notification.notify(
    title = 'DoE AutoLogin',
    message = 'Logged In!',
    timeout = 2,
)
else:
    notification.notify(
    title = 'DoE AutoLogin',
    message = 'Not Logged In :/',
    timeout = 2,
)
