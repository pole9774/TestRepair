import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.danielkim.soundrecorder",
    "appActivity": "com.danielkim.soundrecorder.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Saved Recordings")')
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Share File")')
    el.click()
    time.sleep(3)

    driver.back()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rename File")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rename File")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.danielkim.soundrecorder:id/new_name')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.danielkim.soundrecorder:id/new_name')
    el.send_keys("Test Recording Name")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # OK
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete File")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'com.danielkim.soundrecorder:id/file_name_text')[0] # Long click the first recording of the list
    driver.execute_script("mobile: longClickGesture", {
        "elementId": el.id,
        "duration": 5000
    })
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete File")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1') # OK
    el.click()
    time.sleep(3)

finally:
    time.sleep(5)
    driver.quit()
