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


# test case 5: Side bar, statistics

time.sleep(2)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Open side bar button
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Statistics")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_time_chooser")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[1] # 1 year
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_time_chooser")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[2] # deck life
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ID, "com.ichi2.anki:id/action_time_chooser")
el.click()

time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "com.ichi2.anki:id/title")[0] # 1 month
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FORECAST")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("REVIEW COUNT")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("REVIEW TIME")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("INTERVALS")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("HOURLY BREAKDOWN")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("WEEKLY BREAKDOWN")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ANSWER BUTTONS")')
el.click()

time.sleep(2)

el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CARD TYPES")')
el.click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.quit()
