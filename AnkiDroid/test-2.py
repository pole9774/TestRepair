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


# test case 2: Main page, add button to get shared deck

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/fab_expand_menu_button")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[2] # Get shared decks
el.click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.quit()
