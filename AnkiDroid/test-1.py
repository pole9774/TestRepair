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


# test case1: Main page, add a button, create a deck, and add a card to the newly created deck

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/buttonDefaultNegative")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_deck_action")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.clear()

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.send_keys("Test")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/buttonDefaultPositive")
el.click()
time.sleep(1)

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/add_note_action")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[0]
el.send_keys("TestFront")

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.clear()

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/id_note_editText")[1]
el.send_keys("TestBack")

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_save")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

driver.quit()
