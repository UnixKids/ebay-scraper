import requests
from bs4 import BeautifulSoup
import pandas as pd

def search(term):
  products_list = []

  response = requests.get( url="https://www.ebay.com/sch/i.html?_nkw={}&rt=nc&LH_PrefLoc=1".format(term))
  status = response.status_code

  if status != 200:
    return 'Invalid product page! Please try a different product.'

  
  content = response.content
  soup = BeautifulSoup(response.content, 'html.parser')
  results =  soup.find_all("div", {"class":"s-item__info clearfix"})
  

  for item in results:
    products = { 
      'Title': item.find("h3", {"class":"s-item__title"}).text,
      'URL': item.find("a", {"class":"s-item__link"})['href'].split("?")[0],
      'Price': item.find("div", {"class":"s-item__detail"}).text
    }     
    products_list.append(products)
    
  print("Creating products_list.csv file")
  df = pd.DataFrame(products_list[1:])
  df.to_csv('products_list.csv', index=False)


  return df


print(search(input("What would you like to search for today?\n")))

