import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "me.tsukanov.counter",
    "appActivity": "me.tsukanov.counter.ui.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/menu_edit')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/menu_edit')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/edit_name')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/edit_name')
    el.send_keys("Test")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/edit_value')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/edit_value')
    el.send_keys("42")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Apply
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/menu_reset')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/menu_reset')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Reset
    el.click()
    
finally:
    time.sleep(5)
    driver.quit()
