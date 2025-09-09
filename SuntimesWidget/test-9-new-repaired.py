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
    # Click on More options button
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    # Click on Set Time Zone option - second item in v2 menu
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Set Time Zone"]')
    el.click()
    time.sleep(3)

    # Click Cancel button - in v2 it's an ImageButton with content-desc "Cancel"
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    el.click()
    time.sleep(3)

    # Click on More options again
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    # Click on Set Time Zone again
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Set Time Zone"]')
    el.click()
    time.sleep(3)

    # Click on the Mode spinner - now in a different location
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_timezone_mode')
    el.click()
    time.sleep(3)

    # Select "Time Standard" mode (first option in v2) - replaces "Solar Time" in v1
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@text="Time Standard"]')
    el.click()
    time.sleep(3)

    # Click on the Time Standard spinner
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_solartime')
    el.click()
    time.sleep(3)

    # Select "Apparent Solar Time" (LTST)
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="LTST"]')
    el.click()
    time.sleep(3)

    # Click on the Time Standard spinner again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_solartime')
    el.click()
    time.sleep(3)

    # Select "Local Mean Time" (LMT)
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="LMT"]')
    el.click()
    time.sleep(3)

    # Click on Mode spinner again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_timezone_mode')
    el.click()
    time.sleep(3)

    # Select "System Time Zone"
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@text="System Time Zone"]')
    el.click()
    time.sleep(3)

    # Click on Mode spinner again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_timezone_mode')
    el.click()
    time.sleep(3)

    # Select "User Defined"
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@text="User Defined"]')
    el.click()
    time.sleep(3)

    # Click on Time Zone spinner in user defined section
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_timezone_custom')
    el.click()
    time.sleep(3)

    # Select first Time Zone in the list - America/Phoenix in the example
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')
    el.click()
    time.sleep(3)

    # Click the Set button - now an ImageButton with content-desc "Set"
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Set')
    el.click()

finally:
    time.sleep(3)
    driver.quit()
