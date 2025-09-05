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
    # Open side bar - using the same approach as it still works
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0]
    el1.click()
    time.sleep(3)

    # Click settings button - updated resource ID
    el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/amc')
    el2.click()
    time.sleep(3)

    # Click on "Add Tasks in Wechat" - updated text
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Tasks in Wechat")')
    el3.click()

finally:
    time.sleep(5)
    driver.quit()
