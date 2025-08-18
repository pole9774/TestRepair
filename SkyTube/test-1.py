import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "free.rm.skytube.extra",
    "appActivity": "free.rm.skytube.gui.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(10)

try:
    # el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Feed")')
    # el1.click()
    # time.sleep(3)

    # # branch1
    # el0 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Most Popular")')
    # el0.click()
    # time.sleep(3)
    #
    # el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Feed")')
    # el1.click()
    # time.sleep(3)

    # branch2
    el0 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Bookmarks")')
    el0.click()
    time.sleep(3)
    
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Feed")')
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.ID, 'free.rm.skytube.extra:id/importSubscriptionsButton')[0]
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
