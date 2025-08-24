import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.1.3.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.5.0.apk",
    "appWaitActivity": "de.danoeh.antennapod.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# The sidebar will automatically open when you start the app for the first time, so before starting, open the app and close the sidebar.

# test case 1: Click queue in the sidebar

time.sleep(10)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0] # Open side bar
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/txtvTitle')[0] # Queue
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/queue_lock')
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/queue_lock')
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Lock Queue
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Search
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/search_src_text')
el.send_keys('test')
time.sleep(1)

driver.press_keycode(66) # ENTER
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Collapse')[0] # Back
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Date
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Old -> New
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Date
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # New -> Old
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Duration
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Short -> Long
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Duration
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Long -> Short
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2] # Episode title
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # A -> Z
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2] # Episode title
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Z -> A
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[3] # Podcast title
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # A -> Z
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[3] # Podcast title
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Z -> A
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[4] # Random
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[5] # Smart Shuffle
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Old -> New
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[5] # Smart Shuffle
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # New -> Old
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[6] # Keep sorted
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0] # Sort
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[5] # Keep sorted
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2] # Clear Queue
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2] # Clear Queue
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Confirm
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[3] # Multi select
el.click()
time.sleep(1)

driver.back()
time.sleep(1)

driver.quit()
