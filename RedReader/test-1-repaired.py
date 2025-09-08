import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.quantumbadger.redreader",
    "appActivity": "org.quantumbadger.redreader.activities.MainActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    # Find the "Find Location" option (previously "Custom Location")
    # Using accessibility ID is more reliable than indices
    find_location_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Custom Location")
    find_location_btn.click()
    time.sleep(3)
    
    # Click on the spinner to open dropdown
    type_spinner = driver.find_element(AppiumBy.ID, "org.quantumbadger.redreader:id/dialog_mainmenu_custom_type")
    type_spinner.click()
    time.sleep(3)
    
    # Select "Subreddit" from the dropdown options
    subreddit_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Subreddit']")
    subreddit_option.click()
    time.sleep(3)
    
    # Type subreddit name (optional)
    input_field = driver.find_element(AppiumBy.ID, "org.quantumbadger.redreader:id/dialog_mainmenu_custom_value")
    input_field.send_keys("androiddev")
    time.sleep(1)
    
    # Click the "Go" button
    go_button = driver.find_element(AppiumBy.ID, "android:id/button1")
    go_button.click()

finally:
    time.sleep(1)
    driver.quit()
