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

try:
    driver.find_element("xpath", "//android.widget.ImageView[@content-desc='More options']").click()
finally:
    driver.quit()
