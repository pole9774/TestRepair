import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "cn.ticktick.task",
    "appActivity": "com.ticktick.task.activity.MeTaskActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "healenium:session": True,
	"sessionKey": "DIDA_test-1"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://127.0.0.1:8085", options=options)

time.sleep(5)

try:
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0] # open side bar
    el1.click()
    time.sleep(3)

    el2 = driver.find_elements(AppiumBy.ID, 'cn.ticktick.task:id/photo')[0] # profile picture
    el2.click()
    time.sleep(3)

    el3 = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Image")[0] # 'My Achievement Score'
    el3.click()

finally:
    time.sleep(5)
    driver.quit()
