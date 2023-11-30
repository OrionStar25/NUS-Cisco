import requests

from bs4 import BeautifulSoup 
from utils import *


def parse_categories(url):
    r = requests.get(url) 
    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser') 

    # Finding by id 
    s = soup.find('div', id= 'productCategories') 
    # Getting the category rows 
    rows = s.find('tr') 
    # All the li under the above tr 
    content = rows.find_all('li') 

    # Scrape categories
    categories = {}
    for c in content:
        category = c.text
        link = 'https:' + c.find('a')['href']
        categories[category] = link

    return categories


def parse_product_typeA(soup, map, cat):
    products = []
    s = soup.find('ul', id='prodByAlpha')
    content = s.find_all('li')

    for c in content:
        products.append(c.text)
    
    map[cat] = products


def parse_product_typeB(soup, map, cat):
    products = []
    s = soup.find('ul', id='alphabetical')
    content = s.find_all('li')

    for c in content:
        products.append(c.text)

    if cat == "TelePresence":
        products = products[:-2]
    map[cat] = products


def parse_product_networking_tech_and_protocols(soup, map, cat):
    s = soup.find('div', class_='tech-container')
    col = s.find('div', class_='col')
    sub_cats = {}
    curr_sub_cat = None

    for c in col:
        h = str(c)
        if 'h3' in h:
            curr_sub_cat = c.text
            sub_cats[curr_sub_cat] = []
        elif curr_sub_cat is not None:
            text = (c.text).strip('\n')
            if len(text) > 0:
                texts = text.split('\n')
                for t in texts:
                    sub_cats[curr_sub_cat].append(t)

    map[cat] = sub_cats


def parse_product_typeC(soup, map, cat):
    s = soup.find_all('div', class_='col')
    for i, c in enumerate(s):
        h = str(c)
        if 'A-Z' in h:
            break

    content = s[i].find_all('li')
    products = []

    for c in content:
        products.append(c.text.strip('\n'))
   
    map[cat] = products[:-2]


def parse_product_data_analytics(soup, map, cat):
    s = soup.find_all('div', class_='col')
    for i, c in enumerate(s):
        h = str(c)
        if 'All Supported Data Center Analytics Products' in h:
            break

    content = s[i+1].find_all('li')
    products = []

    for c in content:
        products.append(c.text.strip('\n'))
   
    map[cat] = products


def main():
    url = 'https://www.cisco.com/c/en/us/support/all-products.html'
    categories = parse_categories(url)
    write_to_json("categories.json", categories)

    # Scrape products for each category

    # Software (Cisco ONE)

    NO_PRODUCTS = ['Services Support', 'Small Business Product Support']
    PRODUCT_TYPE_A = [
        "Accessories (Interfaces, Modules, Cards)",
        "Cloud and Systems Management",
        "Collaboration Endpoints",
        "Conferencing",
        "Connected Safety and Security",
        "Contact Center ",
        "Optical Networking",
        "Routers",
        "Security",
        "Servers - Unified Computing (UCS)",
        "Storage Networking",
        "Switches",
        "Unified Communications",
        "Video",
        "Wireless"
    ]
    PRODUCT_TYPE_B = [
        "TelePresence",
        "Webex"
    ]
    PRODUCT_TYPE_C = [
        'Networking Software (IOS & NX-OS)',
        'Hyperconverged Infrastructure'
    ]

    categories_products_map = {}

    for cat, link in categories.items():
        if cat in NO_PRODUCTS:
            continue

        print(cat)
        r = requests.get(link) 
        soup = BeautifulSoup(r.content, 'html.parser')

        if cat in PRODUCT_TYPE_A:
            parse_product_typeA(soup, categories_products_map, cat)
        elif cat in PRODUCT_TYPE_B:
            parse_product_typeB(soup, categories_products_map, cat)
        elif cat in PRODUCT_TYPE_C:
            parse_product_typeC(soup, categories_products_map, cat)
        elif cat == 'Networking Technologies and Protocols':
            parse_product_networking_tech_and_protocols(soup, categories_products_map, cat)
        elif cat == 'Data Center Analytics':
            parse_product_data_analytics(soup, categories_products_map, cat)
        
            
        
    print(len(categories_products_map))
    write_to_json("categories_products.json", categories_products_map)


if __name__=="__main__": 
    main() 
