import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.quantumbadger.redreader",
    "appActivity": "org.quantumbadger.redreader.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.quantumbadger.redreader:id/title')[0] # Accounts
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, 'android:id/button3') # Close
    el.click()

finally:
    time.sleep(3)
    driver.quit()
