import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)

    # wb = webdriver.Ie()

    request.addfinalizer(wb.quit)
    return wb


def parse_rgba(text: str) -> list:
    l_bracket = text.find('(')
    return [int(_) for _ in text[l_bracket + 1: -1].split(', ')]


def test_check_sorting_for_countries_and_zones(driver):
    driver.get('http://localhost/litecart/en/')

    # MP - main page
    mp_item = driver.find_element(By.XPATH, '//div[@id="box-campaigns"]//li')
    mp_item_name = mp_item.find_element(By.XPATH, './/div[@class="name"]').text

    mp_item_regular_price = mp_item.find_element(By.XPATH, './/*[@class="regular-price"]')
    mp_item_regular_price_text = mp_item_regular_price.text
    mp_item_regular_price_color = mp_item_regular_price.value_of_css_property('color')
    mp_item_regular_price_rgb = parse_rgba(mp_item_regular_price_color)[:3]
    assert mp_item_regular_price_rgb[0] == mp_item_regular_price_rgb[1] == mp_item_regular_price_rgb[2]
    mp_item_regular_price_line_through = mp_item_regular_price.value_of_css_property('text-decoration-line')
    assert mp_item_regular_price_line_through == 'line-through'

    mp_item_campaign_price = mp_item.find_element(By.XPATH, './/*[@class="campaign-price"]')
    mp_item_campaign_price_text = mp_item_campaign_price.text
    mp_item_campaign_price_color = mp_item_campaign_price.value_of_css_property('color')
    mp_item_campaign_price_rgb = parse_rgba(mp_item_campaign_price_color)[:3]
    assert mp_item_campaign_price_rgb[1] == mp_item_campaign_price_rgb[2] == 0
    mp_item_campaign_price_font_weight = mp_item_campaign_price.value_of_css_property('font-weight')
    assert int(mp_item_campaign_price_font_weight) >= 600

    mp_item_regular_price_font_size = float(mp_item_regular_price.value_of_css_property('font-size')[:-2])
    mp_item_campaign_price_font_size = float(mp_item_campaign_price.value_of_css_property('font-size')[:-2])
    assert mp_item_campaign_price_font_size > mp_item_regular_price_font_size

    link_to_pp = mp_item.find_element(By.XPATH, './a[@class="link"]')
    link_to_pp.click()

    # PP - product page
    pp_item = driver.find_element(By.XPATH, '//div[@id="box-product"]')
    pp_item_name = pp_item.find_element(By.XPATH, './/h1[@class="title"]').text

    pp_item_regular_price = pp_item.find_element(By.XPATH, './/*[@class="regular-price"]')
    pp_item_regular_price_text = pp_item_regular_price.text
    pp_item_regular_price_color = pp_item_regular_price.value_of_css_property('color')
    pp_item_regular_price_rgb = parse_rgba(pp_item_regular_price_color)[:3]
    assert pp_item_regular_price_rgb[0] == pp_item_regular_price_rgb[1] == pp_item_regular_price_rgb[2]
    pp_item_regular_price_line_through = pp_item_regular_price.value_of_css_property('text-decoration-line')
    assert pp_item_regular_price_line_through == 'line-through'

    pp_item_campaign_price = pp_item.find_element(By.XPATH, './/*[@class="campaign-price"]')
    pp_item_campaign_price_text = pp_item_campaign_price.text
    pp_item_campaign_price_color = pp_item_campaign_price.value_of_css_property('color')
    pp_item_campaign_price_rgb = parse_rgba(pp_item_campaign_price_color)[:3]
    assert pp_item_campaign_price_rgb[1] == pp_item_campaign_price_rgb[2] == 0
    pp_item_campaign_price_font_weight = pp_item_campaign_price.value_of_css_property('font-weight')
    assert int(pp_item_campaign_price_font_weight) >= 600

    pp_item_regular_price_font_size = float(pp_item_regular_price.value_of_css_property('font-size')[:-2])
    pp_item_campaign_price_font_size = float(pp_item_campaign_price.value_of_css_property('font-size')[:-2])
    assert pp_item_campaign_price_font_size > pp_item_regular_price_font_size

    assert mp_item_name == pp_item_name
    assert mp_item_regular_price_text == pp_item_regular_price_text
    assert mp_item_campaign_price_text == pp_item_campaign_price_text

