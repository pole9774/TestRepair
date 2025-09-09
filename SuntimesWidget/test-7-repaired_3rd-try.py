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
    
    # In v2, "Set Alarm" is the third option in the menu
    el2 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Set Alarm']")
    el2.click()
    time.sleep(3)
    
    # The alarm dialog is now a tabbed interface
    # Make sure we're on the Event tab
    event_tab = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Event']")
    # If Event tab is not selected, click it
    tab_parent = event_tab.find_element(AppiumBy.XPATH, "./..")
    if "selected=\"true\"" not in driver.execute_script("return arguments[0].outerHTML;", tab_parent):
        event_tab.click()
        time.sleep(1)
    
    # Click on the alarm event spinner
    event_spinner = driver.find_element(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/appwidget_schedalarm_mode")
    event_spinner.click()
    time.sleep(2)
    
    # Select "solar noon" from the dropdown
    solar_noon_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='solar noon']")
    solar_noon_option.click()
    time.sleep(2)
    
    # In v2, there's no direct Cancel button - instead we need to:
    # Option 1: Click outside the dialog to dismiss it
    touch_outside = driver.find_element(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/touch_outside")
    touch_outside.click()
    time.sleep(1)
    
    # If clicking outside didn't work, try pressing the back button
    if driver.find_elements(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/appwidget_schedalarm_mode"):
        driver.press_keycode(4)  # Android back button keycode

finally:
    time.sleep(3)
    driver.quit()
