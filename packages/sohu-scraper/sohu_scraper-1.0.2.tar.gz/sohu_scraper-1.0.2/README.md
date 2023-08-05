### Title

Sohu.com Scraper

### Descrption

* With Sohu.com Scraper you can scrape search results and extract the contents produced by the search result.
* In Sohu scraper it will scrape the data present of the website and give json data which contains the details of the contents on the website.

### JSON sample data
```sh
{
    "Scraper_\u9999\u6e2f\u9762\u5411\u5185\u5730\u5f15\u8fdb\u4eba\u624d_\u7b26\u5408\u6761\u4ef6\u53ef\u7533\u8bf7\u9999\u6e2f\u8eab\u4efd": [
        {
            "blank": "\u65b0\u4eac\u62a5",
            "feed_four_title_style_link": "https://www.sohu.com/a/499810521_114988?scm=1004.773955565398458368.0.0.672&spm=smpc.ch13.fd-news.1.1636356674692YG6AwTs",
            "feed_publish": "\u4eca\u5929 04:28",
            "feed_visited_theme_history_color_hover": "\u4eac\u534e\u7269\u8bed\u4e28\u57281920\u5e74\u4ee3\u7684\u5317\u4eac\uff0c\u4eba\u529b\u8f66\u771f\u53ef\u8c13\u516c\u5171\u5947\u666f",
            "profile_link": "http://mp.sohu.com/profile?xpt=c29odXptdDNqdHpnY0Bzb2h1LmNvbQ==&spm=smpc.ch13.fd-news.1.1636356674692YG6AwTs"
        }
```

[Click Here for more](https://datakund-scraper.s3.amazonaws.com/fors2d22ace_VKDU2XN03IQ3VD7_json.json)
					  

### Run Scraper
```sh
from sohu_scraper import *
link="http://history.sohu.com/?spm=smpc.home.history-nav.1.1633101794696TEciRMP"
data=run_sohu_scraper(link)
```

### How it works?
* It takes URL of Sohu page with a search keyword to scrape the data.
* It generates the json data which contains the information of the sohu search result.
* It gives the every detail present inside website in the form of json data.


### Examples
Below are some of the examples of URLs using which you can scrape:

* [Example 1](http://history.sohu.com/?spm=smpc.home.history-nav.1.1633101794696TEciRMP)

* [Example2](http://cul.sohu.com/?spm=smpc.home.cul-nav.1.1633101794696TEciRMP)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)