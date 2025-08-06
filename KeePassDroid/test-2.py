import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Remember to delete files every time

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\KeePassDroid\\KeePassDroid v2.0.6.4.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\KeePassDroid\\KeePassDroid v2.2.0.9.apk",
    "appWaitActivity": "com.keepassdroid.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 2: Start page, about

time.sleep(5)

el = driver.find_element(AppiumBy.ID, "com.android.keepass:id/menu_about")
el.click()

time.sleep(1)

el = driver.find_element(AppiumBy.ID, "com.android.keepass:id/about_button")
el.click()

time.sleep(1)

driver.quit()
