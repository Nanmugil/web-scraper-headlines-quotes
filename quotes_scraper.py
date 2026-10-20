import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"
}

MAX_PAGES = 10


def scrape_quotes():
    all_quotes = []
    current_url = BASE_URL
    visited_pages = 0

    try:
        with requests.Session() as session:
            session.headers.update(HEADERS)

            while current_url and visited_pages < MAX_PAGES:
                print(f"Scraping page {visited_pages + 1}...")

                response = session.get(
                    current_url,
                    timeout=15
                )
                response.raise_for_status()

                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )

                quote_blocks = soup.find_all(
                    "div",
                    class_="quote"
                )

                if not quote_blocks:
                    print("No quotes found on this page.")
                    break

                for block in quote_blocks:
                    quote_element = block.find(
                        "span",
                        class_="text"
                    )
                    author_element = block.find(
                        "small",
                        class_="author"
                    )

                    tag_elements = block.find_all(
                        "a",
                        class_="tag"
                    )

                    if quote_element and author_element:
                        all_quotes.append({
                            "quote": quote_element.get_text(
                                strip=True
                            ),
                            "author": author_element.get_text(
                                strip=True
                            ),
                            "tags": [
                                tag.get_text(strip=True)
                                for tag in tag_elements
                            ]
                        })

                visited_pages += 1

                # Find the next-page link
                next_link = soup.select_one(
                    "li.next a"
                )

                if next_link:
                    current_url = urljoin(
                        current_url,
                        next_link.get("href", "")
                    )
                else:
                    current_url = None

        if not all_quotes:
            print("No quotes collected.")
            return

        result = {
            "scraped_at": datetime.now().isoformat(
                timespec="seconds"
            ),
            "source": BASE_URL,
            "pages_visited": visited_pages,
            "total_quotes": len(all_quotes),
            "quotes": all_quotes
        }

        with open(
            "quotes.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                result,
                file,
                indent=4,
                ensure_ascii=False
            )

        with open(
            "quotes.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write("QUOTES AND AUTHORS\n")
            file.write("=" * 50 + "\n\n")

            for number, item in enumerate(
                all_quotes,
                start=1
            ):
                file.write(
                    f"{number}. {item['quote']}\n"
                )
                file.write(
                    f"   Author: {item['author']}\n"
                )
                file.write(
                    f"   Tags: {', '.join(item['tags'])}\n\n"
                )

        print(f"\nPages visited: {visited_pages}")
        print(f"Total quotes: {len(all_quotes)}")
        print("Updated quotes.json")
        print("Updated quotes.txt")
        print("Scraping completed successfully!")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    scrape_quotes()