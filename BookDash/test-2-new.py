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
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el1 = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/action_search_books')[0]
    el1.click()
    time.sleep(1)

    el2 = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/search_src_text')[0]
    el2.clear()
    time.sleep(1)

    el3 =  driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/search_src_text')[0]
    el3.send_keys("Test")
    time.sleep(1)

    driver.press_keycode(66) # ENTER
    time.sleep(1)

    el4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") # Back button
    el4.click()
    time.sleep(1)

finally:
    time.sleep(3)
    driver.quit()
