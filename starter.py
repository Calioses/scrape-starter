from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
url = "https://www.goodreads.com/book/show/18885833-open-season"
driver.get(url)

# Wait for the page to load
WebDriverWait(driver, 10)

# Get the entire page HTML
html = driver.page_source

# Print the HTML to the console
file1 = open("MyFile.html", "w", encoding='utf8')
file1.write(html)
file1.close()

# Quit the driver
driver.quit()
