import requests
from bs4 import BeautifulSoup

# one item on the menu for the day
class MenuItem:
    def __init__(self, name: str, price: str) -> None:
        self.name = name
        self.price = price

class Day:
    def __init__(self, menu, date) -> None:
        self.menu = menu
        self.date = date

        

# returns a list of the 5 days of the week, containing the menu for each day
def getPlan():
    plan = []

    page = requests.get("https://studentenwerk.sh/de/mensaplandruck?ort=1&mensa=5")
    website = BeautifulSoup(page.content, 'html.parser')

    dayElements = website.find_all("div", class_="tag_headline")

    for dayElement in dayElements:
        date = (dayElement.find_all("div", class_="element_1"))
        if (len(date[0].text.split(" ")) >= 2):
            foodElements = dayElement.find_all("div", class_="mensa_menu_detail")
            menu = []
            for food in foodElements:
                price = food.find_all("div", class_="menu_preis")
                name = food.find_all("div", class_="menu_name")                
                menu.append(MenuItem(name[0].text, price[0].text))
            plan.append(Day(menu, date[0].text.split(" ")[2]))
    return plan

    
    

if (__name__ == "__main__"):
    print (getPlan().menu[0].name)