from selenium import webdriver 
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

profile = FirefoxProfile("/home/patrick/.mozilla/firefox/kn62libz.default")
d = webdriver.Firefox(profile)
d.get("https://jobs.stahl-holding-saar-gruppe.de/bewerber/if_stellenboerse_formapply.php?prj=3181&b=5&oid=1&quelle=0&ie=1")
 
#------------------------------------------------------------------------------
#` predefined data
#` list_of_my_choices a list of possible choices I always choose
list_of_my_choices = ['herr','1993','ägypten']

#` find all comboboxes and fill them
#` @param driver a driver element
def fillComboboxes(driver):
    a = driver.find_elements_by_tag_name('select')
    for item in a:
        print(getComboboxOptions(item))
        chooseCombobox(item)
        
#------------------------------------------------------------------------------
#` extract options from combobox 
#' @param combobox a combobox element
#` @return a list of the options
def getComboboxOptions(combobox):
    o = combobox.find_elements_by_tag_name("option")
    i = []
    for item in o:
        i.append(item.text)
    return i

#------------------------------------------------------------------------------
#` select an item in a combobox
#` @param my_choice the item I choosed
#` @param combox a combobox element

def selectItemCombobox(combobox, my_choice = "herr"):
    combobox.click()
    o = combobox.find_elements_by_tag_name("option")
    for item in o:
        if item.text.lower == my_choice:
            item.
    combobox.send_keys(Keys.RETURN)
            
#------------------------------------------------------------------------------
#` make a choice from a combobox
#` @param combobox a combobox element
#` @param predefined list of my choices
#` @return a choice
def chooseCombobox(combobox, my_choices = list_of_my_choices,
                   birthmonth = '9', birthday = '21'):
    i = getComboboxOptions(combobox)
    # enter my birthday
    if '12' in i and '28' not in i:
        selectItemCombobox(combobox, birthmonth)
    if '25' in i and '28' in i:
        selectItemCombobox(combobox, birthday)
        
    for item in i:
        item = item.lower()
        print(item)
        if item in my_choices:
            selectItemCombobox(combobox, item)
    

    