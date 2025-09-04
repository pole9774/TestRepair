import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "me.tsukanov.counter",
    "appActivity": "me.tsukanov.counter.ui.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Find and click on the navigation button - updated selector for v2
    # Use content-desc instead of resource-id that no longer exists
    el1 = driver.find_element(AppiumBy.XPATH, 
                             '//android.widget.ImageButton[@content-desc="Open navigation"]')
    el1.click()
    time.sleep(3)

    # This selector still works in v2 but we could also use resource-id approach
    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add counter")')
    # Alternative approach using resource-id:
    # el2 = driver.find_element(AppiumBy.ID, 'me.tsukanov.counter:id/add_counter')
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
