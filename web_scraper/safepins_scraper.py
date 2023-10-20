```python
import requests
from bs4 import BeautifulSoup
from login import login, UserCredentials

class ScrapedData:
    def __init__(self, data):
        self.data = data

def scrape_data(session, url):
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}  # Replace this with the actual data extraction logic
        return ScrapedData(data)
    else:
        print("ScrapeFailed")
        return None

def main():
    url = "https://safepins.eu"  # Replace this with the actual URL
    credentials = UserCredentials("username", "password")  # Replace these with the actual credentials
    session = requests.Session()
    if login(session, url, credentials):
        print("LoginSuccess")
        scraped_data = scrape_data(session, url)
        if scraped_data:
            print("ScrapeSuccess")
            return scraped_data
        else:
            print("ScrapeFailed")
    else:
        print("LoginFailed")

if __name__ == "__main__":
    main()
```