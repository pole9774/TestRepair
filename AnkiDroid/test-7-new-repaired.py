import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.6.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",
    "appWaitActivity": "com.ichi2.anki.DeckPicker",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)


# test case 7: more options, note types

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Manage note types")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_add_new_note_type")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/dropdown_deck_name")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/dropdown_deck_name")[0] # Add: Basic
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive") # Ok button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
el.clear()

time.sleep(2)

el = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
el.send_keys("Basic (Test)")

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive") # Ok button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # back button
el.click()

time.sleep(2)

driver.quit()
