from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://preprod.testaonline.com/signin")
email_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "outlined-adornment-email")))
email_id.send_keys("abhijeet@radiantinfonet.com")
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "outlined-adornment-password")))
password.send_keys("Abhijeet@123")
signin_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']")))
signin_button.click()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Welcome back, Business Dashboard']")))
print("Signin Successful!")

# Open the batch creation page
driver.get("https://preprod.testaonline.com/exam-management/create-batch")

# Wait for Batch ID field to be visible
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "outlined-adornment-batchId")))

# ========== STEP 1: Fill Batch Details ==========
BatchID = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "outlined-adornment-batchId")))
BatchID.send_keys("Batch_Py")

BatchSize = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "outlined-adornment-batchSize")))
BatchSize.send_keys("20")

# Select Scheme
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mui-component-select-schemeId"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Select Sub-Scheme
driver.find_element(By.ID, "mui-component-select-subshemeId").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Dates (input must be in correct format like '04/06/2025')
driver.find_element(By.ID, ":rgf:").send_keys("04/06/2025")  # Start Date
driver.find_element(By.ID, ":rgh:").send_keys("05/06/2025")  # End Date

# Time (if it accepts AM/PM format)
driver.find_element(By.ID, ":rfm:").send_keys("10:00 AM")    # Start Time
driver.find_element(By.ID, ":rfp:").send_keys("01:00 PM")    # End Time

# Batch Mode
driver.find_element(By.ID, "mui-component-select-batchMode").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Exam Center
driver.find_element(By.ID, "mui-component-select-centerId").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# ========== STEP 2: Fill Question Paper Details ==========

# Job Role
driver.find_element(By.ID, "asynchronous-demo").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# QP Code
driver.find_element(By.ID, "mui-component-select-qpCode").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Level
driver.find_element(By.XPATH, "//label[text()='Level']/following-sibling::div").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Version
driver.find_element(By.XPATH, "//label[text()='version']/following-sibling::div").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Instruction
driver.find_element(By.XPATH, "//label[text()='chooseInstructions']/following-sibling::div").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

# Question Set & Passing %
driver.find_element(By.ID, "outlined-adornment-questionSet").send_keys("Q123")
driver.find_element(By.ID, "outlined-adornment-passingPercentage").send_keys("40")

# ========== STEP 3: Select Sections ==========

driver.find_element(By.XPATH, "//input[@name='sectionName' and @value='theory']").click()
driver.find_element(By.XPATH, "//td[text()='Theory']/following-sibling::td[2]//input[@name='examDuration']").send_keys("60")

driver.find_element(By.XPATH, "//input[@name='sectionName' and @value='viva']").click()
driver.find_element(By.XPATH, "//td[text()='Viva']/following-sibling::td[1]//div[contains(@class, 'MuiSelect-root')]").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='2']"))).click()
driver.find_element(By.XPATH, "//td[text()='Viva']/following-sibling::td[2]//input[@name='examDuration']").send_keys("20")

driver.find_element(By.XPATH, "//input[@name='sectionName' and @value='practical']").click()
driver.find_element(By.XPATH, "//td[text()='Practical']/following-sibling::td[1]//div[contains(@class, 'MuiSelect-root')]").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='3']"))).click()
driver.find_element(By.XPATH, "//td[text()='Practical']/following-sibling::td[2]//input[@name='examDuration']").send_keys("30")

# ========== STEP 4: Final Submit ==========

# Optional remarks
driver.find_element(By.ID, "outlined-adornment-financeRemarks").send_keys("Automated entry")

# Submit
driver.find_element(By.XPATH, "//button[normalize-space(text()) = 'Submit']").click()

# ========== Verification ==========
time.sleep(5)
print("Batch submitted successfully (check manually for toast or confirmation dialog).")

driver.quit()
