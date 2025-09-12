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


# test case 3: Main page, add button, add card, add card by different types

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[3] # Add
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0] # Type
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0] # Basic
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.send_keys("TestFront1")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.clear()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.send_keys("TestBack1")
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0] # Type
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1] # Basic (and reverse)
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.send_keys("TestFront2")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.send_keys("TestBack2")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0] # Type
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[2] # Basic (optional reversed card)
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Front
el.send_keys("TestFront3")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Back
el.send_keys("TestBack3")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0] # Type
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[3] # Cloze
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Text
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0] # Text
el.send_keys("TestFront4")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Extra
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1] # Extra
el.send_keys("TestBack4")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()

time.sleep(1)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0] # back button
el.click()
time.sleep(1)

driver.quit()
