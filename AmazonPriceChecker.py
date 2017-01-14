import requests
from bs4 import BeautifulSoup
import time
    
def main():
    #s="moto m"
    s = raw_input("Enter product name ")
    amazon(s)
    

def spider(url):
    source = requests.get(url)
    ptext = source.text
    soup = BeautifulSoup(ptext, "html.parser")
    print(soup.title.string)
    print ("\n")
    return soup


def amazon(s):
    s = s.replace(" ", "+")
    url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(s)
    print(url)
    soup = spider(url)
    link =soup.find('a', {'class': 'a-link-normal', 'class': 's-access-detail-page',
                                   'class': 'a-text-normal'})
    href = link.get('href')
    print(href)
    price_checker(href)
        

def price_checker(url):
   time.sleep(3)
   soup = spider(url)
   p_name = soup.find(attrs={'id':'productTitle'})
   p_our_price = soup.find(attrs={'id':'priceblock_ourprice'})
   p_deal_price = soup.find(attrs={'id':'priceblock_dealprice'})
   p_sale_price = soup.find(attrs={'id':'priceblock_saleprice'})
   if p_deal_price:
        new_price=p_deal_price.text.replace(',','').strip()
   elif p_our_price:
        new_price=p_our_price.text.replace(',','').strip()
   elif p_sale_price:
        new_price=p_sale_price.text.replace(',','').strip()
   print ("Name: " +str(p_name.string))
   print ("Price: Rs "+new_price)
  
  
main()  
