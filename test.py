from scrapling import StealthyFetcher


def search(query):
    url = "https://www.google.com/search?"
    q_key = query
    default_key = "&sourceid=chrome&ie=UTF-8"
    page = StealthyFetcher().fetch(url=f"{url}q={q_key}{default_key}")
    # page.find_all('div', id="center_col")
    page.css('div#center_col')
    return page

file_path = 'test.html'

s_page = search('python')

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(str(s_page))

