import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\SuperGenPass\\SuperGenPass v2.2.2.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\SuperGenPass\\SuperGenPass v3.0.0.apk",
    "appActivity": "info.staticfree.SuperGenPass.Super_Gen_Pass",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 2: More options, verify master password
# note: to be executed after test-1.py

time.sleep(5)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/title")[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[0]
el.send_keys("000000")

time.sleep(5)

driver.quit()
