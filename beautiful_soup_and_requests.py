from bs4 import BeautifulSoup
import requests
from csv import writer

# pages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# add header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


# list_of_page = soup.find(class_="product-list-plp")
# print(list_of_page)
# for list_ in list_of_page:
#     titles = list_of_page.select(".pro-name")
#     print(title.get_text().replace('\n', ''))
page_content = requests.get(
    url="https://www.helioswatchstore.com/smartwatches", headers=headers)
soup = BeautifulSoup(page_content.content, "html.parser")
contents = soup.select(".fetch-compare")
print(len(contents))
with open('watches.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Brand & Name', "Price", "Url"]
    csv_writer.writerow(headers)
    for content in contents:
        title = content.select_one("h2 span").get_text()
        name = content.select_one("h2").get_text().replace("\n", '')
        price = content.select_one("font").get_text()[2:]
        urls = content.select_one(".pro_img img")['src']
        csv_writer.writerow([name, price, urls])
