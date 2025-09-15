import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\BookDash\\BookDash v2.8.0.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\BookDash\\BookDash v2.9.2.apk",
    "appPackage": "org.bookdash.android",
    "appActivity": "org.bookdash.android.presentation.splash.SplashActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "BookDash_test-1"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/action_language_choice')[0]
    el1.click()

finally:
    time.sleep(3)
    driver.quit()
