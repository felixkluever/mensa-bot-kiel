import requests
from bs4 import BeautifulSoup

def getPlan():
    SPACER = "\n" + ("-"*80) + "\n"
    output = ""

    Page = requests.get("https://studentenwerk.sh/de/mensaplandruck?ort=1&mensa=5")
    website = BeautifulSoup(Page.content, 'html.parser')

    output += SPACER

    day_elements = website.find_all("div", class_="tag_headline")
    for day in day_elements:
        date = day.find("div", class_="element_1")
        if (len(date.text.split(" ")) >= 2):
            output += date.text.split(" ")[2]
            food_elements = day.find_all("div", class_="menu_name")
            for food in food_elements:
                output += food.text + "\n"
            output += SPACER
    return output