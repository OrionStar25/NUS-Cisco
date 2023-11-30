import requests 
import json 

from bs4 import BeautifulSoup 


url = 'https://www.cisco.com/c/en/us/support/all-products.html'
r = requests.get(url) 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
# Finding by id 
s = soup.find('div', id= 'productCategories') 
# Getting the category rows 
rows = s.find('tr') 
# All the li under the above tr 
content = rows.find_all('li') 

categories = {}
for c in content:
    category = c.text
    link = c.find('a')['href'][2:]
    
    categories[category] = link
    
	
# Dump categories into a json file
with open("categories.json", "w") as outfile: 
	json.dump(categories, outfile)
