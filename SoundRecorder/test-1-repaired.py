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
    # Click on "More options" (same as in original test)
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)
    
    # Click on "Settings" instead of "Licenses" in v2
    el2 = driver.find_element(AppiumBy.ID, 'com.danielkim.soundrecorder:id/title')
    el2.click()
    time.sleep(3)
    
    # If you need to access specific settings features, you can add code here
    # For example, to interact with the "About" section visible in 3-Settings_v2.xml
    about_element = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]  # The "About" option
    about_element.click()
    
finally:
    time.sleep(5)
    driver.quit()
