import csv
import json
from pathlib import Path


def export_headlines():
    input_file = Path("headlines.json")

    if not input_file.exists():
        print("Error: headlines.json not found.")
        return

    try:
        with input_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        headlines = data.get("headlines", [])

        with open(
            "headlines.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "link"]
            )

            writer.writeheader()
            writer.writerows(headlines)

        print(f"Exported {len(headlines)} headlines to headlines.csv")

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not export headlines: {error}")


def export_quotes():
    input_file = Path("quotes.json")

    if not input_file.exists():
        print("Error: quotes.json not found.")
        return

    try:
        with input_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        quotes = data.get("quotes", [])

        with open(
            "quotes.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["quote", "author", "tags"]
            )

            writer.writeheader()

            for item in quotes:
                writer.writerow({
                    "quote": item.get("quote", ""),
                    "author": item.get("author", ""),
                    "tags": ", ".join(item.get("tags", []))
                })

        print(f"Exported {len(quotes)} quotes to quotes.csv")

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not export quotes: {error}")


if __name__ == "__main__":
    export_headlines()
    export_quotes()

    print("CSV export process finished.")