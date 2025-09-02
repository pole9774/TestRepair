import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
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

time.sleep(5)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0] # Open side bar
el.click()
time.sleep(1)

# In v2.5.0, the sidebar uses RecyclerView instead of ListView, but element indexing still works similarly
el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/txtvTitle')[1] # Episodes
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/action_search')
el.click()
time.sleep(1)

# In v2.5.0, the More options menu structure has changed
# The refresh button is now directly accessible
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

# In v2.5.0, the More options menu directly shows "Remove all new flags" as the only option
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/title') # Remove all "new" flags
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Cancel
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'More options')[0]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/title') # Remove all "new" flags
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Confirm
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Collapse')[0] # Back
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

# Tab navigation - this remains similar
# In v2.5.0, the tabs are now LinearLayout elements with content-desc attributes
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'New')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'All')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Favorites')[0]
el.click()
time.sleep(1)

driver.quit()
