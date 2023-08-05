### Title

Instructure Scraper

### Descrption

* With instructure Scraper you can scrape search results and extract the contents produced by the search result.
* In instructure scraper it will scrape the data present of the website and give json data which contains the details of the contents on the website.
* It gives the every detail present inside website in the form of json data such as the text, links, menu links etc .

### JSON sample data
```sh
{
    "Scraper_Main_Australia": [
        {
            "canvas_link": "/en-au/canvas/k-12",
            "column_8": "K-12",
            "menu_item_expanded_accordion_parent_has_toggle": [
                {
                    "link": "/en-au/canvas/k-12/online-blended-learning",
                    "text": "\nSolutions by Need\n\n\nOnline & Blended Learning \n\n\nImprove Student Outcomes\n\n\nIntegrations with Other Tools\n\n\n"
                },
                {
                    "link": "/en-au/canvas/k-12/administrators",
                    "text": "\nSolutions by Role\n\n\nFor Administrators\n\n\nFor IT/Technologists\n\n\nFor Educators\n\n\nFor Students & Parents\n\n\n"
                }
            ]
        }
```

[Download full sample data](https://datakund-scraper.s3.amazonaws.com/datakund_GPWP5OU1Q7GE7ZU_json.json)

### Run Scraper
```sh
from instructure_scraper import *
link="https://www.instructure.com/en-au/product/canvas/k-12/studio"
data=run_instructure_scraper(link)
```

### How it works?
* It takes URL of instructure page with a search keyword to scrape the data.
* It generates the json data which contains the information of the instructure search result.


### Examples
Below are some of the examples of URLs using which you can scrape:

* [Example 1](https://www.instructure.com/en-au/product/canvas/k-12/studio)

* [Example2](https://www.instructure.com/en-au/product/canvas/k-12/lms)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)









