@title[Cover Page]

# Reco<span class="gold">mend</span>

#### Creating a recommendator for Openrice users
<br>
<br>

<span class="byline">Lyoe Lee - Dec 2017</span>

---

@title[Outline]

#### Openrice <span class="gold">Recommendation</span> 
##### Goal: Try to recommend a restaurant to users

<br>

<span class="aside">Press down for more...</span>

+++

#### What to <span class="gray">Eat?</span>

<br>

#### Familiar with <span class="gold">Openrice?</span>
#### Familiar with <span class="gold">Netfilx?</span>

<br>

+++

Anybody who loves to <span class="gold">eat</span> (and <span class="gold">rate</span>)

---

@title[Summary - Part 1]

#### Goals?

<br>
- Predict the right restaurants to users |

<br>

<span class="aside">Not that easy....</span>


+++

#### Steps?

<br>

- Scrape top rated restuarants from Openrice |

+++?image=assets/pic/openrice_restaurant_search.png

<!-- ![Image-Absolute](assets/pic/openrice_restaurant_search.png) -->

+++

#### Steps?

<br>

- <span class="darkgray"> Scrape top rated restuarants from Openrice</span>
- Get each reviews and ratings |

+++?image=assets/pic/openrice_user_review.png

---
@title[Summary - Part 2 (Data)]

#### Data!
<br>

- Scrape all these data down |
- Before showing the data... |

---

@title[Summary - Part 3 (Challenges)]

#### Challenge 1...!?
<br>
- Learn [Scrapy](https://scrapy.org/)! |

+++

### Scrapy 101:<span class="gold"> Some Codes</span>

```python
class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('reviewresult.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class ExtractSpider(scrapy.Spider):
    name = "Extract"
    start_urls = review_urls

    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1}, # Used for pipeline 1
        'FEED_FORMAT':'json',                                 # Used for pipeline 2
        'FEED_URI': 'reviewresult.json'                        # Used for pipeline 2
    }
    
    def parse(self, response):
        for user in response.xpath('//*[@class="sr2-review-list-container full clearfix js-sr2-review-list-container"]'):
            yield {
                # https://stackoverflow.com/questions/20081024/scrapy-get-request-url-in-parse
                'link': response.url,
                'user': user.xpath('div[1]/section/div[1]/a/text()').extract(),
                'user_url' : user.xpath('div[1]/section/div[1]/a/@href').extract(),
                'rating': user.xpath('div[2]/section/div[1]/div[1]/div').extract(),
                'taste_star_1': user.xpath('div[3]/section/div[2]/div[2]/span[1]').extract(),
                'taste_star_2': user.xpath('div[3]/section/div[2]/div[2]/span[2]').extract(),
                'taste_star_3': user.xpath('div[3]/section/div[2]/div[2]/span[3]').extract(),
                'taste_star_4': user.xpath('div[3]/section/div[2]/div[2]/span[4]').extract(),
                'taste_star_5': user.xpath('div[3]/section/div[2]/div[2]/span[5]').extract(),
                'decor_star_1': user.xpath('div[3]/section/div[3]/div[2]/span[1]').extract(),               
                'decor_star_2': user.xpath('div[3]/section/div[3]/div[2]/span[2]').extract(),              
                'decor_star_3': user.xpath('div[3]/section/div[3]/div[2]/span[3]').extract(),               
                'decor_star_4': user.xpath('div[3]/section/div[3]/div[2]/span[4]').extract(),                
                'decor_star_5': user.xpath('div[3]/section/div[3]/div[2]/span[5]').extract(),                
                'service_star_1': user.xpath('div[3]/section/div[4]/div[2]/span[1]').extract(),                                
                'service_star_2': user.xpath('div[3]/section/div[4]/div[2]/span[2]').extract(),                                
                'service_star_3': user.xpath('div[3]/section/div[4]/div[2]/span[3]').extract(),                                
                'service_star_4': user.xpath('div[3]/section/div[4]/div[2]/span[4]').extract(),                                
                'service_star_5': user.xpath('div[3]/section/div[4]/div[2]/span[5]').extract(),                                                
                'hygiene_star_1': user.xpath('div[3]/section/div[5]/div[2]/span[1]').extract(),                                                
                'hygiene_star_2': user.xpath('div[3]/section/div[5]/div[2]/span[2]').extract(),                                                
                'hygiene_star_3': user.xpath('div[3]/section/div[5]/div[2]/span[3]').extract(),                                                
                'hygiene_star_4': user.xpath('div[3]/section/div[5]/div[2]/span[4]').extract(),                                                
                'hygiene_star_5': user.xpath('div[3]/section/div[5]/div[2]/span[5]').extract(),                                                
                'value_star_1': user.xpath('div[3]/section/div[6]/div[2]/span[1]').extract(),                                                                
                'value_star_2': user.xpath('div[3]/section/div[6]/div[2]/span[2]').extract(),                                                                
                'value_star_3': user.xpath('div[3]/section/div[6]/div[2]/span[3]').extract(),                                                                
                'value_star_4': user.xpath('div[3]/section/div[6]/div[2]/span[4]').extract(),                                                                
                'value_star_5': user.xpath('div[3]/section/div[6]/div[2]/span[5]').extract(),
            }
            
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
})

process.crawl(ExtractSpider)
process.start()

```
@[1-13](Define a class, saving in JSON)
@[14-24](Define a Extracting Spider, defining the URLs to scrape)
@[25-59](Defining the xpath/css to scrape and store in JSON)
@[60-65](Actual scraping of websites)

+++ 

#### Challenge 1...!?
<br>

- Learn [Scrapy](https://scrapy.org/)!
- Openrice limits...|
	- Only up to 17 pages per Region! | 
- Bad html consistency... |

---

@title[Step 2. Git-Commit]

### <span class="gold">STEP 2. GIT-COMMIT</span>
<br>

```shell
$ git add PITCHME.md
$ git commit -m "New slideshow content."
$ git push

Done!
```

@[1](Add your PITCHME.md slideshow content file.)
@[2](Commit PITCHME.md to your local repo.)
@[3](Push PITCHME.md to your public repo and you're done!)
@[5](Supports GitHub, GitLab, Bitbucket, GitBucket, Gitea, and Gogs.)

---

@title[Step 3. Done!]

### <span class="gold">STEP 3. GET THE WORD OUT!</span>
<br>
![GitPitch Slideshow URLs](assets/images/gp-slideshow-urls.png)
<br>
<br>
#### Instantly use your GitPitch slideshow URL to promote, pitch or present absolutely anything.

---

@title[Slide Rich]

### <span class="gold">Slide Rich</span>

#### Code Presenting for Blocks, Files, and GISTs
#### Image, Video, Chart, and Math Slides
#### Multiple Themes with Easy Customization
<br>
#### <span class="gold">Plus collaboration is built-in...</span>
#### Your Slideshow is Part of Your Project
#### Under Git Version Control within Your Git Repo

---

@title[Feature Rich]

### <span class="gold">Feature Rich</span>

#### Present Online or Offline
#### With Speaker Notes Support
#### Print Presentation as PDF
#### Auto-Generated Table-of-Contents
#### Share Presentation on Twitter or LinkedIn

---

### Go for it.
### Just add <span class="gold">PITCHME.md</span> ;)
<br>
[Click here to learn more @fa[external-link fa-pad-left]](https://github.com/gitpitch/gitpitch/wiki)