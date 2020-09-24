from selenium import webdriver
import time
import getpass
import spider

# log into github
def github_login(login_url):    
    # log into github
    driver.get(login_url)

    # login through console
    # username=input('Please input your username: ')
    # password=getpass.getpass('Please input your password: ')
    # print(username,password)

    # clear the login field and input username
    driver.find_element_by_id('login_field').clear()
    driver.find_element_by_id('login_field').send_keys('ted-test')
    # clear the password field and input password
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('gmZtiU78dBaN7CN')
    # sign in github
    driver.find_element_by_name('commit').click()

# Watch the project with "Releases only" option
def watch_project(project_url):
    driver.get(project_url)
    # find the "Watch" button
    driver.find_element_by_class_name('btn.btn-sm.btn-with-count').click()
    # uses xpath to find the button which value=release_only, then click to watch the project
    driver.find_element_by_xpath("//button[@value='release_only']").click()

# Unwatch the project
def unwatch_project(project_url):
    driver.get(project_url)
    # find the "Watch" button
    driver.find_element_by_class_name('btn.btn-sm.btn-with-count').click()
    # uses xpath to find the button which value=included, then click to watch the project
    driver.find_element_by_xpath("//button[@value='included']").click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    # driver.maximize_window()
    login_url='https://github.com/login'
    projects=spider.spider()
    github_login(login_url)
    for project in projects:
        watch_project(project)

    for project in projects:
        unwatch_project(project)    #unwatch all projects

    driver.quit()
