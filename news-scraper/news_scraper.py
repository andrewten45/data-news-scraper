"""
This script is a scraper that scrapes information from the Google News API

Author: andrewten45
Date: 1/23/2023
"""

from pygooglenews import GoogleNews

gn = GoogleNews(country = 'United States')

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

# TODO: Add a unit test to ensure functionality. Redo file structure.
# Note that convention in python is 'snake_case' for file names
# Rename this file to news_scraper and move it to a new directory 'news-scraper'
# Create a new file 'test_news_scraper' within a new directory 'tests'
# Create __init__ files