import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Wait longer for the newer version which has more content to load
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
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

# test case 5: More options - About

time.sleep(15)

# Click on "More options" - same in both versions
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

# Click on "Settings" - in v2 it's the second item (index 1) 
el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]  # Settings (second item now)
el.click()
time.sleep(1)

# Click on "About" - in v2 it's the fifth item (index 4)
el = driver.find_elements(AppiumBy.ID, 'android:id/title')[4]  # About (now at index 4)
el.click()
time.sleep(1)

# In v2, About is a full screen, not a dialog with an OK button
# Need to press back button to return to Settings
driver.press_keycode(4)  # Android back button
time.sleep(1)

driver.quit()
