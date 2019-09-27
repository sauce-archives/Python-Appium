import os

from appium import webdriver


caps = {
        'appiumVersion':    '1.13.0',
        'browserName':      'safari',
        'platformName':     'iOS',
        'deviceName':       'iPhone XS Simulator',
        'platformVersion':  '12.2',
        'deviceOrientation':'portrait',
        'name': 'simple-ios'
        # you can set a destination for an app to load on the emulator 
        # 'app': 'http://appium.s3.amazonaws.com/ContactManager.apk'
}

user = os.environ.get('SAUCE_USERNAME', 'my-username')
access_key = os.environ.get('SAUCE_ACCESS_KEY', 'my-key')

sauce_url = "https://{}:{}@ondemand.saucelabs.com/wd/hub/".format(user,access_key)

driver = webdriver.Remote(sauce_url, desired_capabilities=caps)

# appium application logic here

driver.quit()
