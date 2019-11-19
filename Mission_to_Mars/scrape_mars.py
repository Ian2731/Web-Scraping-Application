from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

browser = Browser("chrome", executable_path="/usr/local/bin/chromedriver", headless=True)


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# def scrape_info():
#     browser = init_browser()

def mars_title():
    browser = init_browser() 
    #browser = Browser("chrome", executable_path="/usr/local/bin/chromedriver", headless=True}
    
    # Visit visitcostarica.herokuapp.com
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)

    # Scrape page into Soup
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')

    #Pulling article title with text only
    slide_elem.find("div", class_='content_title').get_text()
    news_title = slide_elem.find("div", class_='content_title').get_text()

    #Pulling first paragraph of article with text only
    slide_elem.find("div", class_='article_teaser_body').get_text()
    news_paragraph = slide_elem.find("div", class_='article_teaser_body').get_text()

    browser.quit()

    return news_title, news_paragraph

# JPL SECTION
def image():
    executable_path = executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path)
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)

    full_image = browser.click_link_by_partial_text('FULL IMAGE')

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)

    more_info = browser.click_link_by_partial_text('more info')

    jpl_html = browser.html
    img_soup = BeautifulSoup(jpl_html, 'html.parser')

    img_url_rel = img_soup.select_one('.main_image').get("src")

    abs_img_url = f"https://www.jpl.nasa.gov/{img_url_rel}"

## TWITTER SECTION
def mars_weather(browser):
    executable_path = executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path)
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)

    twitter_html = browser.html
    twitter_news_soup = BeautifulSoup(twitter_html, 'html.parser')
    
    twitter_slide_elem = twitter_news_soup.select_one('ul.item_list li.slide')

    mars_weather = twitter_news_soup.find("div", class_="js-tweet-text-container").get_text()

## MARS FACTS
def mars_facts(browser):
    executable_path = executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browserF = Browser("chrome", **executable_path)
    mars_facts_url = 'https://space-facts.com/mars/'
    browserF.visit(mars_facts_url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)

    facts_html = browserF.html
    facts_news_soup = BeautifulSoup(facts_html, 'html.parser')

    mars_facts = facts_news_soup.find("table", class_="tablepress tablepress-id-p-mars")

    name_list = []
    for x in mars_facts.find_all("td", class_="column-1"):
        name_list.append(x.get_text())

    print(name_list)

    facts_list = []
    for x in mars_facts.find_all("td", class_="column-2"):
        facts_list.append(x.get_text())

    print(facts_list)

    total_facts = {
    "name": name_list,
    "data": facts_list
    }

    facts_dataframe = pd.DataFrame(total_facts)

    print(facts_dataframe.to_html())

## MARS HEMISPHERES
def hemispheres():
    executable_path = executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browserF = Browser("chrome", **executable_path)
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browserF.visit(mars_hemispheres_url)

    hemisphere_image_urls = []

    # create a list of the four hemispheres
    links = browserF.find_by_css("a.product-item h3")

    for item in range(len(links)):
        hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browserF.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browserF.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browserF.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browserF.back()

    print(hemisphere_image_urls)

    mars_dictionary = {
    "Mars Hemispheres": hemispheres
    }

    browser.quit()

    return mars_dictionary