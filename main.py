import subprocess
import sys


def run_script(filename):
    print(f"\nRunning {filename}...\n")

    try:
        result = subprocess.run(
            [sys.executable, filename],
            check=False
        )

        if result.returncode == 0:
            print(f"\nFinished running {filename}.")
        else:
            print(f"\n{filename} ended with an error.")

    except OSError as error:
        print(f"Could not run {filename}: {error}")


def show_menu():
    while True:
        print("\n" + "=" * 40)
        print("       WEB SCRAPER APPLICATION")
        print("=" * 40)
        print("1. Scrape Technology Headlines")
        print("2. Scrape Quotes and Authors")
        print("3. Export Data to CSV")
        print("4. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            run_script("scraper.py")

        elif choice == "2":
            run_script("quotes_scraper.py")

        elif choice == "3":
            run_script("export_csv.py")

        elif choice == "4":
            print("Thank you for using Web Scraper!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    show_menu()