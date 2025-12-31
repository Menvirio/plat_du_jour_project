# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 17:48:24 2025

@author: mnnvt
"""

# main.py
from scraper import MenuScraper

# Define the list of restaurant menu pages to scrape
RESTAURANT_URLS = [
        "https://www.restaurant1.it/menu/", 
        "https://www.restaurant2.it/menu/",
        "https://www.restaurant3.it/menu/",
        "https://www.restaurant4.it/menu/",
        "..."
]

def main():
    print("--- Starting Restaurant Menu Scraper ---")
    
    # Initialize the scraper with the URLs
    bot = MenuScraper(RESTAURANT_URLS)
    
    # Run the scrape
    bot.scrape_all()
    
    # Generate the formatted DataFrame
    final_df = bot.get_processed_df()
    
    if final_df is not None:
        bot.save_to_downloads(final_df)
        print("--- Process Completed Successfully ---")
    else:
        print("--- Error: No data was collected. ---")

if __name__ == "__main__":
    main()
