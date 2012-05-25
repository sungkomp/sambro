# Set up New Volunteer
from tests.web2unittest import SeleniumUnitTest
from tests import *
import unittest, re, time

class hrm_setup_volunteer(SeleniumUnitTest):
    def test_setup_volunteer(self):
        
        browser = self.browser
        driver = browser
        driver.find_element_by_link_text("Staff & Volunteers").click()
        driver.find_element_by_link_text("New Volunteer").click()
        w_autocomplete("Rom","hrm_human_resource_organisation_id","Romanian Food Assistance Association (Test) (RFAAT)",False)
        driver.find_element_by_id("pr_person_first_name").clear()
        driver.find_element_by_id("pr_person_first_name").send_keys("John")
        driver.find_element_by_id("pr_person_last_name").clear()
        driver.find_element_by_id("pr_person_last_name").send_keys("Thompson")
        driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        driver.find_element_by_link_text("7").click()
        driver.find_element_by_id("pr_person_gender").send_keys("male")
        driver.find_element_by_id("pr_person_occupation").clear()
        driver.find_element_by_id("pr_person_occupation").send_keys("Social Worker")
        driver.find_element_by_id("pr_person_email").clear()
        driver.find_element_by_id("pr_person_email").send_keys("test@notavalidemail.com")
        driver.find_element_by_id("hrm_human_resource_job_title").clear()
        driver.find_element_by_id("hrm_human_resource_job_title").send_keys("Distributor")
        driver.find_element_by_id("hrm_human_resource_start_date").click()
        driver.find_element_by_id("hrm_human_resource_start_date").clear()
        driver.find_element_by_id("hrm_human_resource_start_date").send_keys("2012-04-17")
        driver.find_element_by_id("gis_location_L0").send_keys("Romania")
        driver.find_element_by_id("gis_location_street").clear()
        driver.find_element_by_id("gis_location_street").send_keys("23 Petru St")
        driver.find_element_by_id("gis_location_L3_ac").clear()
        driver.find_element_by_id("gis_location_L3_ac").send_keys("Bucharest")
        time.sleep(5)
        driver.find_element_by_id("ui-menu-2-0").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Home").click()
