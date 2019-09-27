import os

from appium import webdriver


caps = {
        'appiumVersion':    '1.9.1',
        'browserName':      'chrome',
        'platformName':     'Android',
        'platformVersion':  '8.1',
        'deviceOrientation':'portrait',
        'name': 'simple-android',
        # you can set a destination for an app to load on the emulator 
        # 'app': 'http://appium.s3.amazonaws.com/ContactManager.apk'
}

user = os.environ.get('SAUCE_USERNAME', 'my-username')
access_key = os.environ.get('SAUCE_ACCESS_KEY', 'my-key')

sauce_url = "https://{}:{}@ondemand.saucelabs.com/wd/hub/".format(user,access_key)

driver = webdriver.Remote(sauce_url, desired_capabilities=caps)

# appium application logic here

driver.quit()
