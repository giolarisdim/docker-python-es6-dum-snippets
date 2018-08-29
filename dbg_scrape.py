from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/computers").text

soup = BeautifulSoup(source,'lxml')
csv_file = open('dbg_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['description','price'])

for article in soup.find_all(class_='caption'):
    #print(article.prettify())
    description = article.p.text
    print (description)

    price1 = article.find('h4', class_='pull-right price').text
    price2=price1.split('$')
    price=price2[1]
    print(price)

    print()

    csv_writer.writerow([description,price])

csv_file.close()














