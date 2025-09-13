import time
from appium.options.android import UiAutomator2Options
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.simplemobiletools.applauncher",
    "appActivity": "com.simplemobiletools.applauncher.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
    "sessionKey": "AppLauncher_test-4"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(10)

try:
    driver.find_element("accessibility id", "More options").click()
    time.sleep(3)

    driver.find_element("xpath", "//*[@text='Settings']").click() # Healenium: changed to XPATH
    time.sleep(3)

    driver.find_element("id", 'com.simplemobiletools.applauncher:id/settings_customize_colors_label').click()
    time.sleep(3)

    driver.find_element("xpath", "//*[@text='Theme']").click() # Healenium: changed to XPATH
    time.sleep(3)

    driver.find_element("xpath", "//*[@text='Dark theme']").click() # Healenium: changed to XPATH

finally:
    time.sleep(10)
    driver.quit()
