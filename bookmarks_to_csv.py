import re
from bs4 import BeautifulSoup
import csv

bookmark_file = "bookmarks_11_6_24.html"


def parse_bookmarks(file_content):
    soup = BeautifulSoup(file_content, "html.parser")
    bookmarks = []

    for link in soup.find_all("a"):
        href = link.get("href")
        title = link.string
        bookmarks.append({"title": title, "href": href})

    return bookmarks


def main():
    with open(bookmark_file, encoding='utf-8') as file:
        file_content = file.read()
        bookmarks = parse_bookmarks(file_content)
        for bookmark in bookmarks:
            print("Title:", bookmark["title"], "URL:", bookmark["href"])
        with open("bookmarks.csv", "w", encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "URL"])
            for bookmark in bookmarks:
                writer.writerow([bookmark["title"], bookmark["href"]])


if __name__ == "__main__":
    main()