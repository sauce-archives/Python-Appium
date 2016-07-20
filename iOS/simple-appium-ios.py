from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['appiumVersion'] = '1.4.16'
desired_caps['platformVersion'] = '8.4'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['browserName'] = ''
desired_caps['name'] = 'Sample Test'
desired_caps['app'] = 'https://s3.amazonaws.com/appium/TestApp8.4.app.zip'

driver = webdriver.Remote('http://YOUR_SAUCE_USERNAME:YOUR_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub', desired_caps)

# Test Actions here...

driver.quit()