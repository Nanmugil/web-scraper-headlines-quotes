import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Website URL
URL = "https://news.ycombinator.com/"

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"
}


def scrape_headlines():
    try:
        # Send an HTTP request
        response = requests.get(
            URL, headers=headers, timeout=15
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Read and inspect HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines and their links
        articles = []

        for item in soup.select(".titleline > a"):
            title = item.get_text(" ", strip=True)
            link = item.get("href")

            if title and link:
                articles.append({
                    "title": title,
                    "link": link
                })

        if not articles:
            print("No headlines found. Check the HTML selectors.")
            return

        # Add scraping timestamp
        result = {
            "scraped_at": datetime.now().isoformat(
                timespec="seconds"
            ),
            "source": URL,
            "total_headlines": len(articles),
            "headlines": articles
        }

        # Save as JSON
        with open(
            "headlines.json", "w", encoding="utf-8"
        ) as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

        # Save as readable text
        with open(
            "headlines.txt", "w", encoding="utf-8"
        ) as file:
            file.write("TECHNOLOGY HEADLINES\n")
            file.write("=" * 50 + "\n\n")

            for number, article in enumerate(articles, start=1):
                file.write(f"{number}. {article['title']}\n")
                file.write(f"   Link: {article['link']}\n\n")

        print(f"Successfully collected {len(articles)} headlines.")
        print("Saved to headlines.txt and headlines.json")

    except requests.exceptions.Timeout:
        print("Error: The website took too long to respond.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    scrape_headlines()