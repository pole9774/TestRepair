import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    # Use the v2 APK for the new version
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

# test case 1: Main page, add button, create a deck, and add a card to the newly created deck

time.sleep(2)

# Press the FAB button to expand menu (unchanged)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

# Press the "Create deck" button (unchanged)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# Cancel button resource-id changed in v2
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultNegative") # Cancel button
el.click()
time.sleep(1)

# Reopen the menu to create a deck
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# Deck name input field (same resource-id)
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.clear()

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.send_keys("Test")

# OK button resource-id changed in v2
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive") # Ok button
el.click()
time.sleep(1)

time.sleep(2)

# Add a note to newly created deck
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_note_action")
el.click()
time.sleep(1)

# Select deck spinner opens; select "Test" deck (resource-id unchanged, but use the second item in the list)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1] # Deck
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1] # Test (second in the list)
el.click()
time.sleep(1)

# Edit note fields: resource-id unchanged, but content-desc changed in v2
# Fill Front field
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()
el.send_keys("TestFront")

# Fill Back field
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()
el.send_keys("TestBack")

# Save the note (resource-id unchanged)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Back button (unchanged)
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
