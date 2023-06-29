import numpy as np 
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import requests

categoryOfProblem = ['easy', 'medium', 'hard']
# numberOfProblems = [662, 1419, 592] #easy, medium, hard

# def findDificulty(problemNumber):
    # options = Options()
    # options.add_argument("--disable-notifications")
    # options.add_argument("--headless")
    # driver = webdriver.Chrome('./chromedriver', chrome_options = options)
    # driver.get(f"https://leetcode.com/problemset/all/")#?search={problemNumber}&page=1")
    # driver.get(f"https://mapleroyals.com/?page=index")
    # ChromeDriverManager().install()
    # dificulty = [my_elem.text for my_elem in \
    #              WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located\
    #                  ((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[3]/div[2]/div[4]/span[1]")))]
    # dificulty = driver.find_element(By.XPATH, '//div[@class="LabeledButton_module_box__2bf466cb"]/label/span').text
    # driver.quit()
    # return dificulty

def pickProblem(n, week):
    print(f"Problems of the week ({week}): {np.random.randint(1, 2688, n)}")


# diff = findDificulty(208)
# print(diff)

pickProblem(3, '6/26')



