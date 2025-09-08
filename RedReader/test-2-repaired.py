import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.quantumbadger.redreader",
    "appActivity": "org.quantumbadger.redreader.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Find the Custom Location icon by its content description
    custom_location_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Custom Location")
    custom_location_icon.click()
    time.sleep(3)
    
    # The Cancel button can still be found by its resource-id
    cancel_button = driver.find_element(AppiumBy.ID, 'android:id/button2')
    cancel_button.click()

finally:
    time.sleep(3)
    driver.quit()
