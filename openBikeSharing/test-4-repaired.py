import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# todo: Select a network in advance when entering, and you need to wait a little longer

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.0.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.10.0.apk",
    "appWaitActivity": "be.brunoparmentier.openbikesharing.app.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 4: More options - License

# Wait longer for the new UI with tabs to load
time.sleep(15)

# Click on "More options" (this element is still accessible the same way)
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

# In v1.10.0, "Settings" is now at index 1 instead of index 0
el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]  # Settings
el.click()
time.sleep(1)

# In v1.10.0, we need to click on "About" first (index 4 in the settings list)
# Note: The indices in Settings have changed
el = driver.find_elements(AppiumBy.ID, 'android:id/title')[4]  # About
el.click()
time.sleep(1)

# Now click on "License" within the About screen (index 4 in the about list)
el = driver.find_elements(AppiumBy.ID, 'android:id/title')[4]  # License
el.click()
time.sleep(1)

# The OK button is still accessible by the same ID
el = driver.find_element(AppiumBy.ID, 'android:id/button1')  # OK
el.click()
time.sleep(1)

# We need to navigate back twice now (once from License dialog, once from About screen)
driver.back()
time.sleep(1)
driver.back()
time.sleep(1)

driver.quit()
