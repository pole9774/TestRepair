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


# test case 3: Main page, add button, add card, add card by different types

time.sleep(2)

# Click on the FAB to expand menu (same ID, but now with content-desc="Add")
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

# Click on the Add button - now using content-desc instead of index
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add")
el.click()

time.sleep(2)

# Select Type - same as before
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()

time.sleep(1)

# Select Basic type - same as before
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()

time.sleep(1)

# Enter text in the Front field - now using content-desc
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.send_keys("TestFront1")

# Enter text in the Back field - now using content-desc
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.clear()
time.sleep(1)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.send_keys("TestBack1")
time.sleep(1)

# Save - ID remains the same
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()

time.sleep(1)

# Select Type again
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()

time.sleep(1)

# Select Basic (and reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

# Enter text in Front field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.send_keys("TestFront2")

# Enter text in Back field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.send_keys("TestBack2")

# Save the card
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Select Type again
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()

time.sleep(1)

# Select Basic (optional reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[2]
el.click()
time.sleep(1)

# Enter text in Front field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Front")
el.send_keys("TestFront3")

# Enter text in Back field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
el.send_keys("TestBack3")

# Save the card
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Select Type again
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()

time.sleep(1)

# Select Cloze
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[3]
el.click()
time.sleep(1)

# Enter text in the Text field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text")
el.send_keys("TestFront4")

# Enter text in the Extra field
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Extra")
el.clear()

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Extra")
el.send_keys("TestBack4")

# Save the card
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()

time.sleep(1)

# Go back to the main screen
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
el.click()
time.sleep(1)

driver.quit()
