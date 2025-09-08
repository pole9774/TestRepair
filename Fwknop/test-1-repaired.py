import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.cipherdyne.fwknop2",
    "appActivity": "biz.incomsystems.fwknop2.ConfigListActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Click on "More options" in the main screen
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)

    # Click on "New config" option (note the lowercase 'c' in v2)
    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("New config")')
    el2.click()
    time.sleep(3)

    # Click on "More options" in the config detail screen
    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el3.click()
    time.sleep(3)

    # Click on "Save config" option
    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Save config")')
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
