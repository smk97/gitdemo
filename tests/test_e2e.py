import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # passing fixture name as an argument will make it usable by this method
        # def test_e2e(self, gedata):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.finalCheckout().click()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        checkoutpage = CheckOutPage(self.driver)
        checkoutpage.select_c()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        checkoutpage.terms()
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        checkoutpage.submit()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)

