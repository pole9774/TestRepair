import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "cn.ticktick.task",
    "appActivity": "com.ticktick.task.activity.MeTaskActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

# start from the Template (settings) page, enable template
try:
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Daily record")')
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el2.click()
    time.sleep(3)

    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')
    el3.click()

finally:
    time.sleep(5)
    driver.quit()
