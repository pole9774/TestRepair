import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# After installing, press and hold to start and then shut down

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.4.1.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.6.8.apk",
    "appWaitActivity": "org.jak_linux.dns66.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 3: Hosts main interface

time.sleep(15)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/bottom_navigation_item_title')[1]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/host_enabled')
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/host_enabled')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_title')[0]
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[0]
el.clear()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[0]
el.send_keys('test')
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_save')
el.click()
time.sleep(10)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/host_add')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/title')[0]
el.send_keys('test')
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/location')
el.send_keys('test')
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/text1')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/text1')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/text1')
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[2]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_save')
el.click()
time.sleep(1)

driver.quit()
