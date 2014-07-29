__author__ = 'Kan!skA'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()
browser = webdriver.Chrome('C:/Users/Kan!skA/PycharmProjects/chromedriver.exe')
# browser = webdriver.Ie('C:/Users/Kan!skA/PycharmProjects/IEDriverServer.exe')

browser.get('http://www.google.com')
assert 'Google' in browser.title
href = browser.find_element_by_name('q')  # Find the search box
href.send_keys('kaniska.in' + Keys.RETURN)
browser.quit()