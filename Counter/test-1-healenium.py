import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "me.tsukanov.counter",
    "appActivity": "me.tsukanov.counter.ui.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "Counter_test-1"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_element(AppiumBy.ID, 'android:id/up') # Side bar
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.XPATH, "//*[@text='Add counter']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
