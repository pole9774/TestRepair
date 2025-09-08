import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.github.yeriomin.dumbphoneassistant",
    "appActivity": "com.github.yeriomin.dumbphoneassistant.ManageContactsActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Changed to match the new text pattern with (0) suffix
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sim Card (0)")')
    el1.click()
    time.sleep(3)

    # This element still has the same accessibility ID
    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Copy contact to phone')
    el2.click()
    time.sleep(3)

    # Changed to match the new text pattern with (0) suffix
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone (0)")')
    el3.click()
    time.sleep(3)

    # This element still has the same accessibility ID
    el4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Copy contact to SIM')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
