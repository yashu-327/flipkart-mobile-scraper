import requests
import pandas as pd
from bs4 import BeautifulSoup
responce=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
print(responce)
soup=BeautifulSoup(responce.content,'html.parser')
names=soup.find_all('div',class_="RG5Slk")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
prices=soup.find_all('div',class_='hZ3P6w DeU9vF')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
images=soup.find_all('img',class_='UCc1lI')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
ratings=soup.find_all('div',class_='MKiFS6')
rating=[]
for i in ratings[0:20]:
    d=i.get_text()
    rating.append(d)
links=soup.find_all('a',class_='k7wcnx')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
df=pd.DataFrame()
df['Names']=name
df['Prices']=price
df['Images']=image
df['Ratings']=rating
df['Links']=link
df.to_csv("mobiles_details.csv")
