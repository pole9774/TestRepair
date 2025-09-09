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
    
    # In v2, "Set Alarm" is now the third option in the menu
    el2 = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Set Alarm']")
    el2.click()
    time.sleep(3)
    
    # The alarm dialog is now a tabbed interface
    # Check if we're on the Event tab, if not, click it
    event_tab = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Event']")
    if not "selected=\"true\"" in driver.find_element(AppiumBy.XPATH, "//android.support.v7.app.ActionBar.Tab[1]").get_attribute("outerHTML"):
        event_tab.click()
        time.sleep(1)
    
    # Click on the alarm event spinner
    event_spinner = driver.find_element(AppiumBy.ID, "com.forrestguice.suntimeswidget:id/appwidget_schedalarm_mode")
    event_spinner.click()
    time.sleep(3)
    
    # Select "solar noon" from the dropdown
    solar_noon_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='solar noon']")
    solar_noon_option.click()
    time.sleep(3)
    
    # Click on Cancel button - now it's in a bottom sheet layout
    cancel_button = driver.find_element(AppiumBy.ID, "android:id/button2")
    if not cancel_button.is_displayed():
        # Try alternative method if not visible
        cancel_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Cancel']")
    cancel_button.click()

finally:
    time.sleep(3)
    driver.quit()
