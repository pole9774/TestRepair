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

    # Find the About option that has "Version" in its description
    # This ensures we select the clickable About item, not the header
    about_option = driver.find_element(AppiumBy.XPATH, 
        "//android.widget.TextView[@text='About' and ../android.widget.TextView[contains(@text, 'Version')]]/ancestor::android.widget.LinearLayout[1]")
    about_option.click()

finally:
    time.sleep(5)
    driver.quit()
