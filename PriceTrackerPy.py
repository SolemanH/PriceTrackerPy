import requests
from bs4 import BeautifulSoup
import smtplib

# URL of the Amazon product
# URL = 'https://www.amazon.com/dp/B08G8JXZHC/'
URL = "https://www.amazon.in/OnePlus-Sierra-Black-Storage-SuperVOOC/dp/B09WRP2WXG/ref=sr_1_5?keywords=oneplus&sr=8-5"

# Desired price to get an alert
desired_price = 3199

# User agent to avoid getting blocked by Amazon
headers = {
    'User -Agent': "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    converted_price = soup.find('span', {'class': 'a-price-whole'})
    converted_price = float(converted_price.text.split()[0].replace(",", ""))
   
    print("price: ", converted_price)

    if (converted_price <= desired_price):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Your email credentials
    server.login('bhoohoo19@gmail.com', 'mhaitosfgeujrvqy')

    subject = 'Price fell down!'
    body = f'Check the Amazon link: {URL}'
    msg = f"Subject: {subject}\n\n{body}"

    # Receiver's email address
    server.sendmail('bhoohoo19@gmail.com', 'adityaks2020yo@gmail.com', msg)

    print('Email has been sent!')

    server.quit()

check_price()