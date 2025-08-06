import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# todo: Select a network in advance when entering, and you need to wait a little longer

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.0.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.10.0.apk",
    "appWaitActivity": "be.brunoparmentier.openbikesharing.app.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 3: More options---Map layer

time.sleep(5)

el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[2]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[3]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/title')[1]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0]
el.click()
time.sleep(1)

driver.back()
time.sleep(1)

driver.quit()
