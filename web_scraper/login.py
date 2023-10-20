```python
import requests
from bs4 import BeautifulSoup

class UserCredentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login(user_credentials):
    login_url = "https://safepins.eu/login"
    session = requests.Session()

    login_payload = {
        "username": user_credentials.username,
        "password": user_credentials.password
    }

    response = session.post(login_url, data=login_payload)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find(id="loginButton") is None:
            print("LoginSuccess")
            return session
        else:
            print("LoginFailed")
            return None
    else:
        print("LoginFailed")
        return None
```