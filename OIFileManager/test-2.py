import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Restore to the initial state after each test.
# Store init01.png and init02.csv in the first folder of the system (the second file's format is optional).

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

# Notes:
# 1. For the first launch, manually skip the introductory page.
# 2. For testing purposes, two files were placed in the first folder, the first of which is an image.
# 3. After execution, restore the files to their original state for the next run.

# test case 2: Current folder, More options, Donate

time.sleep(10)

el = driver.find_elements(AppiumBy.ID, "org.openintents.filemanager:id/primary_info")[0]
el.click()
time.sleep(1)

el = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageButton")
el.click()
time.sleep(1)

el = driver.find_elements(AppiumBy.ID, "android:id/title")[0]
el.click()
time.sleep(1)

time.sleep(5)

driver.back()

time.sleep(2)
driver.quit()
