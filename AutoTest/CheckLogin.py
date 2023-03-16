from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
from threading import Thread

# Hàm thực hiện các thao tác đăng nhập
def Login(driver,usr,pwd):
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[3]/form/div[1]/div/div/input").send_keys(usr)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[3]/form/div[2]/div/div/input").send_keys(pwd)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[3]/button").click()
    
# Hàm thực hiện các thao tác đăng xuất
def Logout(driver):
    driver.get("https://accounts.viblo.asia/logout?service=viblo")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/header/div/div[2]/div[3]/button/span").click()
    
# Hàm kiểm tra, xuất file
def OpenFile(driverOS,iput,oput):
    list_test = []
    # chọn trình duyệt
    driver = driverOS
    # mở link đăng nhập
    driver.get("https://accounts.viblo.asia/login?service=viblo&continue=https%3A%2F%2Fviblo.asia%2Fnewest")
    # Mở và kiểm tra file INPUT
    with open(iput) as f:
        reader = csv.reader(f)
        h = next(reader)
        for i in reader:
            usr,pwd = i[0].split(';')[:2]
            try:
                Login(driver,usr,pwd)
                sleep(2)
                print(f'{usr}/{pwd}: Fail')
                list_test += [i[0] + 'Fail']
                driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[3]/form/div[1]/div/div/input").clear()
                driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[3]/form/div[2]/div/div/input").clear()
            except:
                print(f'{usr}/{pwd}: Pass')
                list_test += [i[0] + 'Pass']
                sleep(2)
                Logout(driver)
                
    # Xuất ra file OUTPUT
    with open(oput,'w') as f:
        writer = csv.writer(f)
        writer.writerow(h)
        for row in list_test:
            writer.writerow([row])
    print('------------------------------------------------------')
    
# Hàm main         
def main():
    p1 = Thread(target = OpenFile, args=(webdriver.Chrome(),'INPUT1.csv','OUTPUT1.csv',))
    p2 = Thread(target = OpenFile, args=(webdriver.Safari(),'INPUT2.csv','OUTPUT2.csv',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Đã test xong! Dữ liệu được lưu vào file OUTPUT.csv')  
    
if __name__ == '__main__':
    main()






