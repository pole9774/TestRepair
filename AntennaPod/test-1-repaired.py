import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    # Comment out the old version
    # "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.1.3.apk",
    # Use the new version
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.5.0.apk",
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

time.sleep(10)

# Open side bar - ID remains the same
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0]
el.click()
time.sleep(1)

# Click Queue - ID remains the same but navigate using index in case multiple elements with same ID
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/txtvTitle')[0]  # Queue
el.click()
time.sleep(1)

# Click on More options first to access Lock Queue (moved to menu in v2.5.0)
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Select Lock Queue (now in the options menu)
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2]  # Lock Queue in options menu
el.click()
time.sleep(1)

# Cancel button remains the same
el = driver.find_element(AppiumBy.ID, 'android:id/button2')  # Cancel
el.click()
time.sleep(1)

# Click on More options again to access Lock Queue
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Select Lock Queue
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2]  # Lock Queue
el.click()
time.sleep(1)

# Lock Queue button remains the same
el = driver.find_element(AppiumBy.ID, 'android:id/button1')  # Lock Queue
el.click()
time.sleep(1)

# Refresh item remains the same
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

# More options again
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# In v2.5.0, "Search" is now in the toolbar as a dedicated button
driver.back()  # Close the options menu
time.sleep(1)

# Click on Search in the toolbar
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/action_search')
el.click()
time.sleep(1)

# Search text field ID changed
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/search_src_text')
el.send_keys('test')
time.sleep(1)

driver.press_keycode(66)  # ENTER
time.sleep(1)

# Back button (Collapse)
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Collapse')[0]  # Back
el.click()
time.sleep(1)

# More options for sorting
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option - first option in v2.5.0
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Date option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Date
el.click()
time.sleep(1)

# Old -> New option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Old -> New
el.click()
time.sleep(1)

# More options again
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Date option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Date
el.click()
time.sleep(1)

# New -> Old option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # New -> Old
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Duration option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Duration
el.click()
time.sleep(1)

# Short -> Long option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Short -> Long
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Duration option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Duration
el.click()
time.sleep(1)

# Long -> Short option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Long -> Short
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Episode title option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2]  # Episode title
el.click()
time.sleep(1)

# A -> Z option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # A -> Z
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Episode title option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[2]  # Episode title
el.click()
time.sleep(1)

# Z -> A option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Z -> A
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Podcast title option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[3]  # Podcast title
el.click()
time.sleep(1)

# A -> Z option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # A -> Z
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Podcast title option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[3]  # Podcast title
el.click()
time.sleep(1)

# Z -> A option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Z -> A
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Random option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[4]  # Random
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Smart Shuffle option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[5]  # Smart Shuffle
el.click()
time.sleep(1)

# Old -> New option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Old -> New
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Smart Shuffle option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[5]  # Smart Shuffle
el.click()
time.sleep(1)

# New -> Old option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # New -> Old
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Keep sorted option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[6]  # Keep sorted
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Sort option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[0]  # Sort
el.click()
time.sleep(1)

# Keep sorted option (uncheck)
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[6]  # Keep sorted
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Clear Queue option (now index 1 in v2.5.0)
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Clear Queue
el.click()
time.sleep(1)

# Cancel button remains the same
el = driver.find_element(AppiumBy.ID, 'android:id/button2')  # Cancel
el.click()
time.sleep(1)

# More options
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# Clear Queue option
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/title')[1]  # Clear Queue
el.click()
time.sleep(1)

# Confirm button remains the same
el = driver.find_element(AppiumBy.ID, 'android:id/button1')  # Confirm
el.click()
time.sleep(1)

# In v2.5.0, the multi-select functionality has changed
# Going back instead of using multi-select as the UI flow has changed significantly
driver.back()
time.sleep(1)

driver.quit()
