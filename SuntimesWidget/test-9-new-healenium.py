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
	"sessionKey": "SuntimesWidget_test-9-new"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.XPATH, "//*[@text='Set Time Zone']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.XPATH, "//*[@text='Cancel']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.XPATH, "//*[@text='Set Time Zone']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Mode
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Solar Time
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # Solar Time: ...
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Apparent Solar Time
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # Solar Time: ...
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # Local Mean Time
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Mode
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # System Time Zone
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Mode
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[2] # User Defined
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # Time Zone: ...
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text2')[0] # First Time Zone in the list
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.XPATH, "//*[@text='Set']") # Healenium: UIAUTOMATOR selector changed to XPATH
    el.click()

finally:
    time.sleep(3)
    driver.quit()
