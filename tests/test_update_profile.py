import pytest
from utils.driver_factory import get_driver
from config.configarations import *
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.logger import logger


@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()


def test_update_resume_headline(setup):
    driver = setup

    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)

    logger.info("Opening Naukri Website")
    login_page.open_naukri(BASE_URL)

    logger.info("Clicking Login button")
    login_page.click_login()

    logger.info("Entering login details")
    login_page.login(email, password)

    logger.info("Opening Profile Section")
    profile_page.open_profile()

    logger.info("Updating Resume Headline")
    profile_page.update_resume_headline("Updated via Automation ✅")

    logger.info("✅ Resume headline updated successfully!")
