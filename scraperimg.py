from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

# Configure Selenium web driver options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Provide the path to the ChromeDriver executable
chromedriver_path = '/Users/xx/chromedriver'

# Create a new ChromeDriver service
service = Service(executable_path=chromedriver_path)

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set the search queries and output directories
search_queries = ['nasi_lemak', 'nasi_kerabu']
output_directories = [
    '/Users/dimuthupahindra/Python_Projects/google-images-download/images/nasi_lemak_V',
    '/Users/dimuthupahindra/Python_Projects/google-images-download/images/nasi_kerabu_V'
]

# Create the output directories if they don't exist
for output_directory in output_directories:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

# Iterate over the search queries and download images for each category
for query, output_directory in zip(search_queries, output_directories):
    # Format the Google Images URL with the search query
    google_images_url = f'https://www.google.com/search?q={query}&tbm=isch'

    # Load the Google Images webpage
    driver.get(google_images_url)

    # Scroll down the page to load more images
    scroll_pause_time = 2
    scroll_height = 0

    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        # Calculate the new scroll height and check if it has reached the bottom
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")

        if new_scroll_height == scroll_height:
            break

        scroll_height = new_scroll_height

    # Find all the image elements on the page
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')

    # Download the images
    for i, image_element in enumerate(image_elements):
        # Get the image source URL
        image_url = image_element.get_attribute('src')

        try:
            # Download the image and save it to the output directory
            urllib.request.urlretrieve(image_url, f'{output_directory}/{query}_{i+1}.jpg')
            print(f'Downloaded image {i+1}/{len(image_elements)} for {query}')
        except Exception as e:
            print(f'Error downloading image {i+1} for {query}: {str(e)}')

# Close the browser
driver.quit()
