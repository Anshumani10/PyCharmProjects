import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("--ignore-certificate-errors")
driver.implicitly_wait(6)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#driver.execute_script("window.scrollBy(0,600);")

#driver.get_screenshot_as_file("screen.png")
















time.sleep(9)