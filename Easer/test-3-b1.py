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
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open navigation drawer') # Open side bar
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Profile")')
    el2.click()
    time.sleep(3)

    el3 = driver.find_elements(AppiumBy.ID, 'ryey.easer:id/fab')[0]
    el3.click()
    time.sleep(3)

    el5 = driver.find_elements(AppiumBy.ID, 'ryey.easer:id/button_add_operation')[0]
    el5.click()
    time.sleep(3)

    el6 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send SMS")')
    el6.click()

finally:
    time.sleep(5)
    driver.quit()
