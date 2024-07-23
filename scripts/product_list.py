## first tab : Product List
from selenium import webdriver as _webdriver
from selenium.webdriver.common.by import By as _By
import scripts.product_list_methods as _methods

def product_list(url, CHROME_WEBDRIVER_PATH, web_url, driver):

    driver_fa = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_2 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_2_fa = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)


    driver.get(web_url)
    driver_fa.get(_methods.translate_url(web_url=web_url))

    #cookies
    driver.find_element(_By.XPATH,"//div[text()='Close']").click()
    driver_fa.find_element(_By.XPATH,"//*[@id='s-modal_close']").click()

    i = 1
    while True:
        #level1 :
        category_posted = _methods.categories_level1(i=i, driver=driver, url=url, driver_fa=driver_fa)
        if category_posted != 0:
            #level2 : 
            driver.find_element(_By.XPATH,"//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a").click()
            driver_fa.find_element(_By.XPATH,"//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a").click()
            j = 1
            while True:
                cat_id = _methods.categories_level2(j=j, driver=driver, url=url, parent_id=category_posted, driver_fa=driver_fa)
                if cat_id != 0:
                    # level 3 :
                    while True:
                        break_val = 0
                        try:
                            driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]").click()
                            driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]").click()
                            break_val = 1
                        except:
                            break_val = 0
                        if break_val == 1:
                            break
                    k = 1
                    while True:
                        product_list = _methods.products_level1(k=k, driver=driver, url=url, cat_id=cat_id, driver_fa=driver_fa, driver_features=driver_2)
                        try:
                            redirect_xpath = driver.find_element(_By.XPATH,product_list[0]+ str(k) +product_list[1])
                            redirect_url = str(redirect_xpath.get_attribute('href'))
                            driver_2.get(redirect_url)
                            driver_2_fa.get(_methods.translate_url(web_url=redirect_url))

                            l = 2
                            while True:
                                product_final = _methods.products_level2(l=l, driver_2=driver_2, url=url, cat_id=cat_id, parent_id=int(product_list[2]), driver_2_fa=driver_2_fa)
                                if product_final == 0:
                                    break
                                print("i : " + str(i) + ", j : " + str(j) + ", k : " + str(k) + ", l : " + str(l))
                                l += 1
                        except:
                            list_of_level3 = driver.find_elements(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div")
                            if k >= len(list_of_level3):
                                driver.back()
                                driver_fa.back()
                                break
                            
                        k+=1

                elif cat_id == 0:
                    driver.back()
                    driver_fa.back()
                    break
                j += 1
        elif category_posted == 0:
            break
        i += 1


            #! we excloded specialized products for general use