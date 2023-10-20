```python
import json
from data_extraction import ScrapedData

def store_data(scraped_data: ScrapedData, filename: str = 'scraped_data.json'):
    try:
        with open(filename, 'w') as json_file:
            json.dump(scraped_data.__dict__, json_file)
        print("ScrapeSuccess: Data stored successfully in JSON format.")
    except Exception as e:
        print(f"ScrapeFailed: {str(e)}")

if __name__ == "__main__":
    # This is just for testing purposes
    # In production, this function will be called from data_extraction.py
    scraped_data = ScrapedData()
    store_data(scraped_data)
```