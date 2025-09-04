import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.billthefarmer.currency",
    "appActivity": "org.billthefarmer.currency.Main",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Find and click the "More options" button first
    more_options_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    more_options_btn.click()
    
    # Wait for the menu to appear
    time.sleep(1)
    
    # Find and click the "Settings" option in the dropdown menu
    # Using xpath to find the element by its text since it doesn't have a unique accessibility ID
    settings_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
    settings_option.click()

finally:
    time.sleep(5)
    driver.quit()
