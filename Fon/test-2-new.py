import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.oakley.fon",
    "appActivity": "com.oakley.fon.AndroidWISPr",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username")')
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/button2") # Cancel
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username")')
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/edit")
    el.clear()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/edit")
    el.send_keys("Test")
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/button1") # OK
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password")')
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/button2") # Cancel
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password")')
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/edit")
    el.clear()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/edit")
    el.send_keys("Test")
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, "android:id/button1") # OK
    el.click()

finally:
    time.sleep(5)
    driver.quit()
