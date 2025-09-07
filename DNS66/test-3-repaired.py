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

# test case 3: Hosts main interface

time.sleep(15)

# Changed: Click on the Hosts tab in the top tab layout instead of bottom bar
el = driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Hosts']")
el.click()
time.sleep(1)

# Changed: Updated the switch element identification
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/host_enabled')
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/host_enabled')
el.click()
time.sleep(1)

# Changed: Updated to use the updated RecyclerView and item selection
el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_title')[1]  # Adaway hosts file in v2
el.click()
time.sleep(1)

# Changed: The title field structure is slightly different but ID remains same
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/title')
el.clear()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/title')
el.send_keys('test')
time.sleep(1)

# Save button retains same ID
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_save')
el.click()
time.sleep(5)

# Changed: FAB button ID changed
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/floating_action_button')
el.click()
time.sleep(1)

# Title field - interface similar but input slightly different
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/title')
el.clear()
el.send_keys('test')
time.sleep(1)

# Location field
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/location')
el.clear()
el.send_keys('test')
time.sleep(1)

# Action selector - unchanged
el = driver.find_element(AppiumBy.ID, 'android:id/text1')  # Action
el.click()
time.sleep(1)

# Options in dropdown unchanged
el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0]  # Deny
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/text1')  # Action
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1]  # Allow
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/text1')  # Action
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[2]  # Ignore
el.click()
time.sleep(1)

# Save button unchanged
el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_save')
el.click()
time.sleep(1)

driver.quit()
