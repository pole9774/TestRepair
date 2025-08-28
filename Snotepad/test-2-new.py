import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "info.aario.snotepad",
    "appActivity": "info.aario.snotepad.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/fab') # Create new note
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/etTitle') # Title
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/etTitle')
    el.send_keys("Test Title")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/etEditor') # Content
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/etEditor')
    el.send_keys("Test Content")
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/btUndo')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/btRedo')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'info.aario.snotepad:id/fab') # Save note
    el.click()

finally:
    time.sleep(5)
    driver.quit()
