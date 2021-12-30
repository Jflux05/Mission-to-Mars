
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Assign the url and instruct the browser to visit it.
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

   # Add try/except for error handling
    try:
  
        slide_elem = news_soup.select_one('div.list_text')

        # ## Scrape Mars Data: The News
        slide_elem.find('div', class_='content_title')

        # In this line of code, we chained .find onto our previously assigned variable, slide_elem. 
        # When we do this, we're saying, "This variable holds a ton of information, so look inside 
        # of that information to find this specific data." The data we're looking for is the content title, 
        # which we've specified by saying, "The specific data is in a <div /> with a class of 'content_title'."

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # We've added something new to our .find() method here: .get_text(). 
         # When this new method is chained onto .find(), only the text of the element is returned.

        # Use the parent element to find the paragraph text 
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    return news_title, news_p


# ## Scrape Mars Data: Featured Image
# ### JPL Space Featured Images:

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

      # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
  
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# ## Scrape Mars Data: Mars Facts

def mars_facts():

    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

# Our data is live—if the table is updated, then we want that change to appear in Robin's app also.
# Pandas also has a way to easily convert our DataFrame back into HTML-ready code using the .to_html() function.

# Convert dataframe into HTML format, add bootstrap
    return df.to_html()


# ## MARS HEMISPHERES
def hemispheres(browser):

    # 1. Use browser to visit the URL 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # Parse the data
    hemi_html = browser.html
    hemi_soup = soup(hemi_html, 'html.parser')

    # Retrieve all items for hemispheres information
    items = hemi_soup.find_all('div', class_='item')

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []


    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    hemi_url = "https://astrogeology.usgs.gov/"

    for x in items:
        # create a dictionary to hold titles and urls for full resolution images
        hemi_dict = {}
        title = x.find('h3').text
    
        # create links for full resolution images
        link_url = x.find('a', class_='itemLink product-item')['href']
        browser.visit(hemi_url + link_url)
    
        # parse resulting html
        img_html = browser.html
        img_soup = soup(img_html, 'html.parser')
    
        # identify urls for full resolution images
        downloads = img_soup.find('div', class_='downloads')
        full_img_url = downloads.find('a')['href']
    
        # append dictionary
        hemi_dict['title'] = title
        hemi_dict['img_url'] = full_img_url
        hemisphere_image_urls.append(hemi_dict)
    
        # print values to check output
        print(title)
        print(full_img_url)
    
        browser.back()

    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
