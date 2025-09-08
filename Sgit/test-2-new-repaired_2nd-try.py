import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "me.sheimi.sgit",
    "appActivity": "me.sheimi.sgit.RepoListActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Open More options menu
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    # Click on Settings (instead of Git Profile in v1)
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
    el.click()
    time.sleep(3)

    # Click on User Name option
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("User Name")')
    el.click()
    time.sleep(3)

    # Clear and set user name in the dialog
    el = driver.find_element(AppiumBy.ID, 'android:id/edit')
    el.clear()
    time.sleep(2)
    el.send_keys("Test Name")
    time.sleep(2)

    # Click OK button to save name
    el = driver.find_element(AppiumBy.ID, 'android:id/button1')  # OK button
    el.click()
    time.sleep(3)

    # Click on User Email option
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("User Email")')
    el.click()
    time.sleep(3)

    # Clear and set email in the dialog
    el = driver.find_element(AppiumBy.ID, 'android:id/edit')
    el.clear()
    time.sleep(2)
    el.send_keys("Test Email")
    time.sleep(2)

    # Click OK button to save email
    el = driver.find_element(AppiumBy.ID, 'android:id/button1')  # OK button
    el.click()
    time.sleep(3)

    # Navigate back to main screen using the correct content description
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Settings, Navigate up')
    el.click()

finally:
    time.sleep(5)
    driver.quit()
