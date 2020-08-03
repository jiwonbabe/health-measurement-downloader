from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"/downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)
driver.get("https://app.powerbi.com/view?r=eyJrIjoiNjIyMDVhZGEtOTc0OS00ZDU5LWJlNTEtZDNkMjFlMzVmOTZkIiwidCI6ImFkMjIxNzg0LTcyYTgtNDI2My1hYzg2LTBjY2M2YjE1MmNkOCIsImMiOjh9")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label=' 책갈피 이미지. Go to COVID-19 Government Public Health Mitigation Measures - Tabular Data']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label=' 웹 URL 이미지. Data Download']"))).click()
action = webdriver.ActionChains(driver)
action.send_keys(Keys.ENTER)