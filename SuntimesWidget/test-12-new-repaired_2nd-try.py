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
    
    # Improved approach to dismiss the bottom sheet dialog in v2
    try:
        # First try clicking the touch_outside element if it exists
        el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/touch_outside')
        el.click()
        time.sleep(2)  # Wait a bit longer to ensure the dismissal completes
    except Exception as e:
        print(f"Could not click touch_outside: {e}")
        try:
            # Try clicking at the top of the screen outside the dialog
            # This simulates tapping outside the bottom sheet
            screen_size = driver.get_window_size()
            driver.tap([(screen_size['width'] // 2, 100)], 500)
            time.sleep(2)
        except Exception as e:
            print(f"Could not perform tap: {e}")
            # If all else fails, use back button as in the original test
            driver.back()
            time.sleep(1)

finally:
    time.sleep(3)
    driver.quit()
