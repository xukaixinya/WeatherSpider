import requests
from lxml import etree


class WeatherSpider:

    def __init__(self):
        self.__city__maps = {
            "wuhan": "http://www.weather.com.cn/weather1d/101200702.shtml",
            "chibi": "http://www.weather.com.cn/weather1d/101200702.shtml",
            "shanghai": "http://www.weather.com.cn/weather1d/101200702.shtml"

        }
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.119 Safari/537.36"}

    @property
    def get_url_content(self):
        if city_name in self.__city__maps:
            return requests.get(self.__city__maps, headers=self.__headers).content.decode()
        else:
            return requests.get("http://www.weather.com.cn/weather1d/101200702.shtml",
                                headers=self.__headers).content.decode()

    def get_weather(self, html):
        tmp_html = etree.HTML(html)
        content_html = self.get_url_content
        self.get_weather(content_html)
        tomorrow_doc = tmp_html.xpath("//div[contains(@class,'con') and contains(@class,'today')]//div["
                                      "@class='c7d']/ul/li[2]")[0]
        weather_data = {"date": tomorrow_doc.xpath("./h1/text()")[0],
                        "weather": tomorrow_doc.xpath("./p[@class='wea']/@title")[0],
                        "temperature_max": tomorrow_doc.xpath("./p[@class='tem']/span/text()")[0],
                        "temperature_min": tomorrow_doc.xpath("./p[@class='tem']/i/text()")[0],
                        "air_speed": tomorrow_doc.xpath("./p[@class='win']/i/text()")[0]}

        return weather_data


if __name__ == '__main__':
    city_name = "wuhan"
    spider = WeatherSpider()
    spider.get_weather()