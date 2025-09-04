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
    # Step 1: Open side bar - using a more specific and robust selector
    # In v2, the hamburger menu ImageButton is inside a ViewGroup with resource-id="cn.ticktick.task:id/auw"
    el1 = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="cn.ticktick.task:id/auw"]/android.widget.ImageButton')
    el1.click()
    time.sleep(3)

    # Step 2: Click settings button - using the updated ID and a more reliable find_element method
    # In v2, the settings button has resource-id="cn.ticktick.task:id/amc"
    el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/amc')
    el2.click()
    time.sleep(3)

    # Step 3: Click General - this selector still works for v2
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("General")')
    el3.click()
    time.sleep(3)

    # Step 4: Click Template - text has changed from "Template" to "Manage Template" in v2
    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Manage Template")')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
