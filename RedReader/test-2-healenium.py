import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.quantumbadger.redreader",
    "appActivity": "org.quantumbadger.redreader.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "RedReader_test-2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')[4] # Custom Location
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.ID, 'android:id/button2')[0] # Cancel
    el2.click()

finally:
    time.sleep(3)
    driver.quit()
