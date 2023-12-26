from logs.logger import logger
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    logger.info('Browser is opend')
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logger.info(f'################### Test Case: {test_name} ######################')
    driver.maximize_window()
    logger.info('Browser is maximized')
    yield driver
    # driver.implicitly_wait(10)
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr".\evidence\{test_name}_{timestamp}.png")
    logger.info(f'Screenshot is created')
    driver.quit()

