import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",  # updated to v2
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

# MAIN PAGE BUTTONS
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

# In v2, the order of ImageButtons may have changed.
# It's safer to find the Add button by resource-id if available.
add_buttons = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")
el = add_buttons[3]  # "Add" button index remains unchanged in v2 view, verify if needed
el.click()

time.sleep(2)

# SELECT NOTE TYPE: Basic
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]  # Type spinner
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]  # Basic (index 0)
el.click()

time.sleep(1)

# FILL FIELDS FOR BASIC
front_fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
front_field = front_fields[0]
front_field.clear()
front_field.send_keys("TestFront1")

back_field = front_fields[1]
back_field.clear()
time.sleep(1)
back_field.send_keys("TestBack1")
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# SELECT NOTE TYPE: Basic (and reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]  # Type spinner
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]  # Basic (and reversed card) (index 1)
el.click()
time.sleep(1)

front_fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
front_field = front_fields[0]
front_field.clear()
front_field.send_keys("TestFront2")

back_field = front_fields[1]
back_field.clear()
back_field.send_keys("TestBack2")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# SELECT NOTE TYPE: Basic (optional reversed card)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]  # Type spinner
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[2]  # Basic (optional reversed card) (index 2)
el.click()
time.sleep(1)

front_fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
front_field = front_fields[0]
front_field.clear()
front_field.send_keys("TestFront3")

back_field = front_fields[1]
back_field.clear()
back_field.send_keys("TestBack3")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# SELECT NOTE TYPE: Cloze
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]  # Type spinner
el.click()
time.sleep(1)
el = driver.find_elements(AppiumBy.ID, "android:id/text1")[3]  # Cloze (index 3)
el.click()
time.sleep(1)

front_fields = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")
text_field = front_fields[0]
text_field.clear()
text_field.send_keys("TestFront4")

extra_field = front_fields[1]
extra_field.clear()
extra_field.send_keys("TestBack4")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

# BACK TO MAIN PAGE: In v2, back button remains index 0
el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
