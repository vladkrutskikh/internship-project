from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support import expected_conditions as EC

from app.application import Application

def browser_init(context, device_index=0):
    """
    :param context: Behave context
    """
    # Mobile Chrome Web Driver
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
    #                                   options=chrome_options)
    # context.app = Application(context.driver)

    bs_user = 'vladkrutskikh_ROyqsE'  # BrowserStack MOB
    bs_key = 'CsmTHTdxwW8mYeN4x1A2'
    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # Список устройств для тестирования
    devices = [
        # {'deviceName': 'Samsung Galaxy S22', 'osVersion': '12.0', 'browserName': 'chrome'},
        # {'deviceName': 'iPhone 13 Pro', 'osVersion': '15', 'browserName': 'chrome'},
        {'deviceName': 'Google Pixel 6', 'osVersion': '12.0', 'browserName': 'chrome'}
    ]

    # Создаем список драйверов для всех устройств
    context.drivers = []
    for device in devices:
        options = Options()
        bstack_options = {
            'deviceName': device['deviceName'],
            'osVersion': device['osVersion'],
            'browserName': device['browserName']
            # 'interactiveDebugging': 'true'
        }
        options.set_capability('bstack:options', bstack_options)
        driver = webdriver.Remote(command_executor=url, options=options)
        driver.implicitly_wait(4)
        driver.wait = WebDriverWait(driver, 15)
        context.drivers.append(driver)

    # Устанавливаем текущий драйвер как первый в списке
    context.driver = context.drivers[0]
    context.app = Application(context.driver)


    # bs_user = 'vladkrutskikh_ROyqsE'    #BrowserStack
    # bs_key = 'CsmTHTdxwW8mYeN4x1A2'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     'browserName': 'chrome',
    #     'osVersion': 'Windows 10'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    # options = Options()     #Chrome Headless Mode
    # options.add_argument("--headless=new")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    # service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # options = Options()                 #Chrome
    # options.add_argument("--window-size=1920,1080")
    # service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)


    # options = FirefoxOptions()        #Firefox
    # options.add_argument("--headless")
    # service = FirefoxService(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service, options=options)

    # context.driver = webdriver.Safari() #Safari

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name) # for WEB
    browser_init(context)
    context.WebDriverWait = WebDriverWait
    context.EC = EC




def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


# def after_scenario(context, feature): #for WEB
#     context.driver.delete_all_cookies()
#     context.driver.quit()

def after_scenario(context, feature): #for MOB
    for driver in context.drivers:
        driver.delete_all_cookies()
        driver.quit()