from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given("I am on the login page")
def step_impl(context):
    # Start a new browser for each scenario
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when('I log in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").clear()
    context.driver.find_element(By.ID, "user-name").send_keys(username)

    context.driver.find_element(By.ID, "password").clear()
    context.driver.find_element(By.ID, "password").send_keys(password)

    context.driver.find_element(By.ID, "login-button").click()

@then("I should be redirected to the inventory page")
def step_impl(context):
    assert "/inventory.html" in context.driver.current_url
    context.driver.quit()

@then("I should see an error message")
def step_impl(context):
    error = context.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    ass
