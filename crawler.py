from selenium import webdriver as _webdriver
import requests as _requests

import scripts.product_list as _pl
import scripts.by_industry_and_process as _ip
import credentials as _cr

_requests.delete(_cr.url + "delete_all/")

web_url = "https://www.smcworld.com/en-jp/"
driver = _webdriver.Chrome(executable_path=_cr.CHROME_WEBDRIVER_PATH)

_pl.product_list(_cr.url, _cr.CHROME_WEBDRIVER_PATH, web_url=web_url, driver=driver)

_ip.by_industry_and_process(_cr.url, _cr.CHROME_WEBDRIVER_PATH, web_url=web_url)