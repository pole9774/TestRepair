import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.clover.daysmatter",
    "appActivity": "com.clover.daysmatter.ui.activity.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(10)

try:
    el = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')[2] # bottom bar Date Calculator
    el.click()

finally:
    time.sleep(5)
    driver.quit()
