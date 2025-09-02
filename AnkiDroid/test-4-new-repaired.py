import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AnkiDroid\\AnkiDroid v2.13.0.apk",  # updated to v2, no underscore
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

# -- Card browser navigation --
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Card browser")')
el.click()

time.sleep(2)

# -- Add note from card browser (resource name changed in v2) --
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_add_note_from_card_browser")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Back button
el.click()

time.sleep(2)

# -- Search icon (same in v2) --
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_search")
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Collapse") # Back button
el.click()

time.sleep(2)

# -- More options (same in v2) --
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

# The dialog layout is updated to use RecyclerView and different index mapping in v2.
# Change display order (index 0 "Change display order")
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/md_title")[0]
el.click()

time.sleep(2)

# No sorting (faster) (index 0 "No sorting (faster)")
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/md_title")[0]
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

# Filter marked (index 1 "Filter marked")
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/md_title")[1]
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

# Filter suspended (index 2 "Filter suspended")
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/md_title")[2]
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")
el.click()

time.sleep(2)

# Filter by tag (index 3 "Filter by tag")
el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/md_title")[3]
el.click()

time.sleep(2)

# Cancel button changed resource id in v2
el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/md_buttonDefaultNegative") # Cancel button
el.click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.quit()
