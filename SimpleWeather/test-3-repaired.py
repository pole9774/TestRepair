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
    # Open side bar - this step remains the same
    driver.find_element("accessibility id", "Open").click()
    time.sleep(3)
    
    # In v2, we need to click on "Settings" in the sidebar first
    driver.find_element("-android uiautomator", 'new UiSelector().text("Settings")').click()
    time.sleep(3)
    
    # Then find and click on "Custom OpenWeatherMap Key" in the Settings page
    driver.find_element("-android uiautomator", 'new UiSelector().text("Custom OpenWeatherMap Key")').click()

finally:
    time.sleep(5)
    driver.quit()
