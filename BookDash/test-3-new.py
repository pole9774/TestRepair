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
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/design_menu_item_text')[1] # Downloaded Books
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/design_menu_item_text')[2] # About
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/design_menu_item_text')[3] # Contributors
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, 'android:id/button1')
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/design_menu_item_text')[6] # Settings
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'android:id/title')[0] # Show Tutorial
    el.click()
    time.sleep(1)

    el = driver.find_element(AppiumBy.ID, 'org.bookdash.android:id/activity_help_skip_textview') # Skip
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1] # New Book Notifications
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1] # New Book Notifications
    el.click()

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    el.click()
    time.sleep(1)

    el = driver.find_elements(AppiumBy.ID, 'org.bookdash.android:id/design_menu_item_text')[0] # All Books
    el.click()
finally:
    time.sleep(3)
    driver.quit()
