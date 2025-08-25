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
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Turn on sounds")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Turn on sounds")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Turn on vibration")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Turn on vibration")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Use hardware buttons")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Use hardware buttons")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Keep screen on")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Keep screen on")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Remove all counters")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Remove all counters")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Remove all
    el.click()

finally:
    time.sleep(5)
    driver.quit()
