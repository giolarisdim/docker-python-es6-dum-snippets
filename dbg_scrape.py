from bs4 import BeautifulSoup
import requests
import csv

## the source page is for educational use
source = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/computers").text


## using BeatifulSoup library we pull data out of HTML file
soup = BeautifulSoup(source,'lxml')
## we will use it as a csv file with writing permisions so we can build two rows
csv_file = open('dbg_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['description','price'])


## here we will find and store the data that we need to fill our empty rows
for article in soup.find_all(class_='caption'):
    #print(article.prettify()) makes reading easier
    #data for description
    description = article.p.text
    print (description)

    #data for price
    price1 = article.find('h4', class_='pull-right price').text
    price2=price1.split('$')
    price=price2[1]
    print(price)
    print()

    ## here we will fill our file with data
    csv_writer.writerow([description,price])

csv_file.close()
