import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.6.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",
    "appWaitActivity": "com.ichi2.anki.DeckPicker",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)


# test case 6: Side bar, settings

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Open side bar button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("AnkiDroid")') # AnkiDroid - General settings
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Reviewing")') # Reviewing - Non-deck-specific reviewer settings
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Appearance")') # Appearance - Change themes and default font
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gestures")') # Gestures - Use taps and swipes instead of buttons
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Advanced")') # Advanced - Optimization and experimental features
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

driver.quit()
