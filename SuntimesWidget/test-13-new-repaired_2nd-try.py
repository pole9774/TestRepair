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
    # Click on More options
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
    el.click()
    time.sleep(3)

    # Click on World Map
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="World Map"]')
    el.click()
    time.sleep(3)
    
    # Click on map options menu (top right)
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/map_modemenu')
    el.click()
    time.sleep(2)
    
    # Select Basic Map (current selection)
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Map"]')
    el.click()
    time.sleep(3)
    
    # Click on map options menu again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/map_modemenu')
    el.click()
    time.sleep(2)
    
    # Select Blue Marble
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Blue Marble"]')
    el.click()
    time.sleep(3)
    
    # Click on map options menu again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/map_modemenu')
    el.click()
    time.sleep(2)
    
    # Select Polar [north]
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Polar [north]"]')
    el.click()
    time.sleep(3)
    
    # Click on map options menu again
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/map_modemenu')
    el.click()
    time.sleep(2)
    
    # Go back to Basic Map
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Map"]')
    el.click()
    time.sleep(3)
    
    # Now we need to access the display options (Sunlight, Moonlight)
    # Click on the more options menu in the bottom right
    el = driver.find_element(AppiumBy.ID, 'com.forrestguice.suntimeswidget:id/map_menu')
    el.click()
    time.sleep(2)
    
    # Click on Options
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Options"]')
    el.click()
    time.sleep(2)
    
    # Toggle Sunlight option (uncheck it first, since it's checked by default)
    # Now using the correct path based on XML structure
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Sunlight"]/../following-sibling::android.widget.CheckBox')
    el.click()
    time.sleep(3)
    
    # Toggle Sunlight back on
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Sunlight"]/../following-sibling::android.widget.CheckBox')
    el.click()
    time.sleep(3)
    
    # Toggle Moonlight option
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Moonlight"]/../following-sibling::android.widget.CheckBox')
    el.click()
    time.sleep(3)
    
    # Toggle Moonlight back on
    el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Moonlight"]/../following-sibling::android.widget.CheckBox')
    el.click()
    time.sleep(3)
    
    # Go back
    driver.back()
    time.sleep(1)
    
    # Go back to the main screen
    driver.back()
    time.sleep(1)

finally:
    time.sleep(3)
    driver.quit()
