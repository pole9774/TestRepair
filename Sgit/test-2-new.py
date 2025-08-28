import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "me.sheimi.sgit",
    "appActivity": "me.sheimi.sgit.RepoListActivity",
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

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Git Profile")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Git Profile")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.sheimi.sgit:id/gitName')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.sheimi.sgit:id/gitName')
    el.send_keys("Test Name")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.sheimi.sgit:id/gitEmail')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'me.sheimi.sgit:id/gitEmail')
    el.send_keys("Test Email")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Done
    el.click()

finally:
    time.sleep(5)
    driver.quit()
