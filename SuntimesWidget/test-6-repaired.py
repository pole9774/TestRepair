import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.forrestguice.suntimeswidget",
    "appActivity": "com.forrestguice.suntimeswidget.SuntimesActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Click on "More options" (this remains the same)
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)

    # Click on "View date" instead of "Set Date"
    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("View date")')
    el2.click()
    time.sleep(3)

    # Click on the "Set" icon button using accessibility ID
    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Set')
    el3.click()

finally:
    time.sleep(3)
    driver.quit()
