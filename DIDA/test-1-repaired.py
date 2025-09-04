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
    # Step 1: Open sidebar - This still works the same way in v2
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0]
    el1.click()
    time.sleep(3)

    # Step 2: Click on profile picture - Need to use the parent element which is clickable in v2
    # Option 1: Using the parent element's resource ID
    el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/adf')
    el2.click()
    # Option 2 (alternative): We could also locate by coordinates or by finding the image and its parent
    # el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/adc').find_element(AppiumBy.XPATH, '..')
    time.sleep(3)

    # Step 3: Click on 'My Achievement Score' - Better to use content-desc for reliability
    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Achievement Score')
    el3.click()

finally:
    time.sleep(5)
    driver.quit()
