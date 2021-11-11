import requests
 
url = "http://webauth.education.tas.gov.au"
 
headers = {"Content-Type": "application/json; charset=utf-8", "password": "Password", "username": "UserName"}

response = requests.post(url, headers=headers)
 
print("Status Code", response.status_code)

