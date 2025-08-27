from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # This runs once before the ENTIRE test suite
    print("=== Starting Behave Test Suite ===")

def before_scenario(context, scenario):
    # This runs before each scenario
    print(f"--- Starting scenario: {scenario.name} ---")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # This runs after each scenario
    print(f"--- Finished scenario: {scenario.name} ---")
    if context.driver:
        context.driver.quit()

def after_all(context):
    # This runs once after the ENTIRE test suite
    print("=== Finished Behave Test Suite ===")
