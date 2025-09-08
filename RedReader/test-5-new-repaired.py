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
    # Click on "More options"
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(1)

    # Click on "Settings" - still the 3rd item in the menu
    el = driver.find_elements(AppiumBy.ID, 'org.quantumbadger.redreader:id/title')[2]
    el.click()
    time.sleep(1)

    # Now we're in Settings screen, the structure has changed to RecyclerView
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Appearance"
    settings_items[0].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Find settings items again as they might have been refreshed
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Font"
    settings_items[1].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Behaviour"
    settings_items[2].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Images/Video"
    settings_items[3].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Cache"
    settings_items[4].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Network"
    settings_items[5].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "Menus"
    settings_items[6].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Refresh settings items
    settings_items = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')
    
    # Click on "About" - now it's the 9th item (index 8) due to added categories
    settings_items[9].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    
    # Go back to main screen
    # In v2, we can use the back navigation in the top bar
    back_button = driver.find_element(AppiumBy.XPATH, 
                                      "//android.widget.RelativeLayout[@content-desc='Back']")
    back_button.click()

finally:
    time.sleep(3)
    driver.quit()
