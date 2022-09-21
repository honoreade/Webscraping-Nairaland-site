import requests
from bs4 import BeautifulSoup

url = 'https://www.nairaland.com/politics'
page = requests.get(url)

# print(page.status_code)
# print(page.text.encode("utf-8"))
  
soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())
title = soup.find_all('h2')[0].get_text().upper()
print(title)

content = soup.find_all('table')[2]

a = 0
while a <50:
    a +=1
    contentlink = content.find_all('td')[a]
    contentlink1 = contentlink.find_all('b')[0].get_text()
    contentlink2 = contentlink.find_all('b')[2].get_text()
    contentlink3 = contentlink.find_all('b')[4].get_text()
    contentlink4 = contentlink.find_all('b')[5].get_text()


    # contentlink2 = contentlink1.find_all('a')[0].get_text()
    print(str(a)+"."+ contentlink1)
     # print(a)
    # print(contentlink1)
    print("By",contentlink2.upper() + " "+ "//Views:",contentlink3 + " "+ "//At: ",contentlink4)

    #########link#########
    contentlink10 = contentlink.find_all('b')[0]
    contentlink11 = contentlink10.find_all('a')[0]
    print("Link: ",contentlink10)
    print()


    