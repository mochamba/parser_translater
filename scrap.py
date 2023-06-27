import time

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup


url = 'https://cheesemaking.com/collections/recipes'
base_url = 'https://cheesemaking.com'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
        }


def get_articles():
    """Save pages with recipes into txt """
    browser = Chrome('/chromedriver')
    browser.get(url)
    for i in range(3):
        button = browser.find_element(
            'xpath', '//*[@id="bc-sf-filter-load-more-button-container"]/a'
            )
        button.click()
        time.sleep(5)

    soup = BeautifulSoup(browser.page_source, 'lxml')
    article_list = []
    articles = soup.find_all(class_='collection__item')
    articles = articles[0: -4]
    for article in articles:
        article_href = base_url + article.get('href') + '\n'
        article_list.append(article_href)
    with open('articles.txt', 'w', encoding='utf-8') as file:
        file.writelines(article_list)


def translater():
    """Translation of articles into russian"""
    pass


if __name__ == '__main__':
    get_articles()
