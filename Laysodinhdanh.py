from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.keys import Keys
import os, sys
import subprocess
import base64
import easyocr
import cv2


serials = subprocess.check_output('wmic diskdrive get SerialNumber').decode().split('\n')[1:]
EdwardSeri = serials[0]
Code = base64.b64encode(bytes(EdwardSeri, 'utf-8')).decode()

Codes = ['RTgyM184RkE2X0JGNTNfMDAwMV8wMDFCXzQ0NEFfNDY4QV8xNzczLiAgDQ0=', #Máy Laptop-Dell
		'NTAwMjZCNzM4MEExQTM4QSAgDQ0=', #Máy ECUS-SERVER
		'NTAwMjZCNzY4M0E3QjM0RiAgDQ0='] #Máy Tracy

if Code in (Codes):
	print('Đã được chấp nhận sử dụng chương trình bởi Edward - KEN LOGISITCS ')
else:
	input('Máy tính này không có quyền sử dụng tools'
		'\nVui lòng liên hệ với Edward - KEN LOGISTICS / SDT: 0988131586')
	exit()

print('-------------EDWARD - KEN LOGISITCS / 0988131586-------------Update: 11-Jan-2022-------------')
# mst = input("Nhập MST (Lưu ý pass = MST): ")
mst = '4601145670'
while len(mst) != 10:
	print('Mã số thuế chưa chính xác')
	print('Vui lòng nhập lại mã số thuế')
	mst = input("Nhập MST (Lưu ý pass = MST): ")

Check = 0
while Check == 0:
	nx = str(input('\nChọn loại hàng hóa cần lấy số định danh\n - Loại hàng nhập nhập "N"\n - Loại hàng xuất nhập "X"\n Vui lòng nhập lựa chọn: '))
	if nx.upper() == 'N' or nx.upper() == 'X':
		print('Lựa chọn lấy số định danh hàng nhập!')
		Check = 1
	else:
		print('Bạn nhập chưa đúng yêu cầu! Vui lòng nhập lại')

n = int(input("Nhập số lượng số định danh cần lấy: "))

if getattr(sys, 'frozen', False):
	dirname = os.path.dirname(sys.executable)
else:
	dirname = os.path.dirname(__file__)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
Edward = webdriver.Chrome(options=options)
Edward.maximize_window()
Edward.get("https://pus.customs.gov.vn/faces/Login")

#Vị trí ô Username trong trang web của Pus
print("Tên đăng nhập")
WAIT = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[2]/form/div/div[4]/div[1]/span/div[1]/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")))
username = Edward.find_element(By.XPATH,"/html/body/div[2]/form/div/div[4]/div[1]/span/div[1]/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")

#Điền Username
username.send_keys(mst)
#Vị trí ô Pass trong trang web của Pus
print("Điền mật khẩu")
passed = Edward.find_element(By.XPATH,"/html/body/div[2]/form/div/div[4]/div[1]/span/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")
#Điền pass
passed.send_keys(mst)
#Vị trí kiểu đăng nhập trong trang web của Pus (Sử dụng tài khoản hệ thống VNACCS/VCIS)

print("Chọn sử dụng tài khoản hệ thống VNACCS/VCIS")
Edward.find_element(By.ID,'pt1:rsoLoginType:_1').click()
#Captcha = input("Nếu bạn đã điền mã xác nhận để nhập thì nhấn ENTER để tiếp tục")

print("Vui lòng nhập mã xác nhận!")
input('Sau khi điền xong mã xác nhận vui lòng nhấn phím bất kỳ để tiếp tục: ')

print("Lưu mật khẩu")
Edward.find_element(By.XPATH,'/html/body/div[2]/form/div/div[4]/div[1]/span/div[1]/table/tbody/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/span/span/span/input').click()

print("Đăng nhập")
Edward.find_element(By.XPATH,'/html/body/div[2]/form/div/div[4]/div[1]/span/div[1]/table/tbody/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/span/span/span/input').send_keys(Keys.TAB,Keys.ENTER)
DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/form/div/div[4]/div[1]/div[1]/div/table/tbody/tr/td[1]/div/a/span")))
print("Đăng nhập thành công")

#Chọn mục định danh hàng hóa
try:
	print("Vào mục định danh hàng hóa")
	Edward.find_element(By.XPATH,'/html/body/div/form/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]/div/div').click()
except:
	print("Vào mục định danh hàng hóa")
	Edward.find_element(By.XPATH,'/html/body/div/form/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]/div/div').click()

try:
	print("Cấp mới")
	#Cấp mới số định danh
	DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/form/div/div[4]/div[1]/span/div[1]/div/div/table/tbody/tr/td[1]/div/a/span")))
	Edward.find_element(By.XPATH,'/html/body/div/form/div/div[4]/div[1]/span/div[1]/div/div/table/tbody/tr/td[1]/div').click()
except:
	print("Cấp mới")
	#Cấp mới số định danh
	DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/form/div/div[4]/div[1]/span/div[1]/div/div/table/tbody/tr/td[1]/div/a/span")))
	Edward.find_element(By.XPATH,'/html/body/div/form/div/div[4]/div[1]/span/div[1]/div/div/table/tbody/tr/td[1]/div').click()

try:
	DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/span")))
	print("Chọn loại hàng hóa: Nhập khẩu")
	if nx.upper() == "N":
		Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/select').send_keys(Keys.DOWN)
	elif nx.upper() == "X":
		Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/select').send_keys(Keys.DOWN,Keys.DOWN)
except:
	DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/span")))
	print("Chọn loại hàng hóa: Nhập khẩu")
	if nx.upper() == "N":
		Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/select').send_keys(Keys.DOWN)
	elif nx.upper() == "X":
		Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/select').send_keys(Keys.DOWN,Keys.DOWN)

try:
	print("Chọn đối tượng: DN XNK")
	Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/select').send_keys(Keys.DOWN)
except:
	print("Chọn đối tượng: DN XNK")
	Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/select').send_keys(Keys.DOWN)

print("MST DN xin cấp lại số định danh")
Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/input').send_keys(mst)

print("Cấp mới")
Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/a/span').click()

print("Chờ hệ thống cấp")
start_time = time.time()
Cho_cap_so_dinh_danh = WebDriverWait(Edward, 120).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/img")))
end_time = time.time()
tinhtime = str(round((end_time - start_time)))
print("Hệ thống mất: " + tinhtime + "s để cấp số định danh")
time.sleep(2)

WAIT = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="pt1:it11::content"]')))
SO_DINH_DANH = Edward.find_element(By.XPATH,'//*[@id="pt1:it11::content"]').text
print("Lấy số định danh thành công")
#Lấy số định danh ra file Text

file = open("Số định danh.txt","a")
file.write("\n" + SO_DINH_DANH)

print(SO_DINH_DANH)

print("Đóng")
Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[1]/div/a/span').click()

print("Chờ 5s")
print("Loading...")
for i in range(5,0,-1):
	print(i,end="...",flush='True')
	time.sleep(1)
print("Bắt đầu")

print("Tiếp tục lấy số định danh")
	#Lặp lại cấp số định danh
for i in range(n):
	WAIT = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="pt1:b1"]/a/span')))
	time.sleep(1)
	Edward.find_element(By.XPATH,'//*[@id="pt1:b1"]/a/span').click()
	DNTC = WebDriverWait(Edward, 30).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[2]/span")))

	print("Cấp mới")
	Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/span/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/a/span').click()
	start_time = time.time()
	Cho_cap_so_dinh_danh = WebDriverWait(Edward, 120).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/img")))
	time.sleep(2)
	end_time = time.time()
	tinhtime = str(round((end_time - start_time)))
	print("Hệ thống mất: " + tinhtime + "s để cấp số định danh")

	SO_DINH_DANH = Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[10]/table/tbody/tr/td[2]/span').text
	print("Đã lấy được số định danh thành công")

	file = open(dirname + "/Số định danh.txt","a")
	file.write("\n" + SO_DINH_DANH)
	
	print(SO_DINH_DANH)

	Edward.find_element(By.XPATH,'/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[1]/div/a/span').click()

print('--------------------------EDWARD - KEN LOGISITCS / 0988131586-----------------------------')
input('Hoàn thành!')
Edward.quit()
