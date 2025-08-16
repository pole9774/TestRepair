import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "hko.MyObservatory_v1_0",
    "appActivity": "hko.homepage.Homepage2Activity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(30)

try:
    el1 = driver.find_elements(AppiumBy.ID, 'hko.MyObservatory_v1_0:id/weather_icon_1')[0]
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("9-Day Forecast")')
    el2.click()

finally:
    time.sleep(5)
    driver.quit()
