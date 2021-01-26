import requests
from bs4 import BeautifulSoup
import time

btc = "https://www.google.ru/search?newwindow=1&ei=GSoKYP2JM6KorgTJn7uwCw&q=курс+btc&oq=Курс+btc&gs_lcp=CgZwc3ktYWIQARgAMg0IABCxAxCDARBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgcIABCwAxBDOgUIABCxAzoCCC46CAgAELEDEIMBOgsIABCxAxDHARCjAjoOCAAQsQMQgwEQxwEQowI6BAgAEEM6BAguEEM6DQgAELEDEMcBEKMCEEM6BwgAELEDEEM6CggAEOoCELQCEEM6DQgAEOoCELQCEEMQiwM6CggAELEDEIMBEEM6DwgAELEDEIMBEEMQRhCCAlCg7TVYuJQ2YOGjNmgDcAJ4AIABSYgBggWSAQIxMJgBAKABAaoBB2d3cy13aXqwAQrIAQq4AQLAAQE&sclient=psy-ab"
headers = {"User-Agent": "юзер агент"}

def check_kurs():
    full_page = requests.get(btc, headers=headers)

    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb"})
    print("На " + time.ctime() + " курс BTC = " + convert[0].text)
    time.sleep(3)
    check_kurs()

check_kurs()