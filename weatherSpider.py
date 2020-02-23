import requests
from lxml import etree

class WeatherSpider:

     def __init__(self):
         self.url = "http://www.weather.com.cn/weather1d/101200702.shtml"
         self.headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

     def get_url_content(self):
         return requests.get(self.url, headers=self.headers).content.decode()

     def get_weather_data(self, html):
         tmp_html = etree.HTML(html)
         tomorrow_doc = tmp_html.xpath("//div[contains(@class,'con') and contains(@class,'today')]//div[@class='c7d']/ul/li[2]")[0]
         weather_data = {}
         weather_data["date"] = tomorrow_doc.xpath("./h1/text()")[0]
         weather_data["weather"] = tomorrow_doc.xpath("./p[@class='wea']/@title")[0]
         weather_data["temperature_max"] = tomorrow_doc.xpath("./p[@class='tem']/span/text()")[0]
         weather_data["temperature_min"] = tomorrow_doc.xpath("./p[@class='tem']/i/text()")[0]
         weather_data["air_speed"] = tomorrow_doc.xpath("./p[@class='win']/i/text()")[0]
         return weather_data
         content_html = self.get_url_content()
         data = self.get_weather_data(content_html)
         print(data)
