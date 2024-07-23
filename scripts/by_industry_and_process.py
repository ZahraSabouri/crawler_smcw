from selenium import webdriver as _webdriver
from selenium.webdriver.common.by import By as _By
import scripts.by_industry_and_process_methods as _methods
import requests as _requests

## second tab : By Industry ⁄ Process
def by_industry_and_process(url, CHROME_WEBDRIVER_PATH, web_url):
    driver_cat_l1 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_fa_cat_l1 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)

    driver_cat_l2 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_fa_cat_l2 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)

    driver_prod_l1 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_fa_prod_l1 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)

    driver_features = _webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver\chromedriver.exe')

    driver_prod_l2 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
    driver_fa_prod_l2 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)



    driver_fa_cat_l1.get(_methods.translate_url(web_url=web_url))
    driver_fa_cat_l1.execute_script("window.scrollTo(0, 1000);")

    #click tab : Introduction of Products by Energy Saving ⁄ Applications ⁄ Industry
    driver_fa_cat_l1.find_element(_By.XPATH,"/html/body/div[2]/div[16]/div/label[2]/span").click()
    driver_cat_l1.get(web_url)
    driver_cat_l1.execute_script("window.scrollTo(0, 1000);")
    driver_cat_l1.find_element(_By.XPATH,"/html/body/div[2]/div[16]/div/label[2]/span").click()

    #cookies
    driver_cat_l1.find_element(_By.XPATH,"//div[text()='Close']").click()
    driver_fa_cat_l1.find_element(_By.XPATH,"//*[@id='s-modal_close']").click()


    for i in range(1, 12):
        #level1
        cat_id = _methods.categories_level1(i=i, driver=driver_cat_l1, url=url, driver_translate=driver_fa_cat_l1)

        cat_url_l2 = str(driver_cat_l1.find_element(_By.XPATH,"//*[@id='programming_content']/div/div[1]/ul/li["+ str(i) +"]/a").get_attribute('href'))
        driver_fa_cat_l2.get(_methods.translate_url(web_url=cat_url_l2))
        driver_cat_l2.get(cat_url_l2)

        if i == 1: #Equipment for Machine Tools
            for j in range(1,11):
                cat_id2 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)

                prod_url_l1 = str(driver_cat_l2.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]").get_attribute('href'))
                driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))
                driver_prod_l1.get(prod_url_l1)

                if j != 9:
                    k = 1
                    while True:
                        cat_temp = _methods.categories_level2(j=k, driver=driver_prod_l1, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_prod_l1)
                        cat_id3 = -1
                        if cat_temp == 0:
                            break
                        cat_id3 = cat_temp
                        k += 1
                if j == 5:
                    cat_id3 = _methods.categories_level3_type4(k=1, driver=driver_prod_l1, title="Air Cylanders", url=url, parent_id=cat_id2, level=3)
                    for k in range(1,8):
                        cat_id4 = _methods.categories_level3_type2(k=k, driver=driver_prod_l1, url=url, parent_id=cat_id3, level=4, map=1)

                    cat_id3 = _methods.categories_level3_type4(k=2, driver=driver_prod_l1, title="Electric Actuators", url=url, parent_id=cat_id2, level=3)
                    for k in range(1,10):
                        cat_id4 = _methods.categories_level3_type2(k=k, driver=driver_prod_l1, url=url, parent_id=cat_id3, level=4, map=2)

                if j == 9:
                    for k in range(1, 7):
                        products = _methods.products_level1_type2(k=k, driver=driver_prod_l1, url=url, cat_id=cat_id2, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                        product_id = products[1]
                        product_details_link = products[0]
                        if product_details_link != "":
                            driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                            driver_prod_l2.get(product_details_link)
                            l = 2
                            product_id2 = 0
                            product_temp = -1
                            while True:
                                product_temp = _methods.products_level2_type1(l=l, driver=driver_prod_l2, url=url, cat_id=cat_id2, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                if product_temp == 0:
                                    break
                                product_id2 = product_temp
                                l += 1
                    
        if i in [2, 10, 11]:
            _methods.products_general_type1(driver=driver_cat_l2, url=url, cat_id=cat_id, driver_translate=driver_fa_cat_l2)
        
        if i == 3:
            driver_cat_l3 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
            driver_fa_cat_l3 = _webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)            
            ##
            for j in range(2,4):
                cat_id2 = _methods.categories_level2_type2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
                cat_url_l3 = str(driver_cat_l2.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]").get_attribute('href'))
                driver_fa_cat_l3.get(_methods.translate_url(web_url=cat_url_l3))
                driver_cat_l3.get(cat_url_l3)
                
                cat_id3 = -1
                k = 1
                # driver_fa_cat_l3.find_element(_By.XPATH,"//*[@id='right']/a["+ str(k) +"]").click()
                # driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/a["+ str(k) +"]").click()
                while True:
                    cat_temp = _methods.categories_level3_type5(k=k, driver=driver_cat_l3, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l3)
                    if cat_temp == 0:
                        break
                    cat_id3 = cat_temp

                    driver_fa_cat_l3.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]").click()
                    driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]").click()

                    cat_id4 = -1
                    k2 = 3
                    while True:
                        try:
                            x_ = driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k2) +"]")
                        except:
                            break
                        try:
                            y = driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k2) +"]/ul/li/a")
                            l2 = 1
                            while True:
                                try:
                                    prod_url_l1 = str(driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k2) +"]/ul/li/a["+ str(l2) +"]").get_attribute('href'))
                                    cat_temp = _methods.categories_level4_type1(k=k2, l=l2, driver=driver_cat_l3, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_cat_l3)
                                    if cat_temp == 0:
                                        break
                                    cat_id4 = cat_temp

                                    l3 = 1 #tabs
                                    cat_id5 = cat_id4
                                    while True:
                                        driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))
                                        driver_prod_l1.get(prod_url_l1)
                                        try:
                                            new_prod_url_l1 = driver_prod_l1.find_element(_By.XPATH,"//*[@id='right']/ul/li["+ str(l3) +"]/a").get_attribute('href')
                                            cat_id5 = _methods.categories_level5_type1(l=l3, driver=driver_prod_l1, url=url, parent_id=cat_id4, level=5, driver_translate=driver_fa_prod_l1)
                                            driver_fa_prod_l1.get(_methods.translate_url(web_url=new_prod_url_l1))
                                            driver_prod_l1.get(new_prod_url_l1)

                                            product_id = -1
                                            m = 1
                                            while True:
                                                x = _methods.get_group(driver_prod_l1.current_url)
                                                products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id5, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                                prod_temp = products[1]
                                                product_details_link = products[0]
                                                
                                                if product_details_link != "":
                                                    product_id = prod_temp
                                                    driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                                    driver_prod_l2.get(product_details_link)
                                                    m2 = 2
                                                    product_id2 = 0
                                                    product_temp = -1
                                                    while True:
                                                        product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id5, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                                        if product_temp == 0:
                                                            break
                                                        product_id2 = product_temp
                                                        m2 += 1
                                                else:
                                                    break
                                                product_id = products[1]
                                                m += 1

                                        except:
                                            m = 1
                                            while True:
                                                x = _methods.get_group(driver_prod_l1.current_url)
                                                products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id5, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                                prod_temp = products[1]
                                                product_details_link = products[0]

                                                if product_details_link != "":
                                                    product_id = prod_temp
                                                    driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                                    driver_prod_l2.get(product_details_link)
                                                    m2 = 2
                                                    product_id2 = 0
                                                    product_temp = -1
                                                    while True:
                                                        product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id5, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                                        if product_temp == 0:
                                                            break
                                                        product_id2 = product_temp
                                                        m2 += 1
                                                else:
                                                    break
                                                product_id = products[1]
                                                m += 1
                                            break
                                        l3 += 1

                                except:
                                    break
                                l2 += 1
                        except:
                            print('passed : k2 = ' + str(k2))

                        k2+=1

                    k += 1

            ##
            for j in range(3, 12):
                cat_id2 = _methods.categories_level2_type3(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
                x = 2
                while True:
                    cat_id3 = _methods.categories_level3_type1(j=j, k=x, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
                    try:
                        prod_url_l1 = str(driver_cat_l2.find_element(_By.XPATH,"//*[@id='right']/div["+ str(j) +"]/ul/li["+ str(x) +"]/a").get_attribute('href'))
                        driver_prod_l1.get(prod_url_l1)
                        driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))

                        l3 = 1 #tabs
                        cat_id4 = cat_id3
                        while True:
                            driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))
                            driver_prod_l1.get(prod_url_l1)
                            try:
                                new_prod_url_l1 = driver_prod_l1.find_element(_By.XPATH,"//*[@id='right']/ul/li["+ str(l3) +"]/a").get_attribute('href')
                                cat_id5 = _methods.categories_level5_type1(l=l3, driver=driver_prod_l1, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_prod_l1)
                                driver_fa_prod_l1.get(_methods.translate_url(web_url=new_prod_url_l1))
                                driver_prod_l1.get(new_prod_url_l1)

                                product_id = -1
                                m = 1
                                while True:
                                    x = _methods.get_group(driver_prod_l1.current_url)
                                    products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id5, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                    prod_temp = products[1]
                                    product_details_link = products[0]
                                    
                                    if product_details_link != "":
                                        product_id = prod_temp
                                        driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                        driver_prod_l2.get(product_details_link)
                                        m2 = 2
                                        product_id2 = 0
                                        product_temp = -1
                                        while True:
                                            product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id5, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                            if product_temp == 0:
                                                break
                                            product_id2 = product_temp
                                            m2 += 1
                                    else:
                                        break
                                    product_id = products[1]
                                    m += 1

                            except:
                                m = 1
                                while True:
                                    x = _methods.get_group(driver_prod_l1.current_url)
                                    products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id5, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                    prod_temp = products[1]
                                    product_details_link = products[0]

                                    if product_details_link != "":
                                        product_id = prod_temp
                                        driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                        driver_prod_l2.get(product_details_link)
                                        m2 = 2
                                        product_id2 = 0
                                        product_temp = -1
                                        while True:
                                            product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id5, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                            if product_temp == 0:
                                                break
                                            product_id2 = product_temp
                                            m2 += 1
                                    else:
                                        break
                                    product_id = products[1]
                                    m += 1
                                break
                            l3 += 1
                    except:
                        break

                    if cat_id3 == 0:
                        break
                    x += 1
            ##
            for j in range(6,15):
                cat_id2 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
                cat_url_l3 = str(driver_cat_l2.find_element(_By.XPATH,"//*[@id='right']/a[" + str(j) +"]").get_attribute('href'))
                driver_cat_l3.get(cat_url_l3)
                driver_fa_cat_l3.get(_methods.translate_url(web_url=cat_url_l3))
                k = 1
                while True:
                    cat_temp = _methods.categories_level2(j=k, driver=driver_cat_l3, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
                    if cat_temp == 0:
                        break
                    cat_id3 = cat_temp

                    try:
                        prod_url_l1 = str(driver_cat_l3.find_element(_By.XPATH,"//*[@id='right']/a[" + str(k) +"]").get_attribute('href'))
                        driver_prod_l1.get(prod_url_l1)
                        driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))

                        l3 = 1 #tabs
                        cat_id4 = cat_id3
                        while True:
                            driver_fa_prod_l1.get(_methods.translate_url(web_url=prod_url_l1))
                            driver_prod_l1.get(prod_url_l1)
                            try:
                                new_prod_url_l1 = driver_prod_l1.find_element(_By.XPATH,"//*[@id='right']/ul/li["+ str(l3) +"]/a").get_attribute('href')
                                cat_id4 = _methods.categories_level5_type1(l=l3, driver=driver_prod_l1, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_prod_l1)
                                driver_fa_prod_l1.get(_methods.translate_url(web_url=new_prod_url_l1))
                                driver_prod_l1.get(new_prod_url_l1)

                                product_id = -1
                                m = 1
                                while True:
                                    x = _methods.get_group(driver_prod_l1.current_url)
                                    products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id4, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                    prod_temp = products[1]
                                    product_details_link = products[0]
                                    
                                    if product_details_link != "":
                                        product_id = prod_temp
                                        driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                        driver_prod_l2.get(product_details_link)
                                        m2 = 2
                                        product_id2 = 0
                                        product_temp = -1
                                        while True:
                                            product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id4, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                            if product_temp == 0:
                                                break
                                            product_id2 = product_temp
                                            m2 += 1
                                    else:
                                        break
                                    product_id = products[1]
                                    m += 1

                            except:
                                m = 1
                                while True:
                                    x = _methods.get_group(driver_prod_l1.current_url)
                                    products = _methods.products_level1_type2_x(x=x, k=m, driver=driver_prod_l1, url=url, cat_id=cat_id4, driver_translate=driver_fa_prod_l1, driver_features=driver_features)
                                    prod_temp = products[1]
                                    product_details_link = products[0]

                                    if product_details_link != "":
                                        product_id = prod_temp
                                        driver_fa_prod_l2.get(_methods.translate_url(web_url=product_details_link))
                                        driver_prod_l2.get(product_details_link)
                                        m2 = 2
                                        product_id2 = 0
                                        product_temp = -1
                                        while True:
                                            product_temp = _methods. products_level2_type1(l=m2, driver=driver_prod_l2, url=url, cat_id=cat_id4, parent_id=product_id, driver_translate=driver_fa_prod_l2)
                                            if product_temp == 0:
                                                break
                                            product_id2 = product_temp
                                            m2 += 1
                                    else:
                                        break
                                    product_id = products[1]
                                    m += 1
                                break
                            l3 += 1
                    except:
                        break

                    if cat_id3 == 0:
                        break

                    

                k += 1



        
        if i == 4:
            for j in range(1,7):
                cat_id2 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)

        if i == 5:
            ##
            cat_id2 = _methods.categories_level2_type4(driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
            ##
            for j in range(1,7):
                cat_id3 = _methods.categories_level3_type2(k=j, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, map=1)
            ##
            for j in range(1,8):
                cat_id2 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
            
        if i == 6:
            for j in range(1,13):
                cat_id2 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
        
        if i == 7:
            cat_id2 = _methods.categories_level2_type5(j=1, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
            cat_id3 = _methods.categories_level3_type3(k=1, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
            for j in range(1,8):
                cat_id4 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_cat_l2)
            cat_id3 = _methods.categories_level3_type3(k=2, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
            for j in range(8,15):
                cat_id4 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_cat_l2)

            # cat_url_l2 = str(driver_cat_l2.find_element(_By.XPATH,"//*[@id='right']/ul/li[2]/a").get_attribute("href"))
            # driver_fa_cat_l2.get(_methods.translate_url(web_url=cat_url_l2))
            # driver_cat_l2.get(cat_url_l2)

            cat_id2 = _methods.categories_level2_type5(j=2, driver=driver_cat_l2, url=url, parent_id=cat_id, level=2, driver_translate=driver_fa_cat_l2)
            cat_id3 = _methods.categories_level3_type3(k=1, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
            for j in range(1,9):
                cat_id4 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_cat_l2)
            cat_id3 = _methods.categories_level3_type3(k=2, driver=driver_cat_l2, url=url, parent_id=cat_id2, level=3, driver_translate=driver_fa_cat_l2)
            for j in range(9,14):
                cat_id4 = _methods.categories_level2(j=j, driver=driver_cat_l2, url=url, parent_id=cat_id3, level=4, driver_translate=driver_fa_cat_l2)
        
        if i == 8:
            titles = ["", "\"Compressed Air\" Line", "Piping Equipment (Fittings)", "Piping Equipment (Tubing)", "Pneumatic Instrumentation Equipment",\
                 "\"Industrial Water (Municipal Water)\" Line", "\"Inert Gas\"\" Clean Dry Air\" Line", "\"Deionized Water / Chemical Liquids\" Line", \
                    "  Air Preparation Equipment"]
            for j in range(1, 9):
                 cat_id2 = _methods.categories_level2_type6(j=j, title=titles[j], driver=driver_cat_l2,url=url, parent_id=cat_id, level=2)
            for j in range(4,6):
                product_id = _methods.products_general_type2(i=j, driver=driver_cat_l2, url=url, cat_id=cat_id, driver_translate=driver_fa_cat_l2)

        if i == 9:
            product_id = _methods.products_level1_type1(driver=driver_cat_l2, url=url, cat_id=cat_id, driver_translate=driver_fa_cat_l2)






    








    
