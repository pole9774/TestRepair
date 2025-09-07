import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

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

# test case 4: Apps main interface

time.sleep(5)

# Click on the Apps tab - now at the top instead of bottom
el = driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Apps']")
el.click()
time.sleep(1)

# Now find and toggle the checkboxes in the RecyclerView
# In the new version, we need to find the app entries by their resource-id and index
# The structure is now different, using RecyclerView instead of ListView

# Toggle the first app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[0]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[0]
el.click()
time.sleep(1)

# Toggle the second app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[1]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[1]
el.click()
time.sleep(1)

# Toggle the third app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[2]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[2]
el.click()
time.sleep(1)

# Toggle the fourth app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[3]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[3]
el.click()
time.sleep(1)

# Toggle the fifth app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[4]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[4]
el.click()
time.sleep(1)

# Toggle the sixth app checkbox
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[5]
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[5]
el.click()
time.sleep(1)

# Toggle the seventh app checkbox if visible
try:
    el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[6]
    el.click()
    time.sleep(1)

    # Toggle it back
    el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/checkbox')[6]
    el.click()
    time.sleep(1)
except:
    pass  # If there are fewer visible apps, continue

# In the new version, the Show system apps switch is in a different location
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/switch_show_system_apps')
el.click()
time.sleep(1)

# Toggle it back
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/switch_show_system_apps')
el.click()
time.sleep(1)

driver.quit()
