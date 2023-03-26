# Para comenzar a rastrear sitios web, necesita solicitudes ,
#beautifoulSoup4 y un sitio web .
'''
pip install requests
pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup
url = 'https://promiedos.com.ar'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)

# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# 
content = response.content # we get all the content from the website
data = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(data.find('div',id='accordian'))

