import time
from appium.options.android import UiAutomator2Options
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.a5corp.weather",
    "appActivity": "com.a5corp.weather.activity.WeatherActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "SimpleWeather_test-3"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(10)

try:
    driver.find_element("accessibility id", "Open").click() # Open side bar
    time.sleep(3)

    driver.find_element("xpath", "//*[@text='Custom OpenWeatherMap Key']").click() # Healenium: UIAUTOMATOR selector changed to XPATH

finally:
    time.sleep(5)
    driver.quit()
