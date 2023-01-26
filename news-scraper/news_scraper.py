"""
This script is a scraper that scrapes information from the Google News API

Author: andrewten45
Date: 1/23/2023
"""

from pygooglenews import GoogleNews

gn = GoogleNews(lang = 'en', country = 'US')

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
print(get_titles('eCommerce'))

# TODO: Add a feature that gets the top news and outputs in a readable format
# So far this feature prints the top news but it remains in the default format.
top = gn.top_news(proxies=None, scraping_bee = None)
print(top)

# TODO: Add a feature that outputs readable titles before outputting other info