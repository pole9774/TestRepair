import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Restore to the initial state for each test
# In the first folder of the system ofm, init01.png and init02.csv are stored (the second file format is optional)

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\OIFileManager\\OIFileManager v2.0.5.apk",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\OIFileManager\\OIFileManager v2.2.2.apk",
    "appWaitActivity": "org.openintents.filemanager.FileManagerActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# Note:
# 1. For the first startup, manually skip the lead page
# 2. For testing purposes, two files are placed in the first folder, the first of which is an image
# 3. After execution, restore the files to their initial state for the next execution

# test case 1: Enter the first folder

time.sleep(10)

el = driver.find_elements(AppiumBy.ID, "org.openintents.filemanager:id/primary_info")[0]
el.click()
time.sleep(1)

time.sleep(1)
driver.quit()
