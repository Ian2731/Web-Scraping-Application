Web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter

- Nasa Mars News
  - Scrape the NASA Mars News Site and collect the latest news title and paragraph text

- JPL Mars Space Images
  - Visited the url for JPL Featured Space Image
  - Use splinter to navigate the site and find the image url for the current Featured Mars Image

- Mars Weather
  - Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet
  
- Mars Hemispheres
  - Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres

MongoDB and Flask Application

- Using MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
