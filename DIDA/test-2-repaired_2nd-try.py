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
    # Open side bar - Using XPath to specifically target the hamburger menu button in the top left
    # This is more reliable than using CLASS_NAME which may select the wrong button
    el1 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.ViewGroup[@resource-id="cn.ticktick.task:id/auw"]/android.widget.ImageButton[1]')
    el1.click()
    time.sleep(3)

    # In v2, the settings button resource ID has changed and it's a TextView, not a Button
    # Old: cn.ticktick.task:id/settings_btn
    # New: cn.ticktick.task:id/amc
    el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/amc')
    el2.click()
    time.sleep(3)

    # This element can still be found by text
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sounds & Notifications")')
    el3.click()
    time.sleep(3)

    # The text has changed from "Daily Alert" to "Daily Notification" in v2
    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Daily Notification")')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
