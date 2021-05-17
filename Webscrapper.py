from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

pages = list(range(1,6))
for page in pages:
    my_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&q=iphone&otracker=categorytree&page={}".format(page)
    uClient = urlopen(my_url)
    html_page = uClient.read()
    uClient.close()
    page_html = BeautifulSoup(html_page, "html.parser")

    outputs = page_html.findAll('div', {'class': '_2kHMtA'})
    #print(len(outputs))

    #print(BeautifulSoup.prettify(outputs[0]))

    #output = outputs[0]
    #print(output.div.img['alt'])

    #price = output.findAll('div',{'class' : 'col col-5-12 nlI3QM'})
    #print(price[0].text)


    #ratings = output.findAll('div',{'class': 'gUuXy-'})
    #print(ratings[0].text)

    file = "products.csv"
    f = open(file, "w")
    headers = "Products_Name,Pricing,Ratings\n"
    f.write(headers)

    for output in outputs:
        product_name = output.div.img['alt']

        price_output = output.findAll('div', {'class': 'col col-5-12 nlI3QM'})
        price = price_output[0].text.strip()

        rating_output = output.findAll('div', {'class': 'gUuXy-'})
        rating = rating_output[0].text

        #print("product_name:" + product_name)
        #print("price:" + price)
        #print("rating:" + rating)

        ### string parsing
        split_rating = rating.split(" ")
        final_rating = split_rating[0]

        trim_price = ''.join(price.split(','))
        rm_rupee = trim_price.split("₹")
        add_rs_price = "Rs" + rm_rupee[1]
        split_price = add_rs_price.split('E')
        final_price = split_price[0]

        print(product_name.replace(',', '|') + ',' + final_price + ',' + final_rating + "\n")
        f.write(product_name.replace(',', '|') + ',' + final_price + ',' + final_rating + "\n")




f.close()















