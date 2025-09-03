import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.1.3.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\AntennaPod\\AntennaPod v2.5.0.apk",
    "appWaitActivity": "de.danoeh.antennapod.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# The sidebar will automatically open when you start the app for the first time, so before starting, open the app and close the sidebar.

# test case 3: Click Downloads in the sidebar

time.sleep(5)

el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Open menu')[0] # Open side bar
el.click()
time.sleep(1)

# In v2.5.0, the sidebar structure changed from ListView to RecyclerView
# But we can still select the Downloads item directly using its index
downloads_item = driver.find_elements(AppiumBy.XPATH, 
    "//androidx.recyclerview.widget.RecyclerView[@resource-id='de.danoeh.antennapod:id/nav_list']/android.widget.RelativeLayout")[3]
downloads_item.click()
time.sleep(1)

# Refresh button still has the same ID
el = driver.find_element(AppiumBy.ID, 'de.danoeh.antennapod:id/refresh_item')
el.click()
time.sleep(1)

# In v2.5.0, the Downloads screen starts directly on the "Completed" tab
# and only has "Completed" and "Log" tabs (no "Running" tab)
# So we can skip the "Running" tab click and proceed with the other tabs

# Click on "Completed" tab (it's already selected by default, but we can click it for consistency)
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Completed')[0]
el.click()
time.sleep(1)

# Click on "Log" tab
el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'Log')[0]
el.click()
time.sleep(1)

driver.quit()
