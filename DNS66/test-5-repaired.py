import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# After installing, press and hold to start and then shut down

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    #"app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.4.1.apk",
    "app": "C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\TestRepair\\DNS66\\DNS66 v0.6.8.apk",
    "appWaitActivity": "org.jak_linux.dns66.*",
    "noReset": True,
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options()
for key, value in desired_caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(20)

# test case 5: DNS Servers main interface

time.sleep(5)

# Navigate to DNS tab (changed from bottom navigation to tabs)
dns_tab = driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='DNS']")
dns_tab.click()
time.sleep(1)

# Toggle DNS servers
dns_enabled = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/dns_enabled')
dns_enabled.click()
time.sleep(1)

dns_enabled = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/dns_enabled')
dns_enabled.click()
time.sleep(1)

# Add new DNS server (button ID changed)
add_button = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/floating_action_button')
add_button.click()
time.sleep(1)

# Input title and location
title_input = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/title')
title_input.clear()  # Clear any existing text
title_input.send_keys('test')
time.sleep(1)

location_input = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/location')
location_input.clear()  # Clear any existing text
location_input.send_keys('test')
time.sleep(1)

# Toggle enabled state
state_switch = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/state_switch')
state_switch.click()
time.sleep(1)

state_switch = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/state_switch')
state_switch.click()
time.sleep(1)

# Save the new entry
save_button = driver.find_element(AppiumBy.ID, 'org.jak_linux.dns66:id/action_save')
save_button.click()
time.sleep(1)

# Toggle the existing DNS servers
# Using XPATH to find the item_enabled elements more reliably
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')

# Toggle first server
dns_servers[0].click()
time.sleep(1)
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')
dns_servers[0].click()
time.sleep(1)

# Toggle second server
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')
dns_servers[1].click()
time.sleep(1)
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')
dns_servers[1].click()
time.sleep(1)

# Toggle third server
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')
dns_servers[2].click()
time.sleep(1)
dns_servers = driver.find_elements(AppiumBy.ID, 'org.jak_linux.dns66:id/item_enabled')
dns_servers[2].click()
time.sleep(1)

driver.quit()
