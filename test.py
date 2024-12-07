from scrapling import *
import re


def search(query):
    url = "https://www.google.com/search?"
    q_key = query
    default_key = "&sourceid=chrome&ie=UTF-8"
    page = StealthyFetcher().fetch(url=f"{url}q={q_key}{default_key}")
    # return page.find_all('div', id_="search")
    return str(page)

r_p = search("python")

# search_results = r_p.find_all('div', id_="search")
urls = [a['href'] for result in r_p for a in r_p.find_all('a', href=True)]


print(urls)
