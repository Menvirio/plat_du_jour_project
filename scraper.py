# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 17:55:13 2025

@author: mnnvt
"""

# scraper.py
import os
import requests
import pandas as pd
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime, timedelta
from pathlib import Path

# Silence SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class MenuScraper:
    """A class to scrape and aggregate restaurant menus."""
    
    def __init__(self, urls):
        self.urls = urls
        self.all_data = []
        # Calculate the Monday of the current week
        self.monday_str = (datetime.today() - timedelta(days=datetime.today().weekday())).strftime("%Y%m%d")

    def scrape_all(self):
        """Iterates through URLs and extracts menu items based on a specific HTML schema."""
        for url in self.urls:
            try:
                print(f"Fetching: {url}")
                response = requests.get(url, verify=False, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, "html.parser")
                # Targeted selector for the dish container
                dishes = soup.find_all("div", class_="dish-title-wrap")
                
                domain = urlparse(url).netloc.split(".")[1]
                
                for dish in dishes:
                    day_tag = dish.find("h4", class_="dish__title")
                    desc_tag = dish.find("p", class_="dish__descr")
                    
                    day = day_tag.text.strip() if day_tag else "Unknown"
                    desc = desc_tag.text.strip() if desc_tag else "No description"
                    
                    self.all_data.append({
                        "Restaurant": domain,
                        "Day": day.capitalize(),
                        "Dish": desc
                    })
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

    def get_processed_df(self):
        """Converts raw list to a clean, pivoted DataFrame."""
        if not self.all_data:
            return None
        
        df = pd.DataFrame(self.all_data)
        weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        # Group dishes (handling multiple items per day) and Pivot
        df_grouped = df.groupby(["Day", "Restaurant"], as_index=False).agg({"Dish": lambda x: "\n".join(x)})
        df_pivot = df_grouped.pivot(index="Day", columns="Restaurant", values="Dish").reset_index()
        
        # Enforce chronological work week order
        df_pivot["Day"] = pd.Categorical(df_pivot["Day"], categories=weekday_order, ordered=True)
        return df_pivot.sort_values("Day").reset_index(drop=True)

    def save_to_downloads(self, df):
        """Saves the resulting dataframe to the user's Downloads folder."""
        path = os.path.join(Path.home(), "Downloads", f"menu_week_{self.monday_str}.xlsx")
        df.to_excel(path, index=False)
        print(f"Saved successfully to: {path}")
        os.startfile(path)
