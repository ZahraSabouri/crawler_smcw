from selenium.webdriver.common.by import By as _By
import requests as _requests
from translate import Translator as _Translator
import pandas as pd

translator= _Translator(to_lang="fa")

def translate_url(web_url):
    # return "https://translate.google.com/translate?sl=en&tl=fa&hl=en&u=" + web_url + "&client=webapp"
    fa_url = web_url.replace("https://www.smcworld.com/", "https://www-smcworld-com.translate.goog/")
    fa_url += "?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=en&_x_tr_pto=wapp"
    return fa_url

def categories_level1(i, driver, url, driver_fa):
    title_fa = ""
    # link_ = ""
    # image_link_ = ""

    try:
        link = driver.find_element(_By.XPATH,"//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a")

        image_link = driver.find_element(_By.XPATH,"//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a/dl/dt/p/img")

        text = str(driver.find_element(_By.XPATH,"//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a/dl/dd/span").get_attribute('innerHTML'))
    except:
        return 0
    try:
        i_path = str("//*[@id='all_content']/ul[1]/li["+ str(i) +"]/a/dl/dd/span/font/font")
        title_fa = str(driver_fa.find_element(_By.XPATH,i_path).text)
    except:
        pass

        
    new_record_category = {"level": 1,
                "parent_id": 0,
                "title" : text,
                "title_fa":  title_fa,
                "description": "",
                "description_fa": "",
                "link": str(link.get_attribute('href')),
                "image_link": str(image_link.get_attribute('src')),
                "category":  "Product List",
                "category_fa":  "لیست محصولات"
                }
    
    level_1_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_1_resp = level_1_req.json()
    print('level 1 category resp :', end='')
    print(level_1_resp)
    level_1_resp_id = int(level_1_resp['id'])
    return level_1_resp_id

def categories_level2(j, driver, url, parent_id, driver_fa):
    title_fa = ""

    try:
        sub_link = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]")
        sub_product_image_link = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]/img")
    except:
        return 0

    try:
        title_fa = str(driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]/img").get_attribute('alt'))
    except:
        pass

    description = ""
    try:
        description = str(driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]/ul").text)
    except:
        pass
    description_fa = ""
    try:
        description_fa = str(driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div[2]/a["+ str(j) +"]/ul").text)
    except:
        pass


    new_record_category = {"level": 2,
        "parent_id": parent_id,
        "title": str(sub_link.text),
        "title_fa":  title_fa,
        "description": description,
        "description_fa": description_fa,
        "link": str(sub_link.get_attribute('href')),
        "image_link": str(sub_product_image_link.get_attribute('src')),
        "category" :  "Product List",
        "category_fa":  "لیست محصولات"}
    level_2_req = _requests.post(url + "SMC_categories/", json=new_record_category)
    level_2_resp = level_2_req.json()
    cat_id = int(level_2_resp['id'])
    print('level 2 category resp :', end='')
    print(level_2_resp)
    # print(new_record_category)
    return cat_id

def products_level1(k, driver, url, cat_id, driver_fa, driver_features):
    title_fa = ""
    digital_catalog_ = ""
    catalogs_ = ""
    image_link_ = ""
    link_ = ""
    techdata_ = ""
    features = ""
    features_fa = ""
    title_ = ""
    description = ""
    description_fa = ""

    #1st try
    try:
        title = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/h2")
        title_ = str(title.get_attribute('innerHTML'))
        try:
            image_link = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[1]/img")
            image_link_ = str(image_link.get_attribute('src'))
        except:
            pass
    except:
        return ["", 0]
    try:
        k_path = str("//*[@id='content']/div[3]/div[3]/div["+str(k)+"]/h2/font/font")
        title_fa = str(driver_fa.find_element(_By.XPATH,k_path).text)
    except:
        pass


    try:
        features_link = str(driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        driver_features.get(features_link)


        features = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features = features.replace("href=\"", "href=\"https://www.smcworld.com")
        features = features.replace("src=\"", "src=\"https://www.smcworld.com")
        # features_fa = features_fa.replace("?_x_tr_sl=en&amp;_x_tr_tl=fa&amp;_x_tr_hl=en", "")
    except:
        pass
    
    try:
        features_link = str(driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[1]/a").get_attribute('href'))
        driver_features.get(features_link)


        features_fa = str(driver_features.find_element(_By.XPATH,"//*[@id='detail']").get_attribute("outerHTML"))
        features_fa = features_fa.replace("href=\"", "href=\"https://www.smcworld.com")
        features_fa = features_fa.replace("src=\"", "src=\"https://www.smcworld.com")
        features_fa = features_fa.replace("?_x_tr_sl=en&amp;_x_tr_tl=fa&amp;_x_tr_hl=en", "")
    except:
        pass

    try:
        technical_data_pdf = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[3]/a[3]")
        techdata_ = str(technical_data_pdf.get_attribute('href'))
    except:
        pass

    try:
        digital_catalog = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[2]/a")
        digital_catalog_ = str(digital_catalog.get_attribute('href'))
    except:
        pass
    try:
        catalogs = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[2]/ul[2]/li[3]/a")
        catalogs_ = str(catalogs.get_attribute('href'))
    except:
        pass

    try:
        description = str(driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
    except:
        pass
    try:
        description_fa = str(driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k) +"]/div[1]/div[2]/ul[1]").text)
        description_fa = description_fa.replace("<font style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("<font class=\"\" style=\"vertical-align: inherit;\">", "")
        description_fa = description_fa.replace("</font>", "")
    except:
        pass

    new_record_product = {
        "parent_id": 0,
        "title": str(title_),
        "title_fa": str(title_fa),
        "link": str(link_),
        "description": str(description),
        "description_fa": str(description_fa),
        "details_link": "",
        "digital_catalog": str(digital_catalog_),
        "catalogs" : str(catalogs_),
        "image_link": str(image_link_),
        "technical_data_pdf": str(techdata_),
        "features": str(features),
        "features_fa": str(features_fa)}

    level_3_req = _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)
    level_3_resp = level_3_req.json()
    # print(level_3_resp)
    print('level 1 product resp :', end='')
    print(level_3_resp)

    level_3_resp_id = int(level_3_resp['id'])
    product_id = level_3_resp_id

    ##here we add table of details #################################
    try:
        table = driver.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k)+"]/table").get_attribute("outerHTML")
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
        table = driver_fa.find_element(_By.XPATH,"//*[@id='content']/div[3]/div[3]/div["+ str(k)+"]/table").get_attribute("outerHTML")
        df = pd.read_html(table)
        header = df[0].columns.values.tolist()
        np_of_rows = df[0].to_numpy()
        for i in np_of_rows:
            for j in range(len(i)):
                new_record_details = {
                    "key": header[j],
                    "value": i[j]}
                details_req = _requests.post(url + "SMC_products/"+str(product_id)+"/SMC_details_table/", \
                json=new_record_details)
        details_resp = details_req.json()
        # print(details_resp)
        print('product details table resp :', end='')
        print(details_resp)
    except:
        print('passed detail : ' + str(k))
    
    return ["//*[@id='content']/div[3]/div[3]/div[","]/div[1]/div[2]/ul[2]/li[1]/a", level_3_resp_id]
    
        
def products_level2(l, driver_2, url, cat_id, parent_id, driver_2_fa):
    error_pram = 0
    image_link_ = ""
    details_ = ""
    title_fa = ""
    #1st try
    try:
        title = driver_2.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[2]")
        try:
            image_link = driver_2.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[1]/img")
            image_link_ = str(image_link.get_attribute('src'))
        except:
            pass
        try:
            details_link = driver_2.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[3]/a")
            details_ = str(details_link.get_attribute('href'))
        except:
            pass
        error_pram = 0
    except:
        error_pram = 1
    try:
        title_fa = str(driver_2_fa.find_element(_By.XPATH,"//*[@id='content']/table/tbody/tr["+ str(l) +"]/td[2]/font/font").text)
    except:
        pass

    if error_pram == 0:
        digital_catalog_ = ""
        catalogs_ = ""

        # try:
        #     title_fa = translator.translate(str(title.get_attribute('innerHTML')))
        # except:
        #     pass

        new_record_product = {
            "parent_id": parent_id,
            "title": str(title.get_attribute('innerHTML')),
            "title_fa": title_fa,
            "link": "",
            "description": "",
            "description_fa": "",
            "details_link": details_,
            "digital_catalog": digital_catalog_,
            "catalogs" : catalogs_,
            "image_link": image_link_, 
            "technical_data_pdf": "",
            "features": "",
            "features_fa": ""}

        level_4_req = _requests.post(url + "SMC_categories/"+ str(cat_id) +"/SMC_products/", json=new_record_product)
        level_4_resp = level_4_req.json()
        print('level 2 product resp :', end='')
        print(level_4_resp)
        # print(level_4_resp)
        # level_4_resp_id = int(level_4_resp['id'])

        return 1
    
    else :
        return 0

        

