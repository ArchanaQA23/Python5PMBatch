import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
@given(u'User launches the url of orange hrm page')
def launch_orangehrm(context):
     context.driver=webdriver.Chrome(ChromeDriverManager().install())
     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     context.driver.implicitly_wait(10)


@when(u'User enter the username "{user}" and password "{pwd}"')
def login_cred(context,user,pwd):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME,"password").send_keys(pwd)


@when(u'User clicks on login button')
def click_login(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)


@then(u'user should successfully login  to the dashboard page')
def check_dashboard(context):
    try:
        text=context.driver.find_element(By.XPATH,"//h6[text()='Dashboard']").text

    except:
        context.driver.close()
        assert False,"Test failed"

    if(text=="Dashboard"):
        context.driver.close()
        assert True,"Test passed "


