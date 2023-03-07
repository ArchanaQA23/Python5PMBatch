from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given(u'User launches the url')
def launch_url(context):

    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.google.com")
    context.driver.maximize_window()
    context.driver.implicitlyWait(10);



@when(u'User check the title')
def check_title(context):

    text=context.driver.title
    print(text)

@when(u'User click on Gmail link')
def click_gmail(context):
    context.driver.find_element(By.LINK_TEXT,"Gmail").click()

@then(u'User should see the gmail page')
def gmail_page(context):
     context.driver.close()
