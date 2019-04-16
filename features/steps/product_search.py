from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Gojane page')
def open_gojane(context):
    context.driver.get('https://www.gojane.com/')
    sleep(2)
    context.driver.find_element(By.CLASS_NAME, 'fancybox-close').click()


@given('Open Youtube page')
def open_gojane(context):
    context.driver.get('https://www.youtube.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()


@when('Click on {menu_item} link')
def click_search_icon(context, menu_item):
    sleep(2)
    context.driver.find_element(By.LINK_TEXT, menu_item).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)


@then('Top navigation is {all_shoes}')
def verify_found_results_text(context, all_shoes):
    result_message = context.driver.find_element(By.CLASS_NAME, 'current').text
    assert all_shoes in result_message, "Expected word '{}' in message, but got '{}'".format(all_shoes, result_message)
