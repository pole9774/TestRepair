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


# test case 4: Side bar, card browser

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Open side bar button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Card browser")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_add_card_from_card_browser")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_search")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Collapse") # Back button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[0] # Change display order
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[1] # No sorting (faster)
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[1] # Filter marked
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[2] # Filter suspended
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[3] # Filter by tag
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/buttonDefaultNegative") # Cancel button
el.click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.quit()
