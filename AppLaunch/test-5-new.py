import time
from appium.options.android import UiAutomator2Options
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.simplemobiletools.applauncher",
    "appActivity": "com.simplemobiletools.applauncher.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(10)

try:
    driver.find_element("id", "com.simplemobiletools.applauncher:id/fab").click()
    time.sleep(3)

    driver.find_element("id", "android:id/button2").click() # Cancel
    time.sleep(3)

    driver.find_element("id", "com.simplemobiletools.applauncher:id/fab").click()
    time.sleep(3)

    driver.find_element("id", "android:id/button1").click() # OK
    time.sleep(3)

finally:
    time.sleep(10)
    driver.quit()
