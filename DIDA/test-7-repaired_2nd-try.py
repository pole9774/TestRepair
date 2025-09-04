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
    # Step 1: Open side bar - This element is still accessible the same way
    # The ImageButton is still the first one in the screen
    el1 = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')[0]
    el1.click()
    time.sleep(3)

    # Step 2: Click settings button - ID has changed in v2
    # In v2, the settings button has ID 'amc' instead of 'settings_btn'
    # Using the parent layout for better targeting
    settings_btn = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/amd')
    settings_btn.click()
    time.sleep(3)

    # Step 3: Click on profile/level section in Settings - ID has changed in v2
    # In v2, the level icon has ID 'aa1' and is now a RelativeLayout
    profile_section = driver.find_element(AppiumBy.ID, 'cn.ticktick.task:id/aa1')
    profile_section.click()
    time.sleep(3)

    # Step 4: Click 'My Achievement Score' - Using accessibility ID which is more reliable
    # The content-desc attribute "My Achievement Score" is used for accessibility
    achievement_score = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Achievement Score')
    achievement_score.click()

finally:
    time.sleep(5)
    driver.quit()
