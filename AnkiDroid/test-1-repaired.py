import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.6.apk",
    # "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",
    "appWaitActivity": "com.ichi2.anki.DeckPicker",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Main page, add button, create a deck, and add a card to the newly created deck (for v2 layout/resources)

time.sleep(2)

# 1. Press the "Add" FAB to expand menu
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

# 2. Tap "Create deck" action (ID and order unchanged)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# 3. Press "Cancel" on the dialog (button ID changed in v2)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultNegative")  # v2: Cancel button
el.click()
time.sleep(1)

# 4. Re-open "Create deck" dialog
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

# 5. Enter deck name ("Test"), then confirm (button ID changed in v2)
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.clear()
el.send_keys("Test")
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive")  # v2: Ok button
el.click()
time.sleep(1)

time.sleep(2)

# 6. Press the "Add" FAB again to expand menu
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

# 7. Tap "Add" note action (content-desc is now set, but ID is unchanged for add_note_action)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_note_action")
el.click()
time.sleep(1)

# 8. Open deck selection spinner (Deck:) (ID unchanged, but resource text "Default" is still the first, "Test" is second)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]  # Press spinner
el.click()
time.sleep(1)

# 9. Select "Test" deck from dialog (2nd option, same as before)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

# 10. Fill in Front and Back fields (EditTexts, now have content-desc "Front"/"Back" in v2)
front_field = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
front_field.clear()
front_field.send_keys("TestFront")

back_field = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
back_field.clear()
back_field.send_keys("TestBack")

# 11. Save the note (ID unchanged)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# 12. Press back button (first ImageButton, toolbar)
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
