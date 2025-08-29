import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.forrestguice.suntimeswidget",
    "appActivity": "com.forrestguice.suntimeswidget.SuntimesActivity",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

try:
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("World Map")')
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/worldmap_selector') # Map type
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[1] # Blue Marble
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/worldmap_selector') # Map type
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[2] # Polar
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/worldmap_selector') # Map type
    el.click()
    time.sleep(3)

    el = driver.find_elements(AppiumBy.ID, 'android:id/text1')[0] # Basic
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/radio_sun') # Sunlight
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/radio_moon') # Moonlight
    el.click()
    time.sleep(3)

    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/radio_sunmoon') # Both
    el.click()
    time.sleep(3)

    driver.back()

finally:
    time.sleep(3)
    driver.quit()
