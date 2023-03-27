# Para comenzar a rastrear sitios web, necesita solicitudes ,
#beautifoulSoup4 y un sitio web .
'''
pip install requests
pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)

# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# 
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title)

### Exercises: Day 22

# 1 - the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# 2 - Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# 3 - Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
