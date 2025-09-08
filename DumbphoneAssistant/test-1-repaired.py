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
    # Updated selector to match the new tab text that includes count
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Sim Card")')
    el1.click()
    time.sleep(3)

    # This element's accessibility ID remains the same in v2
    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete contact from SIM')
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
