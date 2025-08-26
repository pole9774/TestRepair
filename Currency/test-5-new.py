import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.billthefarmer.currency",
    "appActivity": "org.billthefarmer.currency.Main",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ID, 'org.billthefarmer.currency:id/edit')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'org.billthefarmer.currency:id/edit')
    el.clear()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'org.billthefarmer.currency:id/edit')
    el.send_keys("42.000")
    time.sleep(3)

    driver.execute_script("mobile: performEditorAction", {"action": "done"})

finally:
    time.sleep(5)
    driver.quit()
