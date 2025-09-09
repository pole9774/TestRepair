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
    # Click More options - this is the same in both versions
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)
    
    # In v2, "Set Alarm" is the 3rd option in the menu, not the 1st
    # The XML shows it's at index 2 in the ListView
    menu_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    set_alarm_option = menu_items[2]  # 3rd item (index 2)
    set_alarm_option.click()
    time.sleep(3)
    
    # The new version has tabs - make sure we're on the "Event" tab
    # Check if we need to click the Event tab (if we're on the Time tab)
    tabs = driver.find_elements(AppiumBy.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
    event_tab = tabs[0]  # First tab should be Event
    if 'selected="false"' in event_tab.get_attribute('outerHTML'):
        event_tab.click()
        time.sleep(1)
    
    # Click on the dropdown to select alarm type
    # In v2, the spinner has ID 'appwidget_schedalarm_mode'
    el3 = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_schedalarm_mode')
    el3.click()
    time.sleep(3)
    
    # Select "solar noon" from the dropdown
    # In v2, it's still the 3rd item in the list (index 2)
    el4 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.RelativeLayout')[2]
    el4.click()
    time.sleep(3)
    
    # Click Schedule/Accept
    # In v2, the schedule button is now an ImageButton with content-desc "Schedule"
    el5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Schedule')
    el5.click()

finally:
    time.sleep(3)
    driver.quit()
