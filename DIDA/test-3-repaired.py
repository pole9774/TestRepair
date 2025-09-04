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

try:
    # Step 1: Open side bar - remains the same as we're selecting by class and index
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0]
    el1.click()
    time.sleep(3)

    # Step 2: Click settings button - ID has changed from 'settings_btn' to 'amc'
    el2 = driver.find_elements(AppiumBy.ID, 'cn.ticktick.task:id/amc')[0]
    el2.click()
    time.sleep(3)

    # Step 3: Click General - text selector still works
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("General")')
    el3.click()
    time.sleep(3)

    # Step 4: Click Template - text has changed from "Template" to "Manage Template"
    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Manage Template")')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
