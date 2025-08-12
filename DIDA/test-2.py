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
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0] # open side bar
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.ID, 'cn.ticktick.task:id/settings_btn')[0] # settings button
    el2.click()
    time.sleep(3)

    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sounds & Notifications")')
    el3.click()
    time.sleep(3)

    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Daily Alert")')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
