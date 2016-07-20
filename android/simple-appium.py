from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['appiumVersion'] = '1.4.16'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['browserName'] = ''
desired_caps['name'] = 'Sample Test'
desired_caps['app'] = 'http://appium.s3.amazonaws.com/ContactManager.apk'

driver = webdriver.Remote('http://YOUR_SAUCE_USERNAME:YOUR_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub', desired_caps)

# Test Actions here...

driver.quit()