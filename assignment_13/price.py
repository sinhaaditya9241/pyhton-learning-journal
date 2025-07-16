import requests 
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "html.parser")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text
        else:
            return "title not found"

    def product_price(self):
        price = self.soup.find("span", {"id": "=priceblock_ourprice"})
        if price is not None:
            return price.text.strip()
        else:
            return "tag not found"


device = PriceTracer(url= "https://www.amazon.in/Samsung-Smartphone-Storage-Powerful-Snapdragon/dp/B0FDL3VZR8/ref=sr_1_1_sspa?crid=23IRC6RL1K94J&dib=eyJ2IjoiMSJ9.YnowC3VQbYtXGwWvySYEbXY-VUD_Qiw7nINp4kAGOEttDfDdsHB_BDQNKT-6wdOe7Lcv2AqlZNurtj2s-aYm69EwSodJLj_extyadtA84HZM4Qqjg3MNgw33GgHSRi7S5QHYEnGiX-Od0cMbZmaH4ATPbDzBEjtrUg1H-LfWV8dZGxa3EfLjHHmvQJDiKPh-IFRdeVbIGU_25Wtr-oeqAN9UwJwOEavPMtxFxykKGhs.6DRobT3ivjKTl4hMtSTFrTaSvgHJVNYVM3qlwxrEoOw&dib_tag=se&keywords=samsung%2Bfold%2B7%2B5g&nsdOptOutParam=true&qid=1752667099&sprefix=samsung%2Bfold%2B7%2B5g%2Caps%2C477&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

print(device.product_title())
print(device.product_price())

