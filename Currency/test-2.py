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
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Settings')
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')[10]
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
