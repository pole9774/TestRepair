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
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "Mgit_test-1"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)
driver.implicitly_wait(20)

# test case 1: Clone

time.sleep(15)

el = driver.find_element(AppiumBy.ID, 'com.manichord.mgit:id/action_new') # + button
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'com.manichord.mgit:id/remoteURL')
el.send_keys('https://github.com/Vallxy/Vallxy.github.io.git')
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'com.manichord.mgit:id/localPath')
el.send_keys('Vallxy')
time.sleep(1)

el = driver.find_element(AppiumBy.ID, 'android:id/button1') # Clone
el.click()
time.sleep(60)

driver.quit()
