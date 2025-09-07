import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# After installing, press and hold to start and then shut down

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.4.1.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.6.8.apk",
    "appWaitActivity": "org.jak_linux.dns66.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Action bar above, except more options

time.sleep(10)

# Click on refresh button - still exists in v2
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_refresh')
el.click()
time.sleep(1)

# Try to find and click restore button if it exists (for v1)
# Skip this step if it doesn't exist (for v2)
try:
    el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_restore')
    el.click()
    time.sleep(1)
except NoSuchElementException:
    print("Restore button not found in this version - skipping this step")

# Alternative: Click on more options and look for restore in the menu
# Uncomment if needed
"""
try:
    # Click on more options menu
    more_options = driver.find_element(AppiumBy.XPATH, 
        '//android.widget.ImageView[@content-desc="More options"]')
    more_options.click()
    time.sleep(1)
    
    # Look for restore option in the menu
    # Note: Would need the XML of the opened menu to properly implement this
except NoSuchElementException:
    print("More options or Restore option not found")
"""

driver.quit()
