import time
from appium.options.android import UiAutomator2Options
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.a5corp.weather",
    "appActivity": "com.a5corp.weather.activity.WeatherActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(10)

try:
    # Updated: Click the FAB for search (v2)
    driver.find_element("id", "com.a5corp.weather:id/fab").click()

finally:
    time.sleep(5)
    driver.quit()
