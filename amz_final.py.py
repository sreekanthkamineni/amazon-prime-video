from bs4 import BeautifulSoup
from selenium import webdriver
# add URL here in URL folder
import urldata
# added credentials file
import az_log
# update any URL in url data file which is having list of movies
url1 = urldata.url_amz_in
# after page number we have to add this Url2
url2 = urldata.url_amz_1
page = 00
# chrome driver location
chromed = "c:\\Users\\sreek\\Documents\\PythonScripts\\chromedriver"
driver = webdriver.Chrome(chromed)
# calling amazon login program
az_log.amz_logon(driver)
mov_list = []
mov_list1 = []
# give max number pages available sections (for 50 pages give 50*20+ =1001)
while page < 981:
    url = url1 + str(page) + url2
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    amz_soup = BeautifulSoup(html, 'html.parser')
    mov_name = amz_soup.findAll('div', {'class': 'av-result-card-details-wrapper'})
    for buz in mov_name:
        name = buz.findAll('a', {'class': 'av-result-card-title'})[0].text
        # extract movie name
        print(name)
        link1 = (buz.a.attrs['href'])
        link2 = "https://www.primevideo.com"
        link_full = link2+link1
        # open movie link to extract director and language
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link_full)
        # extract director name
        try:
            sub2 = driver.find_element_by_xpath("/html/body/div[3]/section[1]/div[3]/dl[1]/dd/a")
            print(sub2.text)
            dir = sub2.text
        except:
            dir = ""
        # extract language
        try:
            lang = driver.find_element_by_xpath("/html/body/div[3]/section[1]/div[3]/dl[5]/dd")
            lang1 = (lang.text)
        except:
            try:
                lang = driver.find_element_by_xpath("/html/body/div[3]/section[1]/div[3]/dl[4]/dd")
                lang1 = (lang.text)
            except:
                try:
                    lang = driver.find_element_by_xpath(
                        "/html/body/div[3]/section[1]/div[3]/dl[3]/dd")
                    lang1 = (lang.text)
                except:
                    lang1 = ""
        # write details to text file, because non-en language code is not accepted in CVS
        with open("new.txt", "a", encoding='utf-8') as file:
            file.write(str(name)+";"+str(dir)+";"+str(lang1)+"\n")
        print("\n")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    # increase 20 t go to next page
    page += 20
# close webbrowser
driver.close()

exit()
