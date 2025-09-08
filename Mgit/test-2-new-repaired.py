import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\Mgit\\Mgit v1.5.1.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\Mgit\\Mgit v1.6.1.apk",
    "appWaitActivity": "com.manichord.mgit.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Search

time.sleep(15)

el = driver.find_element(AppiumBy.ID, 'com.manichord.mgit:id/action_search')
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/search_src_text')
el.send_keys('test')
time.sleep(1)

driver.press_keycode(66) # ENTER
time.sleep(1)

# The up button has changed to a Collapse button in v2
try:
    # Try to find the old up button first (for backward compatibility)
    el = driver.find_element(AppiumBy.ID, 'android:id/up')
    el.click()
except:
    # If not found, use the new Collapse button
    el = driver.find_element(AppiumBy.XPATH, 
                            '//android.widget.ImageButton[@content-desc="Collapse"]')
    el.click()
time.sleep(1)

driver.quit()
