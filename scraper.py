from bing_scraper import BingScraper

# Specify the URL, limit, and ChromeDriver path
url = 'https://www.bing.com/images/search?q=mao+shan+wang'
limit = 100
chromedriver_path = '/Users/dimuthupahindra/Downloads/chromedriver_mac64'

# Instantiate the BingScraper and run the scrape method
scraper = BingScraper(url, limit, chromedriver_path)
scraper.scrape()

