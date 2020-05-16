from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 
from login import userLogin
PATH = "D:\projects\ESL book\chromedriver1.exe"
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
# driver = webdriver.Chrome(PATH, options=op)
driver = webdriver.Chrome(PATH)
driver.get("https://northeastern.mywconline.net/")
#EC.presence_of_element_located((By.CLASS_NAME, "golinks"))



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
except:
    print("error.................")

userLogin(driver)

while(True):
    sch_list = driver.find_elements_by_class_name("golinks")
    if len(sch_list) == 0:
        userLogin(driver)
    tbodies = driver.find_elements_by_xpath("/html/body/div/div/table/tbody")


    prevW = False
    nextW = False
    for tbody in tbodies:
        d = tbody.find_element_by_class_name("sch_date")
        txt = d.text.split(":")[0]
        print(txt)

        target = "May 27"
        num = txt.split(" ")[1]
        tnum = target.split(" ")[1]
        if len(tnum) < len(num):
            nextW = True
        elif tnum > num:
            nextW = True
        else:
            prevW = True

        if txt == target:
            print("==========================")
            nextW = False
            prevW= False

            row2 = tbody.find_element_by_class_name("sch_row2")
            tds = row2.find_elements_by_tag_name('td')
            count = 0
            dir = ["sch_slots c_my", "sch_slots c_otNH", "sch_slots"]
            main_page = driver.current_window_handle
            for td in tds:
                print("==========================2")
                print(td.get_attribute("class"))
                if td.get_attribute("class") in dir:
                    count += 1
                    if td.get_attribute("class") == "sch_slots":
                        print("===================3")
                        prevWinNum = len(driver.window_handles)
                        print(prevWinNum)
                        td.click()
                        curWinNum = len(driver.window_handles)
                        print(curWinNum)
                        while curWinNum - prevWinNum < 1:
                            
                            td.click()
                            sleep(5)
                            curWinNum = len(driver.window_handles)
                            print(curWinNum)
                            
                        WebDriverWait(driver, 20)
                        for handle in driver.window_handles: 
                            if handle != main_page: 
                                book_page = handle
                                driver.switch_to.window(book_page)
                                close_btn = driver.find_element_by_name("submit")
                                print("close-------------------------------------")
                                close_btn.click() 
            break


    if nextW == True:
        print("next click!")
        driver.find_element_by_link_text('NEXT WEEK').click()

    if prevW == True:
        print("prev click!")
        driver.find_element_by_link_text('PREVIOUS WEEK').click()
    sleep(600)


