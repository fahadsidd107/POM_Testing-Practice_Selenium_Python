import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class demoQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://demoqa.com/")
        cls.driver.maximize_window()

    def test_forms(self):
        self.BookStoreApplication = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]')
        self.driver.execute_script("arguments[0].click()", self.BookStoreApplication)
        self.loginbtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[1]')
        self.driver.execute_script("arguments[0].click()", self.loginbtn)
        self.loginbtn = self.driver.find_element(By.ID, 'newUser')
        self.driver.execute_script("arguments[0].click()", self.loginbtn)
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("Muhammad Fahad")
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys("Siddiqui")
        self.driver.find_element(By.ID, "userName").clear()
        self.driver.find_element(By.ID, "userName").send_keys("Fadflex")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})$")
        self.recapctha = self.driver.find_element(By.XPATH, "//*[@id='recaptcha-anchor']/div[2]")
        self.driver.execute_script("arguments[0].click()", self.recapctha)
  
    @classmethod
    def tearDownClass(cls):
     cls.driver.close()
     cls.driver.quit()
