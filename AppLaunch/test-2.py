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
    driver.find_element("accessibility id", "More options").click()
    time.sleep(3)

    driver.find_element("-android uiautomator", 'new UiSelector().text("Settings")').click()
    time.sleep(3)

    driver.find_element("id", 'com.simplemobiletools.applauncher:id/settings_customize_colors_label').click()
    time.sleep(3)

    driver.find_element("id", 'com.simplemobiletools.applauncher:id/customization_primary_color_label').click()
    
finally:
    time.sleep(10)
    driver.quit()
