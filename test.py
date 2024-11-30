import re
import requests
import json
from scrapling import StealthyFetcher
from bs4 import BeautifulSoup

def search(query):
    url = "https://www.google.com/search?"
    q_key = query
    default_key = "&sourceid=chrome&ie=UTF-8"
    page = StealthyFetcher().fetch(url=f"{url}q={q_key}{default_key}")
    # return page.css('div#center_col')
    return page

# def extract_links(s_page):
#     soup = BeautifulSoup(str(s_page), 'html.parser')
#     links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith(('https://', 'http://'))]
#     return links

# def filter_links(links, pattern):
#     filtered_links = [link for link in links if re.match(pattern, link) and 'google' not in link]
#     return filtered_links


# file_path = 'test.txt'
# pattern = r"https?://[a-zA-Z0-9./]+"

# s_page = search('python')

# urls = extract_links(s_page)
# links = filter_links(urls, pattern)
# print(links)

# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(str(urls))

# def extract_links(url):
#     # 發送 GET 請求到指定頁面
#     response = requests.get(url)
#     response.raise_for_status()  # 確保請求成功
    
#     # 解析 HTML 內容
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # 過濾條件（排除包含 google、youtube，或是圖片檔案的網址）
#     excluded_keywords = ['google', 'youtube']
#     excluded_extensions = ['.jpg', '.png', '.gif', '.svg', '.jpeg']
    
#     links = []
    
#     # 從所有 <a> 標籤中提取 href 屬性
#     for a_tag in soup.find_all('a', href=True):
#         href = a_tag['href']
#         # 檢查網址是否包含排除的關鍵字或檔案副檔名
#         if not any(keyword in href for keyword in excluded_keywords) and \
#            not any(href.lower().endswith(ext) for ext in excluded_extensions):
#             links.append(href)
    
#     return links

# # 測試函式
# if __name__ == "__main__":
#     # 目標頁面 URL
#     target_url = search('python')
    
#     try:
#         result_links = extract_links(target_url)
#         print("提取的網址：")
#         for link in result_links:
#             print(link)
#     except Exception as e:
#         print(f"發生錯誤：{e}")


def webpage2text(keywords):
    # 將網頁內容轉換為文字
    results = search(keywords)
    webpage_text_list = []
    for i in range(min(3, len(results.get("items", [])))):
        try:
            url = results["items"][i]["link"]
            response = requests.get(url)
            response.encoding = "utf-8"
            
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 移除 script 和 style 等不需要的標籤
            for script in soup(["script", "style"]):
                script.decompose()
            
            # 取得乾淨的文字內容，並去掉多餘空白
            webpage_text = soup.get_text(separator="\n").strip()
            webpage_text_list.append(webpage_text)
            
        except Exception as e:
            pass
            # print(f"處理網頁 {url} 時發生錯誤: {e}")
    return webpage_text_list
