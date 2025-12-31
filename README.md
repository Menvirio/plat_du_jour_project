# plat_du_jour_project
# Multi-Restaurant Menu Scraper 🍴

An automated Python solution designed to scrape, process, and aggregate daily specials ("Plat du Jour") from multiple restaurant websites into a single, organized Excel report.

## 📌 Project Overview
Checking multiple restaurant websites every day to find the best lunch option can be time-consuming. This project automates that process by:
1. **Fetching** HTML content from a list of predefined restaurant URLs.
2. **Parsing** specific CSS classes to extract the "Day of the Week" and the "Dish Description."
3. **Cleaning** and normalizing the data (handling multiple dishes per day and fixing capitalization).
4. **Pivoting** the data into a matrix format (Days as rows, Restaurants as columns).
5. **Exporting** the final menu directly to the user's local `Downloads` folder for immediate viewing.

## 🏗️ Project Structure
The repository is organized following clean-code principles and separation of concerns:

* `main.py`: The entry point of the application. It contains the configuration (URLs) and executes the scraping workflow.
* `scraper.py`: Contains the `MenuScraper` class logic. This is the "engine" that handles HTTP requests, BeautifulSoup parsing, and Pandas transformations.
* `requirements.txt`: Lists the external libraries required to run the tool.
* `.gitignore`: Prevents local system files and generated Excel reports from being tracked in version control.

## 🛠️ Technical Stack
- **Python 3.x**
- **Requests**: For handling HTTP GET requests.
- **BeautifulSoup4**: For parsing HTML and navigating the DOM.
- **Pandas**: For advanced data manipulation, grouping, and pivoting.
- **OpenPyXL**: The engine used by Pandas to generate `.xlsx` files.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed on your system. You can check this by running:
```bash
python --version
