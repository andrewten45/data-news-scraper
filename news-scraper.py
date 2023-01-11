# Google News Scraper

# (Error): Getting errors with this.. couldn't get pip to install pygooglenews
# (Resolution): Wheel was missing and needed to be a specific version
# Feedparser needed to be updated

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