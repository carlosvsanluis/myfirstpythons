trial.py


import.urlib.request
import time

price = 99.99
while price > 60
    time sleep(900)
    page = urlib.request.urlopen("http://www.techbzh.com")
    text =page.read().decode("utf8")
    where = text.find('carlosv')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])
print ("Buy")