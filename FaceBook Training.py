from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='/Users/moti/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('http://facebook.com')
driver.maximize_window()


def registration_screen():
    driver.find_elements_by_class_name("inputtext")[2].send_keys("Moti")
    driver.find_elements_by_class_name("inputtext")[3].send_keys("Hacking")
    driver.find_elements_by_class_name("inputtext")[4].send_keys("Madina@gmail.com")
    driver.find_elements_by_class_name("inputtext")[5].send_keys("Madina@gmail.com")
    driver.find_element_by_name("reg_passwd__").send_keys("1234567890lili")
    driver.find_element_by_name("birthday_month").click()
    driver.find_element_by_xpath("//option[@value='10']").click()
    driver.find_element_by_name("birthday_day").click()
    driver.find_element_by_xpath("//option[@value='25']").click()
    driver.find_element_by_name("birthday_year").click()
    driver.find_element_by_xpath("//option[@value='1989']").click()
    driver.find_elements_by_name("sex")[1].click()
    driver.find_element_by_name("websubmit").click()
    time.sleep(3)
    driver.quit()


def translate_screen():
    time.sleep(3)
    driver1 = webdriver.Chrome(executable_path='/Users/moti/Downloads/chromedriver')
    driver1.implicitly_wait(3)
    driver1.get('http://translate.google.com')
    driver1.maximize_window()
    driver1.find_element_by_class_name("tl-more").click()
    driver1.find_element_by_class_name("tl_list_iw_checkmark").click()
    driver1.find_element_by_class_name("tlid-source-text-input").send_keys("Hello, How Are You")
    time.sleep(3)
    driver1.quit()


if __name__ == '__main__':
    registration_screen()


if __name__ == '__main__':
    translate_screen()
