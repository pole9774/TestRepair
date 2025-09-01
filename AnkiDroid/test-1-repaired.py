import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",  # Use v2 APK here!
    "appWaitActivity": "com.ichi2.anki.DeckPicker",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Main page, add button, create a deck, and add a card to the newly created deck

time.sleep(2)

# FAB button - unchanged resource-id and location in v2
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

# Add deck button - unchanged resource-id, but now content-desc is "Create deck" (can still use resource-id)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# Cancel button - resource-id changed to "com.ichi2.anki:id/md_buttonDefaultNegative"
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultNegative")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# EditText for deck name - unchanged; still first EditText on dialog
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.clear()
el.send_keys("Test")

# OK button - resource-id changed to "com.ichi2.anki:id/md_buttonDefaultPositive"
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive")
el.click()
time.sleep(1)

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_note_action")
el.click()
time.sleep(1)

# Deck selection - unchanged, still by android:id/text1, index 1 is "Test"
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]  # Deck
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]  # Test (second in the list)
el.click()
time.sleep(1)

# EditText for note fields - unchanged resource-id and structure
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]  # Front
el.clear()
el.send_keys("TestFront")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]  # Back
el.clear()
el.send_keys("TestBack")

# Save button - unchanged resource-id
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Back button - unchanged, still first android.widget.ImageButton
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
