import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

EMAIL="YOUR EMAIL"
PASS="YOUR PASSWORD"
BUY_PRICE=80
subject="Amazon price Alert"
below_price=f"Price is below your buy price of {BUY_PRICE}"
my_http_header={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

}

URL="https://www.amazon.com/dp/B075CYMYK6/ref=twister_B0CZ9G83PC?_encoding=UTF8&th=1"
response=requests.get(URL)
amazon_web=response.text
soup=BeautifulSoup(amazon_web,"html.parser")
title=soup.find(id="productTitle",class_="a-size-large product-title-word-break").getText().strip()
price = soup.find(class_='a-price-whole')


decimal = soup.find(class_='a-price-fraction')
full_price = float(price.getText() + decimal.getText())



if full_price<=BUY_PRICE:
    content= f"{title} is now {full_price}"
    
    with SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASS)
        connection.sendmail(from_addr=EMAIL,
                     to_addrs=EMAIL,
                             msg=f"Subject:{subject}\n\n{content} and the url is {URL} ".encode("utf-8"))
    print(f"Email sent\n\nthe price of the product is {full_price}")  
        



        


