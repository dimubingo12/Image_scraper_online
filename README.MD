# Image Scraper Online

## Overview
Image Scraper Online is a simple Python application that uses Selenium WebDriver for scraping images from Google Images. This tool can be used to download a batch of images related to specific search queries, which are stored in designated output directories.

## Requirements
- Python 3.6 or higher.
- Selenium WebDriver
- ChromeDriver

Please ensure that you have installed the correct versions of Selenium WebDriver and ChromeDriver compatible with your system.

## Usage
1. Clone this repository to your local machine.


2. Install the required Python dependencies.


3. Edit the `search_queries` and `output_directories` variables in `scraperimg.py` to contain your desired search queries and corresponding output directories.

4. Run the `scraperimg.py` script.




## How it works
The script loads the Google Images webpage for each search query, scrolls to the bottom of the page to load all images, and then downloads each image to the corresponding output directory. The images are saved with the format `{query}_{i+1}.jpg`.

## Note
Please be respectful and mindful of the terms of service of any website that you are scraping. Additionally, while this script is helpful for educational purposes and small personal projects, it might not be suitable for large scale data gathering, and you should consider using official APIs or data providers for such tasks.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
