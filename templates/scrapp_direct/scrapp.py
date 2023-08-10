import json

import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class Scrappy:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("URL")

    def get_scrappy(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            get_info = soup.find("div", class_="prose md:prose-md xl:prose-xl content-other distance-1-5")

            quote_elements = get_info.find_all("h3")

            quotes_list = [{"{}".format(index + 1): quote.text} for index, quote in enumerate(quote_elements)]

            with open("motivational_quotes.json", "w") as json_file:
                json.dump(quotes_list, json_file, ensure_ascii=False, indent=4)

            print("Quotes saved to motivational_quotes.json")
            return True
        else:
            print("Failed to retrieve the page")
            return False
