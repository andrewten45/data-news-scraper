"""
This script is a scraper that scrapes information from the Google News API

Author: andrewten45
Date: 1/23/2023
"""

from pygooglenews import GoogleNews
import random

gn = GoogleNews(lang = 'en', country = 'US')

# Gets titles of news stories given search parameter
def get_titles(search):
    stories = []
    search = gn.search(search)
    newsitem = search['entries']

    for item in newsitem:
        story = {
            'title': item.title,
            'link': item.link
        }
        stories.append(story)

    return stories

# Enter in search term and call to the get_titles def
#print(get_titles('eCommerce'))

# TODO: Add a feature that gets the top news and outputs in a readable format
# Related: Practice outputting readable titles before other info
# So far this feature prints the top news but it remains in the default format.
top = gn.top_news(proxies=None, scraping_bee = None)
#print(top)

# WIP: Add a feature that picks a random story through search
def get_random_title(search):
    stories = []
    search = gn.search(search)
    newsitem = search['entries']

    for item in newsitem:
        story = {
            'title': item.title
        }
        stories.append(story)
    
    # Note: Enumeration appears to make the results more readable.
    # 
    #for index, value in enumerate(stories):
    #    print(index, value)

    random_index = random.randint(0, len(stories) - 1)
    random_title = stories[random_index]

    return random_title

print(get_random_title('Llamas'))


# TODO: Add a feature that counts up the most commonly used words in scraped titles