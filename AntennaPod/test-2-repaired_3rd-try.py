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

# test case 2: Click Episodes in the sidebar

time.sleep(5)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0] # Open side bar
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'de.danoeh.antennapod:id/txtvTitle')[1] # Episodes
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/action_search')
el.click()
time.sleep(1)

# Exit search mode by clicking the back/collapse button
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Collapse')[0]
el.click()
time.sleep(1)

# Now we can access the refresh button in the toolbar
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

# Access the More options menu
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

# FIXED: After confirming, we're already on the main screen
# No need to look for "Collapse" button here - it doesn't exist at this point

# We can directly access the refresh button again
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

# Tab navigation remains the same
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
