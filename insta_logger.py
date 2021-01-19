import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

username = input('Please enter your login\n')
password = input('Please enter your password\n')
hashtag = input('Please enter the hashtag you want to like\n')

sleep(2)

browser = webdriver.Firefox(executable_path="***(some dir with geckodriver)***/geckodriver.exe")
browser.get('http://instagram.com')

accept_button = browser.find_element_by_class_name("aOOlW ").click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

sleep(2)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(6)

username_input = browser.find_element_by_css_selector("button.yWX7d").click()

sleep(3)

username_input = browser.find_element_by_css_selector("button.aOOlW").click()

sleep(3)

if hashtag[0] == '#':
    username_input = browser.find_element_by_css_selector("input.XTCLo").send_keys(hashtag)
else:
    username_input = browser.find_element_by_css_selector("input.XTCLo").send_keys("#"+hashtag)

sleep(3)

username_input = browser.find_element_by_css_selector("div.z556c").click()

sleep(4)

username_input = browser.find_element_by_css_selector("div._9AhH0").click()

sleep(10)

username_input = browser.find_element_by_xpath('//span//button//div//span').click()

sleep(4)

username_input = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow").click()

browser.close() 
