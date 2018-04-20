import urldata
import time


def amz_logon(driver):
    url_log = urldata.url_log
    driver.get(url_log)
    time.sleep(1)
    user = driver.find_element_by_name("email")
    # enter user name for amazon acount
    user.send_keys('******')
    password = driver.find_element_by_name("password")
    # enter password for amazon account
    password.send_keys('*******')
    login = driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
