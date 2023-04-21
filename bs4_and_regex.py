from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

url = 'https://www.ethoswatches.com/mens-watches.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
watches = {}
watch_no = 0
while True:
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.find_all('div', {'class': 'product_hoverWrap'})
    for content in contents:
        title_tag = content.find('span', {'class': 'collection_name'})
        title = title_tag.text if title_tag else "N/A"
        name_tag = content.find('h2', {'class': 'brand_name'}).find('a')
        name = name_tag.text if name_tag else "N/A"
        img_tag = content.find('img', {'class': 'product-image-photo'})
        img = img_tag['src'] if img_tag else "N/A"
        price_tag = content.find('span', {'class': 'price'})
        price = price_tag.text[2:] if price_tag else 'N/A'
        watch_no += 1
        watches[watch_no] = [title, name, img, price]
    try:
        url_tag = soup.find('a', {'title': "Next"})['href']
    except:
        break
    if url_tag:
        url = url_tag
        print(url_tag)
    else:
        break
print("Total Watches", watch_no)
watches_df = pd.DataFrame.from_dict(watches, orient='index', columns=[
                                    'Brand', 'Name', 'Img_Url', 'Price'])
watches_df.to_csv('watches_new.csv')
