# Mission-to-Mars


## Overview
The goal of this project was to learn and utilizing web scraping methods to extract information from the NASA Science Mars Exploration website using Chrome Developer tools to identify HTML components, Beautiful Soup/Splinter to automate a web browser and perform the scrape, MongoDB to store the data, and finally Flask to create a web application to display the data. Through the process, the goal was to develop an appt to scrape the following information about the planet Mars:
 -  Latest News
 -  Features Images
 -  Facts in a table about the planet 
 -  Images of the hemispheres

### Deliverable 1: 

We created the file "Mission_to_Mars_Challenge.ipynb" in Jupyter notebook to perform the scraping activity and pull the requested information needed to build the app. Some of the code used include:

- Visiting the URL url = 'https://mars.nasa.gov/news/', browser.visit(url)
- Using Splinter and BeautifulSoup to automate the browser and parse the HTML element to obtain the latest news title news_soup = soup(html,'html.parser'), slide_elem.find("div",class_='content_title'), news_title = slide_elem.find("div", class_='content_title').get_text()

![deliverable1](https://github.com/Jflux05/Mission-to-Mars/blob/a40ac0ff3768ef2c817e8d058eb9c8132df9f214/Resources/Images/deliverable1.png)


### Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
For this deliverable we exported our Jupyter notebook file into a Python script. Using this script as the starting point, we started to define the scraping process using Visual Studio Code to edit our Python script. We added functions to scrape through the website(s) and loop through the HTML tags to return the information used to create a database to be stored in MongoDB.

![Deliverable2_scraping](https://github.com/Jflux05/Mission-to-Mars/blob/a40ac0ff3768ef2c817e8d058eb9c8132df9f214/Resources/Images/deliverable2_scrapping.png)

Using the database in Mongo, we create a Flask app to connect to the information and create our app routes. These routes help to display the information on the home page and will perform the scraping of new data using the codes that we wrote in the Python script.

After, Mongo was integrated into the web app so that the data stored is updated every time the script, "Scraping.py" is run.

Then, an HTML template was created to customize the the web app and use Bootstrap components to enhance the HTML and CSS the file.

Finally, the HTML file was modified to loop through the dictionary and pull the titles and images for the hemispheres of Mars.
![deliverable2_hemis](https://github.com/Jflux05/Mission-to-Mars/blob/a40ac0ff3768ef2c817e8d058eb9c8132df9f214/Resources/Images/deliverable2_hemis.png)

### Deliverable 3: Add in the Bootstrap 3 Components
For the final deliverable, the following changes were made to the Bootstrap components to customize the view of the page:

(1) Updated the color of the Jumbotron header by adding gradient color shading and changing the color of the scrape button.

- Tag before challeneg: <div class_"jumbotron text-center"> & <a class="btn btn-primary btn-lg">
 
- updated tag <div style="background:linear-gradient(to bottom, #ffcccc 15%, #e9967a 85%)!important" class="jumbotron text-center"> & <a class="btn btn-default btn-lg">
 
(2) Modified the orientation of the hemisphere images to a single ribbon by changing the grid from col-md-6 to col-md-3.
 
 
(3) Updated the background color of the entire webpage by modifying the <body> tag with <body style="background-color:darksalmon; color:black">.


