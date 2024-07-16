import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)

    # wb = webdriver.Ie()

    request.addfinalizer(wb.quit)
    return wb


def test_check_all_sections(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    assert driver.find_element(By.XPATH, '//*[@class="notice success"]')
    driver.implicitly_wait(1)
    left_menu = driver.find_element(By.ID, 'box-apps-menu')
    all_apps = left_menu.find_elements(By.ID, 'app-')
    all_apps_texts = [app.text for app in all_apps]
    for app_text in all_apps_texts:
        app = driver.find_element(By.XPATH, f'//*[text()="{app_text}"]')
        app.click()
        child_docs = driver.find_elements(By.XPATH, "//*[@id='app-'][@class='selected']//li")
        child_docs_texts = [doc.text for doc in child_docs]
        for doc_text in child_docs_texts:
            doc = driver.find_element(By.XPATH, f'//*[text()="{doc_text}"]')
            doc.click()
            assert driver.find_element(By.XPATH, '//h1').text