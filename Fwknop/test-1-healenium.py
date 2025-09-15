import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.cipherdyne.fwknop2",
    "appActivity": "biz.incomsystems.fwknop2.ConfigListActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "Fwknop_test-1"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el1.click()
    time.sleep(3)

    el2 = driver.find_element(AppiumBy.XPATH, "//*[@text='New config']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el2.click()
    time.sleep(3)

    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el3.click()
    time.sleep(3)

    el4 = driver.find_element(AppiumBy.XPATH, "//*[@text='Save config']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el4.click()

finally:
    time.sleep(5)
    driver.quit()
