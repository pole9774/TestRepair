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
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Step 1: Open sidebar - Fix for v2
    # Using XPath to find the hamburger menu button at the top left
    # This is more reliable than using class name and index in v2
    el1 = driver.find_element(AppiumBy.XPATH, 
        '//android.widget.ImageButton[@bounds="[0,63][147,210]"]')
    el1.click()
    
    # Alternative methods that should also work:
    # Option A: Find the first ImageButton within the toolbar area
    # el1 = driver.find_element(AppiumBy.XPATH, 
    #     '//android.view.ViewGroup[@resource-id="cn.ticktick.task:id/auw"]/android.widget.ImageButton')
    
    # Option B: Find the first ImageButton in the app (still works in this case)
    # el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0]
    
    time.sleep(3)

    # Step 2: Click on profile picture - Using the parent element which is clickable in v2
    el2 = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/adf')
    el2.click()
    time.sleep(3)

    # Step 3: Click on 'My Achievement Score' - Using accessibility ID for reliability
    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Achievement Score')
    el3.click()

finally:
    time.sleep(5)
    driver.quit()
