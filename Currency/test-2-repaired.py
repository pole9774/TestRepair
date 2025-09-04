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
    # Click on "More options" button first
    more_options = driver.find_element(AppiumBy.XPATH, 
        "//android.widget.ImageButton[@content-desc='More options']")
    more_options.click()
    time.sleep(1)
    
    # Click on "Settings" from the dropdown menu
    settings_option = driver.find_element(AppiumBy.XPATH, 
        "//android.widget.TextView[@text='Settings']")
    settings_option.click()
    time.sleep(3)

    # Find the About option in the Settings screen
    # Note: Using XPATH instead of class name and index for better reliability
    about_option = driver.find_element(AppiumBy.XPATH, 
        "//android.widget.TextView[@text='About']/../..")
    about_option.click()

finally:
    time.sleep(5)
    driver.quit()
