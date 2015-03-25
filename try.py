__author__ = 'Kaniska'

from selenium import webdriver
from saucelabs import sauceclient

sauce_url = "http://kaniska2008:f99fe868-7283-4e45-befc-2381921bccc3@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

browser = webdriver.Firefox()
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(10)

driver.get('http://google.com')
assert "Google" in driver.title
href = browser.find_element_by_name('q')  # Find the search box
href.send_keys('kaniska.in' + Keys.RETURN)