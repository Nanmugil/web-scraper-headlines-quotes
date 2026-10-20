Web Scraper for Headlines & Quotes

Project Overview

This is a Python web scraping project that collects technology headlines and quotes from websites. It uses Requests to send HTTP requests and BeautifulSoup to extract information from HTML pages. The collected data is saved in TXT, JSON, and CSV formats.

Features

- Scrapes technology headlines from Hacker News.
- Extracts quotes, authors, and tags from Quotes to Scrape.
- Handles multiple pages of quotes.
- Saves scraped data in JSON and text files.
- Exports headlines and quotes into CSV files.
- Provides a menu-driven application to run the scripts easily.

Technologies Used

- Python
- Requests
- BeautifulSoup
- JSON
- CSV
- HTML

Project Structure

webScraperProject/
├── main.py
├── scraper.py
├── quotes_scraper.py
├── export_csv.py
├── headlines.json
├── headlines.txt
├── headlines.csv
├── quotes.json
├── quotes.txt
├── quotes.csv
└── README.md

Installation

1. Install Python on your computer.

2. Open the project folder in VS Code.

3. Open the terminal and create a virtual environment:
   
   "python -m venv .venv"

4. Activate the environment in Windows PowerShell:
   
   ".\.venv\Scripts\Activate.ps1"

5. Install the required libraries:
   
   "python -m pip install requests beautifulsoup4"

How to Run

Run the main application:

"python main.py"

Choose an option from the menu:

1. Scrape Technology Headlines
2. Scrape Quotes and Authors
3. Export Data to CSV
4. Exit

Output Files

- "headlines.json" — headline data in JSON format.
- "headlines.txt" — headlines in readable text format.
- "headlines.csv" — headlines and links in CSV format.
- "quotes.json" — quotes, authors, and tags in JSON format.
- "quotes.txt" — quotes and authors in readable text format.
- "quotes.csv" — quotes, authors, and tags in CSV format.

Learning Outcomes

This project helped me learn how to send HTTP requests, inspect HTML elements, extract webpage content, handle structured data, work with JSON and CSV files, and organize Python scripts into a menu-driven application.

Future Enhancements

- Add logging and improved error handling.
- Remove duplicate headlines and quotes.
- Schedule automatic scraping.
- Add a database to store collected information.
- Build a simple web interface to display results.

Note

Web scraping should follow the target website's terms of service, robots.txt guidance, and applicable rules. Use reasonable request rates and scrape only content you are permitted to access.