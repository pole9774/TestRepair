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

# test case 6: more options

time.sleep(5)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[0] # Load default settings
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[4] # Show Notifications (index changed from 3 to 4)
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button2') # Abort
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[4] # Show Notifications (index changed from 3 to 4)
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Disable notifications
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[4] # Show Notifications (index changed from 3 to 4)
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[5] # About (index changed from 4 to 5)
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up') # Back button
el.click()
time.sleep(1)

driver.quit()
