# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import logging
# from Locators.locators import *
# from config.configarations import *
#
#
#
#
# def test_login():
#     url = 'https://www.naukri.com/'
#     d = webdriver.Chrome()
#     d.get(url)
#     time.sleep(4)
#     d.maximize_window()
#     d.find_element(By.XPATH, login_button_xpath).click()
#     login_form = d.find_element(By.XPATH, login_form_xpath)
#     time.sleep(3)
#     if login_form.is_displayed():
#         logging.info("Login form loaded Successful")
#     else:
#         logging.info("Login form not loaded Successful")
#     d.find_element(By.XPATH, email_input_xpath).send_keys(email)
#     d.find_element(By.XPATH, password_input_xpath).send_keys(password)
#     d.find_element(By.XPATH, button_login).click()
#     time.sleep(3)
#     d.find_element(By.XPATH,profile_icon_xpath).is_displayed()
#     time.sleep(5)
#     d.find_element(By.XPATH,profile_icon_xpath).click()
#     time.sleep(3)
#     d.find_element(By.XPATH,button_complete_profile_xpath).click()
#     time.sleep(3)
#     d.find_element(By.XPATH,edit_icon_resume_headline).click()
#     d.find_element(By.XPATH,input_field_xpath).send_keys('..')
#     time.sleep(3)
#     d.find_element(By.XPATH,save_button_xpath).click()
#     logging.info("updated success ...")
#
#
# # def test_update_profile():
# #     url = 'https://www.naukri.com/'
# #     d = webdriver.Chrome()
#
#
#
