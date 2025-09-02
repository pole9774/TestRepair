import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",  # Updated to v2
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

# "More options" button (unchanged: still an ImageView with content-desc)
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

# "Manage note types" option (unchanged: still a ListView with TextView text)
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Manage note types")')
el.click()

time.sleep(2)

# "Add note type" button: resource-id ("com.ichi2.anki:id/action_add_new_note_type") still correct, but now inside androidx.appcompat.widget.LinearLayoutCompat
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_add_new_note_type")
el.click()

time.sleep(2)

# Open dropdown: resource-id and class unchanged ("com.ichi2.anki:id/dropdown_deck_name", class CheckedTextView inside Spinner)
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/dropdown_deck_name")
el.click()

time.sleep(2)

# Select from dropdown: now the CheckedTextView text in v2 is "Add: Basic" (same as v1, but make sure we select the correct one)
dropdown_items = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/dropdown_deck_name")
for item in dropdown_items:
    if item.text == "Add: Basic":
        item.click()
        break

time.sleep(2)

# Ok button: resource-id changed in v2 to "com.ichi2.anki:id/md_buttonDefaultPositive"
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive")
el.click()

time.sleep(2)

# EditText: resource-id is not present, so use class name "android.widget.EditText"
el = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
el.clear()

time.sleep(2)

el = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
el.send_keys("Basic (Test)")

time.sleep(2)

# Ok button to confirm new note type name: resource-id is "com.ichi2.anki:id/md_buttonDefaultPositive"
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultPositive")
el.click()

time.sleep(2)

# Back button: content-desc is still "Navigate up"
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
el.click()

time.sleep(2)

driver.quit()
