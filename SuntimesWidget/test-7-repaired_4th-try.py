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
    # Click More options button (same as before)
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)
    
    # Find and click the "Set Alarm" option in the menu
    # In v2, it's the third option in the menu
    el2 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Set Alarm']")
    el2.click()
    time.sleep(3)
    
    # The alarm dialog is now a tabbed interface
    # Simply click the Event tab to ensure it's selected
    event_tab = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Event']")
    event_tab.click()
    time.sleep(2)
    
    # Click on the alarm event spinner directly
    event_spinner = driver.find_element(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/appwidget_schedalarm_mode")
    event_spinner.click()
    time.sleep(2)
    
    # Select "solar noon" from the dropdown
    solar_noon_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='solar noon']")
    solar_noon_option.click()
    time.sleep(2)
    
    # In v2, there's no direct Cancel button in the same place
    # Need to click the back button or touch outside to dismiss
    try:
        # First try to find and click the Cancel button if it exists
        cancel_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Cancel']")
        cancel_button.click()
    except:
        # If Cancel button not found, try to click outside the dialog
        try:
            touch_outside = driver.find_element(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/touch_outside")
            touch_outside.click()
        except:
            # If clicking outside doesn't work, press the back button
            driver.press_keycode(4)  # Android back button keycode
    
    time.sleep(2)

finally:
    time.sleep(3)
    driver.quit()
