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
    # Give more time for settings screen to load
    time.sleep(2)

    # Now we're in Settings screen, using more specific selectors for v2
    # The settings items now have resource-id android:id/title inside a RecyclerView
    
    # Click on "Appearance"
    appearance = driver.find_element(AppiumBy.XPATH, 
                                   "//android.widget.TextView[@resource-id='android:id/title' and @text='Appearance']")
    appearance.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Font"
    font = driver.find_element(AppiumBy.XPATH, 
                             "//android.widget.TextView[@resource-id='android:id/title' and @text='Font']")
    font.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Behaviour"
    behaviour = driver.find_element(AppiumBy.XPATH, 
                                  "//android.widget.TextView[@resource-id='android:id/title' and @text='Behaviour']")
    behaviour.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Images/Video"
    images_video = driver.find_element(AppiumBy.XPATH, 
                                     "//android.widget.TextView[@resource-id='android:id/title' and @text='Images/Video']")
    images_video.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Cache"
    cache = driver.find_element(AppiumBy.XPATH, 
                              "//android.widget.TextView[@resource-id='android:id/title' and @text='Cache']")
    cache.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Network"
    network = driver.find_element(AppiumBy.XPATH, 
                                "//android.widget.TextView[@resource-id='android:id/title' and @text='Network']")
    network.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "Menus"
    menus = driver.find_element(AppiumBy.XPATH, 
                              "//android.widget.TextView[@resource-id='android:id/title' and @text='Menus']")
    menus.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)

    # Click on "About" - now find it by text rather than index
    about = driver.find_element(AppiumBy.XPATH, 
                              "//android.widget.TextView[@resource-id='android:id/title' and @text='About']")
    about.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    
    # Go back to main screen using the back button at the top
    back_button = driver.find_element(AppiumBy.XPATH, 
                                    "//android.widget.RelativeLayout[@content-desc='Back']")
    back_button.click()

finally:
    time.sleep(3)
    driver.quit()
