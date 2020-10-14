import json
from selenium import webdriver

with open("../../config.json") as CONFIG_FILE:
    CONFIG = json.load(CONFIG_FILE)


class CarSearch:
    def __init__(self):
        self.price_list = []
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get(CONFIG['url'])
        self.driver.implicitly_wait(10)
        self.average = []

    def select_search(self):
        brand = self.driver.find_element_by_xpath(CONFIG['elements']['brand']).click()
        search_button = self.driver.find_element_by_xpath(CONFIG['elements']['search_button']).click()
        return self.add_to_list()

    def add_to_list(self):
        for i in self.driver.find_elements_by_class_name('price'):
            price = i.text
            self.price_list.append(int(price.rstrip(' лв.').replace(" ", "")))
        self.price_list.sort()
        return self.average_price()

    def average_price(self):
        self.average = sum(self.price_list)/len(self.price_list)
        return self.close_driver()

    def close_driver(self):
        self.driver.close()


new_search = CarSearch()
new_search.select_search()

print(f'the average car price from your search is {new_search.average} BGN')
