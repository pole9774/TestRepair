import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
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

# Open FAB menu on main page
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

# Press Add button (the index may need to be adjusted if the order changes in v2)
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[3]  # Add
el.click()

time.sleep(2)

# Select note type spinner (opens the model selection)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)

# Select "Basic" note type (index 0)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)

# Fill fields for Basic note
fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
fields[0].clear()
fields[0].send_keys("TestFront1")
fields[1].clear()
time.sleep(1)
fields[1].send_keys("TestBack1")
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add note type: Basic (and reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
fields[0].clear()
fields[0].send_keys("TestFront2")
fields[1].clear()
fields[1].send_keys("TestBack2")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add note type: Basic (optional reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[2]
el.click()
time.sleep(1)

fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
fields[0].clear()
fields[0].send_keys("TestFront3")
fields[1].clear()
fields[1].send_keys("TestBack3")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Add note type: Cloze
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[3]
el.click()
time.sleep(1)

fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
fields[0].clear()
fields[0].send_keys("{{c1::TestFront4}}")  # <-- cloze deletion markup required for Cloze type
fields[1].clear()
fields[1].send_keys("TestBack4")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# Back to main page
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
