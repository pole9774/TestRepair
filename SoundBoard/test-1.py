import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\SoundBoard\\SoundBoard v0.91.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\SoundBoard\\SoundBoard v0.92.apk",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# Test case 1: Add
# Note: I added an audio file to the first folder.

time.sleep(5)

el = driver.find_element(AppiumBy.ID, "de.meonwax.soundboard:id/action_new")
el.click()

el = driver.find_element(AppiumBy.ID, "android:id/button2")
el.click()

el = driver.find_element(AppiumBy.ID, "de.meonwax.soundboard:id/action_new")
el.click()

el = driver.find_elements(AppiumBy.ID, "de.meonwax.soundboard:id/directory_entry_name")[0]
el.click()

el = driver.find_elements(AppiumBy.ID, "de.meonwax.soundboard:id/directory_entry_name")[1]
el.click()

driver.quit()
