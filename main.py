import requests
from bs4 import BeautifulSoup as BS 
import csv 

def get_html(url):
    response = requests.get(url)
    return response.text 

def get_soup(html):
    soup = BS(html,'lxml')
    return soup



def get_laptops(soup):
    news = soup.find_all('div',class_='ty-column4')

    for news in laptops:
        news.find('img',class_='ty-pict')
        try:
            title= news.find('a', class_='product-title').text.strip()
        
        except AttributeError:
            title = ''
        
        try:
            price = news.find('span',class_='ty-price-num').text.strip()

        except AttributeError:
            price = ''

        try: 
            image=news.find('img',class_='ty-pict').get('data-ssrs')
        
        except AttributeError:

            image =''

        write_csv({
            'title': title,
            'price': price,
            'image': image
        })

def write_csv(data):
    with open('news.csv','a')as file:
        names =['title', 'price','image']
        write = csv.DictWriter (file, delimiter=',',fieldnames=names)
        write .writerow(data)



url = 'https://vesti.kg/zxc/item/107709-mvf-sprognoziroval-vozvrashchenie-trudovykh-migrantov-iz-za-spada-v-rossijskoj-ekonomike-chto-sprovotsiruet-novyj-rost-inflyatsii-v-kyrgyzstane.html'
import requests
from bs4 import BeautifulSoup as BS 
import csv 

def get_html(url):
    response = requests.get(url)
    return response.text 

def get_soup(html):
    soup = BS(html,'lxml')
    return soup



def get_news(soup):
    news = soup.find_all('div',class_='ty-column4')

    for news in news:
        news.find('img',class_='ty-pict')
        try:
            title= news.find('a', class_='product-title').text.strip()
        
        except AttributeError:
            title = ''
        
        try:
            price = news.find('span',class_='ty-price-num').text.strip()

        except AttributeError:
            price = ''

        try: 
            image=news.find('img',class_='ty-pict').get('data-ssrs')
        
        except AttributeError:

            image =''

        write_csv({
            'title': title,
            'price': price,
            'image': image
        })

def write_csv(data):
    with open('news.csv','a')as file:
        names =['title', 'price','image']
        write = csv.DictWriter (file, delimiter=',',fieldnames=names)
        write .writerow(data)

def main():
    
    for i in range(5):

      url = f'https://vesti.kg/zxc/item/107709-mvf-sprognoziroval-vozvrashchenie-trudovykh-migrantov-iz-za-spada-v-rossijskoj-ekonomike-chto-sprovotsiruet-novyj-rost-inflyatsii-v-kyrgyzstane.html{i}'
      html = get_html(url)
      soup = get_soup(html)
      get_laptops(soup)
      print(f'спарсили {i} новости ')
if __name__=='__name__':

     main()


