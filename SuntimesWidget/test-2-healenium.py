import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.forrestguice.suntimeswidget",
    "appActivity": "com.forrestguice.suntimeswidget.SuntimesActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "SuntimesWidget_test-2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_elements(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/action_location_add')[0] # Location
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_location_mode')[0] # Mode
    el2.click()
    time.sleep(3)

    el3 = driver.find_element(AppiumBy.XPATH, "//*[@text='Current (last known)']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el3.click()
    time.sleep(3)

    el4 = driver.find_elements(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/appwidget_location_mode')[0] # Mode
    el4.click()
    time.sleep(3)

    el5 = driver.find_element(AppiumBy.XPATH, "//*[@text='User Defined']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el5.click()
    time.sleep(3)

    el6 = driver.find_element(AppiumBy.XPATH, "//*[@text='Cancel']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el6.click()

finally:
    time.sleep(3)
    driver.quit()
