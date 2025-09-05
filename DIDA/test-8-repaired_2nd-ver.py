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
    # Open side bar - using XPath for more precise targeting
    sidebar_button = driver.find_element(
        AppiumBy.XPATH, 
        '//android.view.ViewGroup[@resource-id="cn.ticktick.task:id/auw"]/android.widget.ImageButton'
    )
    sidebar_button.click()
    time.sleep(3)

    # Click settings button - finding by its parent layout and position
    settings_button = driver.find_element(
        AppiumBy.XPATH, 
        '//android.widget.RelativeLayout[@resource-id="cn.ticktick.task:id/amd"]/android.widget.TextView'
    )
    settings_button.click()
    time.sleep(3)

    # Try multiple ways to find the "Add Tasks in Wechat" element
    try:
        # First try by exact text
        wechat_element = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().text("Add Tasks in Wechat")'
        )
    except:
        # Fallback to partial text match
        wechat_element = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().textContains("Wechat")'
        )
    
    wechat_element.click()

finally:
    time.sleep(5)
    driver.quit()
