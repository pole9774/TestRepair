import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    # Update the APK path to the new version if needed
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

# FAB button resource-id and index should be consistent in v2
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

# In v2, the add-note button is index 5 in FAB menu and has resource-id "add_note_action"
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/add_note_action")[0]
el.click()

time.sleep(2)

# Select note type: spinner resource-id and layout appears unchanged
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/note_type_spinner")
el.click()
time.sleep(1)

# Select "Basic" type (index 0 in v2 as in v1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)

# Fill "Front" field (EditText resource-id unchanged)
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()
el.send_keys("TestFront1")

# Fill "Back" field
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()
time.sleep(1)
el.send_keys("TestBack1")
time.sleep(1)

# Save button resource-id unchanged
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add another card, select type spinner again
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/note_type_spinner")
el.click()
time.sleep(1)

# Select "Basic (and reversed card)" type (index 1 in v2)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

# Fill fields
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()
el.send_keys("TestFront2")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()
el.send_keys("TestBack2")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add another card, select type spinner again
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/note_type_spinner")
el.click()
time.sleep(1)

# Select "Basic (optional reversed card)" type (index 2 in v2)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[2]
el.click()
time.sleep(1)

# Fill fields
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()
el.send_keys("TestFront3")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()
el.send_keys("TestBack3")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add another card, select type spinner again
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/note_type_spinner")
el.click()
time.sleep(1)

# Select "Cloze" type (index 3 in v2)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[3]
el.click()
time.sleep(1)

# Fill fields ("Text" and "Extra" - index 0 and 1)
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()
el.send_keys("TestFront4")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()
el.send_keys("TestBack4")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Back button: in v2, the top-left back button is still index 0 in toolbar
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
