import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "ryey.easer",
    "appActivity": "ryey.easer.core.ui.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start")')
    el2.click()
    time.sleep(3)

    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el3.click()
    time.sleep(3)

    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Stop")')
    el4.click()
    time.sleep(3)

    el5 = driver.find_element(AppiumBy.ID, 'ryey.easer:id/fab')
    el5.click()

finally:
    time.sleep(5)
    driver.quit()
