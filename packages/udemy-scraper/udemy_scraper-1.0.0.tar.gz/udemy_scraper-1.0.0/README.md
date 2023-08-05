### Title

udemy Scraper

### Descrption

* With udemy Scraper you can scrape search results and extract the contents produced by the search result.
* In udemy scraper it will scrape the data present of the website and give json data which contains the details of the contents on the website.

### JSON sample data
```sh
{
    "Scraper_lecture_min": [
        {
            "column_0": [
                {
                    "text": "Course Learning Contest00:16"
                },
                {
                    "text": "Course IntroductionPreview01:39"
                },
                {
                    "text": "Introduction to AWS NetworkingPreview19:11"
                },
                {
                    "text": "AWS Networking fundamentals7 questions"
                }
            ],
            "section_title": "Introduction",
            "text_section_hidden_on_mobile_content": "3 lectures \u2022 21min"
        }
```

[Click Here for more](https://datakund-scraper.s3.amazonaws.com/datakund_331XWFKJUGT0KYC_json.json)

### Run Scraper
```sh
from udemy_scraper import *
link="https://www.udemy.com/course/aws-certified-advanced-networking-specialty-ans/"
data=run_udemy_scraper(link)
```

### How it works?
* It takes URL of udemy page with a search keyword to scrape the data.
* It generates the json data which contains the information of the udemy search result.
* It gives the every detail present inside website in the form of json data.


### Examples
Below are some of the examples of URLs using which you can scrape:

* [Example 1](https://www.udemy.com/course/aws-certified-advanced-networking-specialty-ans/)

* [Example2](https://www.udemy.com/course/git-github-practical-guide/)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)









