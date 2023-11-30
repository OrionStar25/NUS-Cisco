import json 


# Dump dictionary into a json file
def write_to_json(filename, dictionary):
    with open(filename, "w") as outfile: 
        json.dump(dictionary, outfile)


# import requests 
# from bs4 import BeautifulSoup as bs 
# import csv 

# URL = 'https://www.geeksforgeeks.org/page/1/'

# soup = bs(req.text, 'html.parser') 

# titles = soup.find_all('div', attrs={'class', 'head'}) 
# titles_list = [] 

# count = 1
# for title in titles: 
# 	d = {} 
# 	d['Title Number'] = f'Title {count}'
# 	d['Title Name'] = title.text 
# 	count += 1
# 	titles_list.append(d) 

# filename = 'titles.csv'
# with open(filename, 'w', newline='') as f: 
# 	w = csv.DictWriter(f,['Title Number','Title Name']) 
# 	w.writeheader() 
	
# 	w.writerows(titles_list)
