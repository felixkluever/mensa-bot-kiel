import scraper

plan = scraper.getPlan()

i = 1

for day in plan:
    print ("day:" , i)
    i += 1
    print ("date: " , day.date)
    for item in day.menu:
        print(item.name)
        print(item.price)
    print("\n")