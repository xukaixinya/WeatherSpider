import urllib.request
import requests
from bs4 import BeautifulSoup
class WeatherSpider:

    def __init__(self):
        self.location=input("enter your location:")
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64;\
        rv:23.0) Gecko/20100101 Firefox/23.0'}
        self.website="http://www.tianqi.com/" + self.location + ".html"
        #req = urllib.request.Request(url=website, headers=header)

    def get_url_content(self):
        return requests.get(self.website,headers=self.header)

    def get_weather(self):
        page = urllib.request.urlopen(requests)
        html = page.read()
        soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
        nodes = soup.find_all('dd')
        today_weather = ""
        for node in nodes:
            temp = node.get_text()
            if (temp.find('[切换城市]')):
                temp = temp[:temp.find('[切换城市]')]
            today_weather += temp
        weather = "".join([s for s in today_weather.splitlines(True)
                           if s.strip()])
        return weather

    def run(self):
        content_html = self.get_url_content()
        data = self.get_weather_data(content_html)
        print(data)