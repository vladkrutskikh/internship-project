from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support import expected_conditions as EC

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """

    bs_user = 'vladkrutskikh_ROyqsE'
    bs_key = 'CsmTHTdxwW8mYeN4x1A2'
    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'browserName': 'chrome',
        'osVersion': 'Windows 10'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    # options = Options()                 #Chrome
    # options.add_argument("--headless=new")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    # service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)


    # options = FirefoxOptions()        #Firefox
    # options.add_argument("--headless")
    # service = FirefoxService(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service, options=options)

    # context.driver = webdriver.Safari() #Safari

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    context.WebDriverWait = WebDriverWait
    context.EC = EC


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()