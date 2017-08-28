from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
username = config.USERNAME
password = config.PASSWORD

def login(driver):
	# Load page
	driver.get("https://www.instagram.com/accounts/login/")

	# Login
	driver.find_element_by_xpath("//div/input[@name='username']").send_keys(username)
	driver.find_element_by_xpath("//div/input[@name='password']").send_keys(password)
	driver.find_element_by_xpath("//span/button").click()

	# Wait for the login page to load
	WebDriverWait(driver, 30).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Profile")))


def scrape_followers(driver, account):
	# Load account page
	driver.get("https://www.instagram.com/{0}/".format(account))

	# Click the 'Follower(s)' link
	driver.find_element_by_partial_link_text("follower").click()

	# Wait for the followers modal to load
	xpath = "//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[1]"
	WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, xpath)))

	# Pending Scrolling Magic Here #

	# Scrape the followers
	xpath = "//div[@style='position: relative; z-index: 1;']//ul/li/div/div/div/div/a"
	followers_elems = driver.find_elements_by_xpath(xpath)

	return [e.text for e in followers_elems]


if __name__ == "__main__":
	driver = webdriver.Chrome('drivers/chromedriver_win32.exe')
	try:
		login(driver)
		followers = scrape_followers(driver, username)
		print(followers)
	finally:
		driver.quit()
