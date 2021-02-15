from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass

class Instagram:

    driver_path= "C:/Users/MONSTER/Desktop/instagram python/chromedriver.exe" #chrome driver path
    followerList,followingList=[],[]
    
    def __init__(self,username,password,follower,following):
        self.username = username
        self.password = password
        self.follower = follower
        self.following = following
        self.browser = webdriver.Chrome(Instagram.driver_path)

    def signIn(self):

        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        usernameTextBox = self.browser.find_element_by_name("username")
        passwordTextBox = self.browser.find_element_by_name("password")
        usernameTextBox.send_keys(username)
        passwordTextBox.send_keys(password)
        passwordTextBox.send_keys(Keys.ENTER)
        time.sleep(5)


    def getFollowers(self):

        self.browser.get(f"https://www.instagram.com/{username}/") #profile git
        time.sleep(2)
        self.browser.find_element_by_xpath("//section/main/div/header/section/ul/li[2]").click() #takipçi kutusunu göster
        time.sleep(2)

        modal = self.browser.find_element_by_css_selector("div[role=dialog] ul") #takipçi kutusunu tanımla
        count = len(modal.find_elements_by_tag_name("li"))
        
        action = webdriver.ActionChains(self.browser)
        while count < self.follower:
            modal.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            count = len(modal.find_elements_by_tag_name("li"))


        followers = self.browser.find_element_by_class_name("PZuss").find_elements_by_tag_name("li")
        for user in followers:
            link = str(user.find_element_by_tag_name("a").get_attribute("href"))
            link = link.split("/")
            self.followerList.append(link[3])
        

    def getFollowing(self):
        self.browser.get(f"https://www.instagram.com/{username}/") #go to profile
        time.sleep(2)

        self.browser.find_element_by_xpath("//section/main/div/header/section/ul/li[3]").click() #takip edilenler kutusunu göster
        time.sleep(2)

        modal = self.browser.find_element_by_css_selector("div[role=dialog] ul") #takip edilenler kutusunu tanımla
        count = len(modal.find_elements_by_tag_name("li"))
       
        
        action = webdriver.ActionChains(self.browser)
        while count < self.following:
            modal.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            count = len(modal.find_elements_by_tag_name("li"))


        followings = self.browser.find_element_by_class_name("PZuss").find_elements_by_tag_name("li") 

        for user in followings:
            link = str(user.find_element_by_tag_name("a").get_attribute("href"))
            link = link.split("/")
            self.followingList.append(link[3])


    def __del__(self):
        time.sleep(2)
        self.browser.close()

password2 = "xxxxxxx"
password = "xxxxxxxxxxx"
sayac = 0

username = input("Instagram kullanıcı adı : ")
while password != password2:
    password = getpass.getpass("Instagram şifresi : ")
    password2 = getpass.getpass("Instagram şifresi (Doğrulamak için) : ")
follower = int(input("Instagram takipçi sayısı : "))
following = int(input("Instagram takip edilen hesap sayısı : "))

app =Instagram(username,password,follower,following)

app.signIn()
app.getFollowers()
app.getFollowing()

for x in Instagram.followingList:
    if x not in Instagram.followerList:
        print(x)
        sayac += 1

print("**************")
print(f"{str(sayac)} kişi sizi takip etmiyor")