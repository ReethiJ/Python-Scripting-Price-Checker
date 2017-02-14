import requests
from bs4 import BeautifulSoup
import time
    
def main():
    s = raw_input("Enter product name: ")
    amazon(s)
    

def spider(url):
    source = requests.get(url)
    ptext = source.text
    soup = BeautifulSoup(ptext, "html.parser")
    print ("\n")
    return soup


def amazon(s):
    s = s.replace(" ", "+")
    url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(s)
    soup = spider(url)
    time.sleep(3)
    for link in soup.findAll('a', {'class': 'a-link-normal', 'class': 's-access-detail-page',
                                   'class': 'a-text-normal'}):
        if(link.get('href')):
            href = link.get('href')
            time.sleep(3)
            price_checker(href)
            break
       
        

def price_checker(url):   
   soup = spider(url)
   p_name = soup.find(attrs={'id':'productTitle'})
   print ("Name: " +str(p_name.string.strip()))
   p_our_price = soup.find(attrs={'id':'priceblock_ourprice'})
   p_deal_price = soup.find(attrs={'id':'priceblock_dealprice'})
   p_sale_price = soup.find(attrs={'id':'priceblock_saleprice'})
   if p_deal_price:
        new_price=p_deal_price.text.replace(',','').strip()
   elif p_our_price:
        new_price=p_our_price.text.replace(',','').strip()
   elif p_sale_price:
        new_price=p_sale_price.text.replace(',','').strip()
   print ("Price: Rs "+new_price)
 
    

main()
