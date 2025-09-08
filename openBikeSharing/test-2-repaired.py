import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Uncomment the appropriate app path based on the version you want to test
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

# test case 2: More options - Choose A Network

time.sleep(5)

# Click on "More options" (same in both versions)
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
el.click()
time.sleep(1)

# Click on "Settings" - In v2 it's at index 1 instead of 0
try:
    # First try with title text (more reliable)
    settings_elements = driver.find_elements(AppiumBy.ID, 'android:id/title')
    for element in settings_elements:
        if element.text == "Settings":
            element.click()
            break
except:
    # Fallback: In v2, Settings is the second item (index 1)
    elements = driver.find_elements(AppiumBy.ID, 'android:id/title')
    if len(elements) > 1:
        elements[1].click()  # For v2
    else:
        elements[0].click()  # For v1
time.sleep(1)

# Click on "Choose a network" - First option in both versions
try:
    network_elements = driver.find_elements(AppiumBy.ID, 'android:id/title')
    for element in network_elements:
        if element.text == "Choose a network":
            element.click()
            break
except:
    # Fallback to index-based selection (first item in both versions)
    driver.find_elements(AppiumBy.ID, 'android:id/title')[0].click()
time.sleep(1)

# Navigate back twice (same in both versions)
driver.back()
time.sleep(1)

driver.back()
time.sleep(1)

driver.quit()
