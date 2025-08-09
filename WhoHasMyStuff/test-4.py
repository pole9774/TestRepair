import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\WhoHasMyStuff\\WhoHasMyStuff v1.0.24.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\WhoHasMyStuff\\WhoHasMyStuff v1.0.38.apk",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 4: Enter the first item, mark as returned
# First, execute test-1 and/or test-2 and/or test-3 to add an item

time.sleep(5)

el = driver.find_elements(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/toptext")[0]
el.click()
time.sleep(2)

el = driver.find_element(AppiumBy.ID, "de.freewarepoint.whohasmystuff:id/returned_button")
el.click()
time.sleep(2)

driver.quit()
