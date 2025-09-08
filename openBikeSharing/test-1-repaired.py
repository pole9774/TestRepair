import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# todo: Select a network in advance when entering, and you need to wait a little longer

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.0.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\openBikeSharing\\openBikeSharing v1.10.0.apk",
    "appWaitActivity": "be.brunoparmentier.openbikesharing.app.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 1: Main interface

time.sleep(5)

# In v2, Refresh is in the overflow menu
# Click on "More options" button first
more_options_button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='More options']")
more_options_button.click()
time.sleep(1)

# Then click on "Refresh" in the overflow menu
refresh_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Refresh']")
refresh_option.click()
time.sleep(1)

# Map button still exists with the same ID
map_button = driver.find_element(AppiumBy.ID, 'be.brunoparmentier.openbikesharing.app:id/action_map')
map_button.click()
time.sleep(1)

driver.quit()
