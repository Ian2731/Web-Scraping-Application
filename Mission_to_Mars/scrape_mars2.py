from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

def hemispheres():
    executable_path = executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browserF = Browser("chrome", **executable_path)
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browserF.visit(mars_hemispheres_url)



    hemisphere = {}

    # Get a List of All the Hemispheres
    links = browserF.find_by_css("a.product-item h3")
    for item in range(len(links)):
        # Find Element on Each Loop to Avoid a Stale Element Exception
        browserF.find_by_css("a.product-item h3")[item].click()
    
        # Find Sample Image Anchor Tag & Extract <href>
        sample_element = browserF.find_link_by_text("Sample").first
        img_url = sample_element["href"]
    
        # Get Hemisphere Title
        title = browserF.find_by_css("h2.title").text
    
        # Append Hemisphere Object to List
        #hemisphere_image_urls.append(hemisphere)
        hemisphere[title] = img_url
        # Navigate Backwards
        browserF.back()
        
    return hemisphere
