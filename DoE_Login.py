import requests
from plyer import notification

 
url = "http://webauth.education.tas.gov.au"
 
headers = {"Content-Type": "application/json; charset=utf-8", "password": "REPLACE_WITH_PASSWORD", "username": "REPLACE_WITH_USERNAME"}

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
