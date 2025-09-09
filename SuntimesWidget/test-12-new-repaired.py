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
    # Click on "More options" button - same in both versions
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    # Click on "Solstice / Equinox" option - same text selector works in both versions
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Solstice / Equinox")')
    el.click()
    time.sleep(3)

    # Next year button - ID has changed in v2
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/info_time_nextbtn1')
    el.click()
    time.sleep(3)
    
    # Previous year button - ID has changed in v2
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/info_time_prevbtn1')
    el.click()
    time.sleep(3)
    
    # In v2, we need to click outside the bottom sheet to dismiss it
    # Using the touch_outside element
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/touch_outside')
    el.click()
    time.sleep(1)
    
    # Alternative approach if the above doesn't work:
    # Use back button as in the original test
    driver.back()

finally:
    time.sleep(3)
    driver.quit()
