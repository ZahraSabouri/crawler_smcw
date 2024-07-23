from selenium.webdriver.common.by import By as _By
import requests as _requests
from translate import Translator as _Translator
import pandas as pd
import pyperclip as _clip

translator = _Translator(to_lang="fa") ######

def translate_url(web_url):
    # return "https://translate.google.com/translate?sl=en&tl=fa&hl=en&u=" + web_url + "&client=webapp"
    fa_url = web_url.replace("https://www.smcworld.com/", "https://www-smcworld-com.translate.goog/")
    fa_url += "?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=en&_x_tr_pto=wapp"
    return fa_url

def get_group(url):
    group_urls_2 = ["https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/misoperation/", 
    "https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/maintenance/valves.html",
    "smcworld.com/products/subject/en-jp/food/industry/beer/container/misoperation/"] 
    # , "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    group_urls_3 = ["https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/water/actuator.html",
    "https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/measures/flowcontrol.html",
    "smcworld.com/products/subject/en-jp/food/industry/beer/container/measures/flowcontrol.html", 
    "https://www.smcworld.com/products/subject/en-jp/food/industry/beer/washing/water/actuator.html", 
    "https://www.smcworld.com/products/subject/en-jp/food/theme/compliant/"] 
    # , "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    group_urls_4 = ["https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/measures/valves.html", 
    "https://www.smcworld.com/products/subject/en-jp/food/industry/beer/container/measures/valves.html"] 
    # , "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    group_urls_5 = ["https://www.smcworld.com/products/subject/en-jp/food/industry/beer/bfilling/drop/actuator.html",
    "https://www.smcworld.com/products/subject/en-jp/food/industry/beer/container/drop/actuator.html"] 
    # , "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    # group_urls_ = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    if url in group_urls_2:
        return 2
    if url in group_urls_3:
        return 3
    if url in group_urls_4:
        return 4
    if url in group_urls_5:
        return 5
    return 1



def categories_level1(i, driver, url, driver_translate):
    link_ = ""
    image_link_ = ""
    title_ = ""
    title_fa_ = ""

    try:
        link = driver.find_element(_By.XPATH,"//*[@id='programming_content']/div/div[1]/ul/li["+ str(i) +"]/a")
        image_link = driver.find_element(_By.XPATH,"//*[@id='programming_content']/div/div[1]/ul/li["+ str(i) +"]/a/dl/dt/p/img")
        title = driver.find_element(_By.XPATH,"//*[@id='programming_content']/div/div[1]/ul/li["+ str(i) +"]/a/dl/dd/span")

        link_ = str(link.get_attribute('href'))
        image_link_ = str(image_link.get_attribute('src'))
        title_ = str(title.get_attribute('innerHTML'))
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='programming_content']/div/div[1]/ul/li["+ str(i) +"]/a/dl/dd/span/font/font")
        title_fa_ = str(text_fa.get_attribute('innerHTML'))
    except:
        pass
    
    new_record_category = {"level": 1,
                "parent_id": 0,
                "title" : title_,
                "title_fa":  title_fa_,
                "description": "",
                "description_fa": "",
                "link": link_,
                "image_link": image_link_,
                "category":  r"By Industry / Process",
                "category_fa": r"بر اساس صنعت / فرآیند"
                }
    
    level_1_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_1_resp = level_1_req.json()
    # print(level_1_resp)
    level_1_resp_id = int(level_1_resp['id'])
    return level_1_resp_id

def categories_level2(j, driver, url, parent_id, level, driver_translate):
    link_ = ""
    image_link_ = ""
    title_ = ""
    title_fa_ = ""

    try:
        link = driver.find_element(_By.XPATH,"//*[@id='right']/a[" + str(j) +"]")
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]/img")

        title_ = str(image_link.get_attribute('alt'))
        link_ = str(link.get_attribute('href'))
        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]/img").get_attribute('alt')
        title_fa_ = str(text_fa)
    except:
        pass

    description = ""
    description_fa = ""
    if str(driver.current_url) == "https://www.smcworld.com/products/subject/en-jp/arc/":
        x = 2
        while True:
            try:
                description += str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]").get_attribute('outerHTML'))
                description_fa += str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]").get_attribute('outerHTML'))
            except:
                break
            x += 1
    # try:
    #     description_list = driver.find_elements(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]/ul")
    #     for item in description_list:
    #         if description_list[-1] == item:
    #             description = description + item.text
    #         else :
    #             description = description + item.text + " | "
    # except:
    #     pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": description,
        "description_fa": description_fa,
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level2_type2(j, driver, url, parent_id, level, driver_translate):
    link_ = ""
    image_link_ = ""
    title_ = ""
    title_fa_ = ""

    try:
        link = driver.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]")
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]/img")

        title_ = str(image_link.get_attribute('title'))
        link_ = str(link.get_attribute('href'))
        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]/img").get_attribute('title')
        title_fa_ = str(text_fa)
    except:
        pass

    description = ""

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": description,
        "description_fa": "",
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level2_type3(j, driver, url, parent_id, level, driver_translate):
    link_ = driver.current_url
    title_ = ""
    title_fa_ = ""

    try:
        title = driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(j) +"]/ul/li[1]")
        title_ = str(title.text)
    except:
        return 0

    try:
        title_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(j) +"]/ul/li[1]/font/font").text
        title_fa_ = str(title_fa)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])

    # print(new_record_category)
    return cat_id

def categories_level2_type4(driver, url, parent_id, level, driver_translate):
    link_ = driver.current_url
    image_link_ = ""
    title_ = ""
    title_fa_ = ""

    try:
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/div[2]/img")

        title_ = str(image_link.get_attribute('alt'))
        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/div[2]/img").get_attribute('alt')
        title_fa_ = str(text_fa)
    except:
        pass

    description = ""

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": description,
        "description_fa": "",
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level2_type5(j, driver, url, parent_id, level, driver_translate):
    link_ = driver.current_url
    image_link_ = ""
    title_ = ""
    title_fa_ = ""
    try:
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/div[1]/img")
        title = driver.find_element(_By.XPATH,"//*[@id='right']/ul/li[1]/a").text

        title_ = str(title)
        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/ul/li["+ str(j) +"]/a/font/font").text
        title_fa_ = str(text_fa)
    except:
        pass

    description = ""

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": description,
        "description_fa": "",
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level2_type6(j, title, driver, url, parent_id, level):
    link_ = ""
    image_link_ = ""
    try:
        title_fa_ = translator.translate(title)
    except:
        pass

    try:
        link = driver.find_element(_By.XPATH,"//*[@id='right']/a[" + str(j) +"]")
        link_ = str(link.get_attribute('href'))
    except:
        pass

    try:        
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/a["+ str(j) +"]/img")
        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title,
        "title_fa":  title_fa_,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level3_type1(j, k, driver, url, parent_id, level, driver_translate):
    link_ = ""
    title_ = ""
    title_fa_ = ""
    try:
        link = driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(j) +"]/ul/li["+ str(k) +"]/a")
        link_ = str(link.get_attribute('href'))
        title_ = str(link.text)
    except:
        return 0

    try:
        title_fa_ = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(j) +"]/ul/li["+ str(k) +"]/a/font/font").text)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_3_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_3_resp = level_3_req.json()
    cat_id = int(level_3_resp['id'])

    return cat_id

def categories_level3_type2(k, driver, url, parent_id, level, map): #, driver_translate):
    link_ = ""
    title_ = ""
    title_fa_ = ""
    try:
        if map == 1:
            link = driver.find_element(_By.XPATH,"//*[@id='Map']/area["+ str(k) +"]")
        else:
            link = driver.find_element(_By.XPATH,"//*[@id='Map2']/area["+ str(k) +"]")

        link_ = str(link.get_attribute('href'))
        title_ = str(link.get_attribute('alt'))
    except:
        return 0

    try:
        title_fa_ =  translator.translate(title_)
    except:
        title_fa_ = title_

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_3_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_3_resp = level_3_req.json()
    cat_id = int(level_3_resp['id'])

    return cat_id

def categories_level3_type3(k, driver, url, parent_id, level, driver_translate):
    link_ = driver.current_url
    title_ = ""
    title_fa_ = ""
    try:
        title = driver.find_element(_By.XPATH,"//*[@id='right']/h3["+ str(k) +"]").text
        title_ = str(title)
    except:
        return 0

    try:
        text_fa = driver_translate.find_element(_By.XPATH,"//*[@id='right']/h3["+ str(k) +"]/font/font").text
        title_fa_ = str(text_fa)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title_,
        "title_fa":  title_fa_,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_3_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_3_resp = level_3_req.json()
    cat_id = int(level_3_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level3_type4(k, driver, title, url, parent_id, level):
    link_ = driver.current_url
    image_link_ = ""
    title_fa = ""

    try:
        image_link = driver.find_element(_By.XPATH,"//*[@id='right']/img["+ str(k) +"]")

        image_link_ = str(image_link.get_attribute('src'))
    except:
        return 0

    try:
        text_fa = translator.translate(title)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title,
        "title_fa":  title_fa,
        "description": "",
        "description_fa": "",
        "link": link_,
        "image_link": image_link_,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_3_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_3_resp = level_3_req.json()
    cat_id = int(level_3_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level3_type5(k, driver, url, parent_id, level, driver_translate):
    link = ""
    title = ""
    title_fa = ""
    try:
        image_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]/img").get_attribute('src'))
    except:
        print('shit\n\n\nshitttttt')
        return 0
    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]/img").get_attribute('title'))
    except:
        pass
    try:
        link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]").get_attribute('href'))
    except:
        pass

    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div[1]/a["+ str(k) +"]/img").get_attribute('title'))
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title,
        "title_fa":  title_fa,
        "description": "",
        "description_fa": "",
        "link": link,
        "image_link": image_link,
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_3_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_3_resp = level_3_req.json()
    cat_id = int(level_3_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level4_type1(k, l, driver, url, parent_id, level, driver_translate):
    link = ""
    title = ""
    title_fa = ""
    

    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k) +"]/ul/li/a["+ str(l) +"]").text)
    except:
        return 0
    try:
        link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k) +"]/ul/li/a["+ str(l) +"]").get_attribute('href'))
    except:
        pass

    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(k) +"]/ul/li/a["+ str(l) +"]/font/font").text)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title,
        "title_fa":  title_fa,
        "description": "",
        "description_fa": "",
        "link": link,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_4_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_4_resp = level_4_req.json()
    cat_id = int(level_4_resp['id'])
    # print(new_record_category)
    return cat_id

def categories_level5_type1(l, driver, url, parent_id, level, driver_translate):
    link = ""
    title = ""
    title_fa = ""
    

    try:
        title = str(driver.find_elements(_By.XPATH,"//*[@id='right']/ul/li["+ str(l) +"]/a").text)
    except:
        return 0
    try:
        link = str(driver.find_elements(_By.XPATH,"//*[@id='right']/ul/li["+ str(l) +"]/a").get_attribute('href'))
    except:
        pass

    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/ul/li["+ str(l) +"]/a/font/font").text)
    except:
        pass

    new_record_category = {"level": level,
        "parent_id": parent_id,
        "title": title,
        "title_fa":  title_fa,
        "description": "",
        "description_fa": "",
        "link": link,
        "image_link": "",
        "category" :  r"By Industry / Process",
        "category_fa":  r"بر اساس صنعت / فرآیند"}
    level_4_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_4_resp = level_4_req.json()
    cat_id = int(level_4_resp['id'])
    # print(new_record_category)
    return cat_id


def products_general_type1(driver, url, cat_id, driver_translate):
    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/h3").text)
    except:
        title = ""
    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/h3/font/font").get_attribute('innerHTML'))
    except:
        title_fa = ""
    try:
        link = str(driver.current_url)
    except:
        link = ""
    try:
        description_list = driver.find_elements(_By.XPATH,"//*[@id='right']/div[2]/div[3]/ul")

        description = ""
        for item in description_list:
            description = description + item.text + " <hr> "
        description = description.replace(r"\n", " <hr> ")
    except:
        description = ""

    try:
        description_fa = ""
        x = 1
        while True:
            description_fa_list2 = driver_translate.find_elements(_By.XPATH, "//*[@id='right']/div[2]/div[3]/ul/li["+ str(x) +"]/font/font")
            if description_fa_list2 == []:
                break
            for item in description_fa_list2:
                description_fa = description_fa + str(item.text) + " <hr> "
            description_fa = description_fa.replace(r"\n", " <hr> ")
            x += 1

    except:
        description_fa = ""

    try:
        image_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[2]/div[2]/a[1]/img").get_attribute('src'))
    except:
        image_link = ""

    try:
        digital_catalog = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[2]/div[2]/a[2]").get_attribute('href'))
    except:
        digital_catalog = ""


    new_record_product = {
        "parent_id": 0,
        "title": title,
        "title_fa": title_fa,
        "link": link,
        "description": description,
        "description_fa": description_fa,
        "details_link": "",
        "digital_catalog": digital_catalog,
        "catalogs" : "",
        "image_link": image_link,
        "technical_data_pdf": "",
        "features": "",
        "features_fa": ""}
    
    _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)

def products_general_type2(i, driver, url, cat_id, driver_translate):
    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(i) +"]/div[1]/span").text)
    except:
        title = ""
    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(i) +"]/div[3]/a[1]").get_attribute('title'))
    except:
        title_fa = ""
    try:
        link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(i) +"]/div[3]/a[2]").get_attribute('href'))
    except:
        link = ""

    try:
        image_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(i) +"]/div[3]/a[1]/img").get_attribute('src'))
    except:
        image_link = ""


    new_record_product = {
        "parent_id": 0,
        "title": title,
        "title_fa": title_fa,
        "link": link,
        "description": "",
        "description_fa": "",
        "details_link": "",
        "digital_catalog": link,
        "catalogs" : "",
        "image_link": image_link,
        "technical_data_pdf": "",
        "features": "",
        "features_fa": ""}
    
    _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)

def products_level1_type1(driver, url, cat_id, driver_translate):
    link = driver.current_url
    title_ = ""
    try:
        title_ = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[2]/img").get_attribute("alt"))
    except:
        pass
    title_fa_ = ""
    try:
        title_fa_ = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div[2]/img").get_attribute("alt"))
    except:
        pass

    features = ""
    try:
        features += driver.find_element(_By.XPATH,"//*[@id='right']").get_attribute("outerHTML")
    except:
        pass
    features = features.replace("href=\"", "href=\"https://www.smcworld.com")
    features = features.replace("src=\"", "src=\"https://www.smcworld.com")
 
    features_fa = ""
    try:
        features_fa += driver_translate.find_element(_By.XPATH,"//*[@id='right']").get_attribute("outerHTML")
    except:
        pass
    features_fa = features_fa.replace("href=\"", "href=\"https://www.smcworld.com")
    features_fa = features_fa.replace("src=\"", "src=\"https://www.smcworld.com")
    features_fa = features_fa.replace("?_x_tr_sl=en&amp;_x_tr_tl=fa&amp;_x_tr_hl=en", "")


    new_record_product = {
        "parent_id": 0,
        "title": title_,
        "title_fa": title_fa_,
        "link": link,
        "description": "",
        "description_fa": "",
        "details_link": "",
        "digital_catalog": link,
        "catalogs" : "",
        "image_link": "",
        "technical_data_pdf": "",
        "features": features,
        "features_fa": features_fa}
    
    _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)


def products_level1_type2_x(k, driver, url, cat_id, driver_translate, driver_features, x):
    title = ""
    title_fa = ""
    description = ""
    description_fa = ""
    image_link = ""
    link = ""
    digital_catalog = ""
    catalogs = ""
    techdata = ""
    features = ""
    features_fa = ""

    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/h2").text)
    except:
        return ["", 0]
    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/h2/font/font").text)
    except:
        pass

    try:        
        image_link =  str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[1]/img").get_attribute('src'))
    except:
        pass
    try:
        link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
    except:
        pass
    try:
        description = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
    except:
        pass
    try:
        description_fa = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
        description_fa = description_fa.replace("<font style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("<font class=\"\" style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("</font>", "")
    except:
        pass
    try:
        digital_catalog = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[2]/a").get_attribute('href'))
    except:
        pass
    try:
        catalogs = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[3]/a").get_attribute('href'))
    except:
        pass
    try:
        techdata = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[3]/a[4]").get_attribute('href'))
    except:
        pass

    try:
        features_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        driver_features.get(features_link)

        features = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features = features.replace("href=\"", "href=\"https://www.smcworld.com")
        features = features.replace("src=\"", "src=\"https://www.smcworld.com")
    except:
        pass

    try:
        features_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        features_link_translated = translate_url(web_url=features_link)
        driver_features.get(features_link_translated)

        features_fa = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features_fa = features_fa.replace("href=\"", "href=\"https://www.smcworld.com")
        features_fa = features_fa.replace("src=\"", "src=\"https://www.smcworld.com")
        features_fa = features_fa.replace("?_x_tr_sl=en&amp;_x_tr_tl=fa&amp;_x_tr_hl=en", "")
    except:
        pass

    new_record_product = {
        "parent_id": 0,
        "title": title,
        "title_fa": title_fa,
        "link": link,
        "description": description,
        "description_fa": description_fa,
        "details_link": "",
        "digital_catalog": digital_catalog,
        "catalogs" : catalogs,
        "image_link": image_link,
        "technical_data_pdf": techdata,
        "features": features,
        "features_fa": features_fa}

    level_1_req = _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)
    level_1_resp = level_1_req.json()
    # print(level_1_resp)
    level_1_resp_id = int(level_1_resp['id'])
    product_id = level_1_resp_id

    ##here we add table of details #################################
    try:
        table = driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k)+"]/table").get_attribute("outerHTML")
        df = pd.read_html(table)
        header = df[0].columns.values.tolist()
        np_of_rows = df[0].to_numpy()
        for i in np_of_rows:
            for j in range(len(i)):
                new_record_details = {
                    "key": header[j],
                    "value": i[j]}
                # details_req = 
                _requests.post(url + "SMC_products/"+str(product_id)+"/SMC_details_table/", \
                json=new_record_details)
        # details_resp = details_req.json()
        # print(details_resp)
    except:
        print('passed detail : ' + str(k))
    try:
        table = driver_translate.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k)+"]/table").get_attribute("outerHTML")
        df = pd.read_html(table)
        header = df[0].columns.values.tolist()
        np_of_rows = df[0].to_numpy()
        for i in np_of_rows:
            for j in range(len(i)):
                new_record_details = {
                    "key": header[j],
                    "value": i[j]}
                # details_req = 
                _requests.post(url + "SMC_products/"+str(product_id)+"/SMC_details_table/", \
                json=new_record_details)
        # details_resp = details_req.json()
        # print(details_resp)
    except:
        print('passed detail : ' + str(k))

    product_num_check = ""
    try:
        product_num_check = str(driver.find_element(_By.XPATH,"//*[@id='right']/div["+ str(x) +"]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[1]/a").get_attribute("href"))
    except:
        pass
    return [product_num_check, level_1_resp_id]


def products_level1_type3(k, driver, url, cat_id, driver_translate, driver_features):
    title = ""
    title_fa = ""
    description = ""
    description_fa = ""
    image_link = ""
    link = ""
    digital_catalog = ""
    catalogs = ""
    techdata = ""
    features = ""
    features_fa = ""

    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[1]/div["+ str(k) +"]/h2").text)
    except:
        return ["", 0]
    try:
        title_fa = str(driver_translate.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/h2/font/font").text)
    except:
        pass

    try:        
        image_link =  str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[1]/img").get_attribute('src'))
    except:
        pass
    try:
        link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
    except:
        pass
    try:
        description = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
    except:
        pass
    try:
        description_fa = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
        description_fa = description_fa.replace("<font style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("<font class=\"\" style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("</font>", "")
    except:
        pass
    try:
        digital_catalog = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[2]/a").get_attribute('href'))
    except:
        pass
    try:
        catalogs = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[3]/a").get_attribute('href'))
    except:
        pass
    try:
        techdata = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[3]/a[4]").get_attribute('href'))
    except:
        pass

    try:
        features_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        driver_features.get(features_link)

        features = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features = features.replace("href=\"", "href=\"https://www.smcworld.com")
        features = features.replace("src=\"", "src=\"https://www.smcworld.com")
    except:
        pass

    try:
        features_link = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        features_link_translated = translate_url(web_url=features_link)
        driver_features.get(features_link_translated)

        features_fa = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features_fa = features_fa.replace("href=\"", "href=\"https://www.smcworld.com")
        features_fa = features_fa.replace("src=\"", "src=\"https://www.smcworld.com")
        features_fa = features_fa.replace("?_x_tr_sl=en&amp;_x_tr_tl=fa&amp;_x_tr_hl=en", "")
    except:
        pass

    new_record_product = {
        "parent_id": 0,
        "title": title,
        "title_fa": title_fa,
        "link": link,
        "description": description,
        "description_fa": description_fa,
        "details_link": "",
        "digital_catalog": digital_catalog,
        "catalogs" : catalogs,
        "image_link": image_link,
        "technical_data_pdf": techdata,
        "features": features,
        "features_fa": features_fa}

    level_1_req = _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)
    level_1_resp = level_1_req.json()
    # print(level_1_resp)
    level_1_resp_id = int(level_1_resp['id'])
    product_id = level_1_resp_id

    ##here we add table of details #################################
    try:
        table = driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k)+"]/table").get_attribute("outerHTML")
        df = pd.read_html(table)
        header = df[0].columns.values.tolist()
        np_of_rows = df[0].to_numpy()
        for i in np_of_rows:
            for j in range(len(i)):
                new_record_details = {
                    "key": header[j],
                    "value": i[j]}
                # details_req = 
                _requests.post(url + "SMC_products/"+str(product_id)+"/SMC_details_table/", \
                json=new_record_details)
        # details_resp = details_req.json()
        # print(details_resp)
    except:
        print('passed detail : ' + str(k))
    try:
        table = driver_translate.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k)+"]/table").get_attribute("outerHTML")
        df = pd.read_html(table)
        header = df[0].columns.values.tolist()
        np_of_rows = df[0].to_numpy()
        for i in np_of_rows:
            for j in range(len(i)):
                new_record_details = {
                    "key": header[j],
                    "value": i[j]}
                # details_req = 
                _requests.post(url + "SMC_products/"+str(product_id)+"/SMC_details_table/", \
                json=new_record_details)
        # details_resp = details_req.json()
        # print(details_resp)
    except:
        print('passed detail : ' + str(k))

    product_num_check = ""
    try:
        product_num_check = str(driver.find_element(_By.XPATH,"//*[@id='right']/div[6]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[1]/a").get_attribute("href"))
    except:
        pass
    return [product_num_check, level_1_resp_id]
        
def products_level2_type1(l, driver, url, cat_id, parent_id, driver_translate):
    image_link = ""
    details_link = ""
    title_fa = ""
    try:
        title = str(driver.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[2]").text)
    except:
        return 0
    try:
        title_fa = str(driver.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[2]/font/font").text)
    except:
        pass
    try:
        image_link =  str(driver.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[1]/img").get_attribute('src'))
    except:
        pass
    try:
        details_link = str(driver.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[3]/a").get_attribute('href'))
    except:
        pass

    new_record_product = {
        "parent_id": parent_id,
        "title": title,
        "title_fa": title_fa,
        "link": "",
        "description": "",
        "description_fa": "",
        "details_link": details_link,
        "digital_catalog": "",
        "catalogs" : "",
        "image_link": image_link, 
        "technical_data_pdf": "",
        "features": "",
        "features_fa": ""}

    level_2_req = _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)
    level_2_resp = level_2_req.json()
    # print(level_2_resp)
    level_2_resp_id = int(level_2_resp['id'])

    return level_2_resp_id