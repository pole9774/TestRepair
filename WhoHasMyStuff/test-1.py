import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\WhoHasMyStuff\\WhoHasMyStuff v1.0.24.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\WhoHasMyStuff\\WhoHasMyStuff v1.0.38.apk",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Add, select type as Book

time.sleep(5)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/addButton")
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/add_description")
el.clear()

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/add_description")
el.send_keys("Test1")
time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[0]
el.click()
time.sleep(2)

el = driver.find_elements(AppiumBy.ID, "android:id/text1")[1]
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/pickDate")
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "android:id/button1")
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/choosePerson")
el.click()
time.sleep(2)

driver.back()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/add_calendar_checkbox")
el.click()
time.sleep(2)

# el = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')[7]
# el.click()
# time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/add_calendar_checkbox")
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/add_button")
el.click()
time.sleep(2)

driver.quit()
