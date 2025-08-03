import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def validate_url(self, url):
        """Check if the URL is valid and has a scheme (http/https)"""
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    
    def scrape(self, url, element_type, element_value):
        """
        Scrape data from the given URL based on element type and value
        
        Args:
            url (str): URL to scrape
            element_type (str): 'class', 'id', or 'tag'
            element_value (str): Value of the element to find
            
        Returns:
            list: List of dictionaries containing scraped data
        """
        if not self.validate_url(url):
            raise ValueError("Invalid URL. Please include http:// or https://")
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch URL: {e}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        try:
            if element_type == 'class':
                items = soup.find_all(class_=element_value)
            elif element_type == 'id':
                items = soup.find_all(id=element_value)
            elif element_type == 'tag':
                items = soup.find_all(element_value)
            else:
                raise ValueError("Invalid element type. Use 'class', 'id', or 'tag'")
            
            for item in items:
                result = {
                    'text': item.get_text(strip=True),
                    'element_type': element_type,
                    'element_value': element_value,
                    'tag_name': item.name
                }
                
                # Add attributes if present
                if item.attrs:
                    for attr, value in item.attrs.items():
                        result[f'attr_{attr}'] = value
                
                results.append(result)
            
            return results
            
        except Exception as e:
            raise Exception(f"Scraping error: {e}")
    
    def save_to_csv(self, data, filename='output.csv'):
        """Save scraped data to CSV file"""
        if not data:
            raise ValueError("No data to save")
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        return filename
    
    def save_to_excel(self, data, filename='output.xlsx'):
        """Save scraped data to Excel file"""
        if not data:
            raise ValueError("No data to save")
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        return filename