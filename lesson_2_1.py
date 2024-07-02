from selenium import webdriver


def test_simple():
    wb = webdriver.Chrome()
    wb.get('https://www.mvideo.ru/')
    wb.quit()
