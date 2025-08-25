import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.1.3.apk",
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

# test case 5: Click Settings in the sidebar

time.sleep(5)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0] # Open side bar
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/nav_settings') # Settings
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/search') # Open search
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/search')[1]
el.clear()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/search')[1]
el.send_keys("Test")
time.sleep(1)

driver.press_keycode(66) # ENTER
time.sleep(1)

driver.back()
time.sleep(1)
driver.back() # back to Settings screen

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[0] # User Interface
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1] # Playback
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[2] # Network
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[3] # Synchronization
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[4] # Storage
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[5] # Notifications
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[6] # Statistics
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

driver.quit()
