from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@given('Click {help} on Amazon page')
def click_search_icon(context, help):
    context.driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Help']").click()


@given('Click Orders link on Amazon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@given('Click {hamburger} menu icon on the left')
def click_search_icon(context, hamburger):
    context.driver.find_element(By.XPATH, "//i[@class='hm-icon nav-sprite']").click()


@when('Input {text} into Amazon more solutions field')
def input_query(context, text):
    el = context.driver.find_element(By.ID, 'helpsearch')
    el.clear()
    el.send_keys(text)


@when('Click the Go button')
def click_search_icon(context):
    context.driver.find_element(By.CLASS_NAME, 'a-button-input').click()


@when('{text} text is present')
def verify_result_present(context, text):
    element = context.driver.find_element(By.ID, 'hmenu-content')
    assert text in element.text


@then('Click on the closing X of the menu')
def click_search_icon(context):
    context.driver.find_element(By.CLASS_NAME, 'hmenu-close-icon').click()
    sleep(2)


@then('Click on Try Prime from Amazon logo')
def click_search_icon(context):
    context.driver.find_element(By.CLASS_NAME, 'nav-prime-try').click()


@then('{text} text is present')
def verify_result_present(context, text):
    element = context.driver.find_element(By.TAG_NAME, 'body')
    assert text in element.text


@then('{text} button is present')
def verify_result_present(context, text):
    element = context.driver.find_element(By.ID, 'prime-header-CTA-announce')
    assert text in element.text


@then('Sign in page open')
def verify_signin_page_open(context):
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
