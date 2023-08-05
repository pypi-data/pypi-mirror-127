### Title

gome Scraper

### Descrption

* With gome Scraper you can scrape search results and extract the contents produced by the search result.
* In gome scraper it will scrape the data present of the website and give json data which contains the details of the contents on the website.

### JSON sample data
```sh
{
    "Scraper_repeat_data_0": [
        {
            "column_8": [
                {
                    "link": "//item.gome.com.cn/9140059322-1130765898.html",
                    "text": "   \u7c73\u5bb6\u58f0\u6ce2\u7535\u52a8\u7259\u5237T100  \u5475\u62a4\u7259\u9f88 IPX7\u9632\u6c34 \uffe535.00 \u7acb\u5373\u8d2d\u4e70  "
                },
                {
                    "link": "//item.gome.com.cn/9140056902-1130548362.html",
                    "text": "   \u5c0f\u7c73AI\u97f3\u7bb1 \u4eba\u5de5\u667a\u80fd\u97f3\u54cd \uffe5176.00 \u7acb\u5373\u8d2d\u4e70  "
                }
```

[Click Here for more](https://datakund-scraper.s3.amazonaws.com/datakund_DS3NEMP9REWJT0H_json.json)

### Run Scraper
```sh
from gome_scraper import *
link="https://prom.gome.com.cn/html/prodhtml/topics/201808/31/4889195497.html?intcmp=sy-1000060873-5"
data=run_gome_scraper(link)
```

### How it works?
* It takes URL of gome page with a search keyword to scrape the data.
* It generates the json data which contains the information of the gome search result.
* It gives the every detail present inside website in the form of json data.


### Examples
Below are some of the examples of URLs using which you can scrape:

* [Example 1](https://prom.gome.com.cn/html/prodhtml/topics/201709/18/7456103420.html?intcmp=sy-1000060873-1)

* [Example2](https://prom.gome.com.cn/html/prodhtml/topics/201808/31/4889195497.html?intcmp=sy-1000060873-5)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)









