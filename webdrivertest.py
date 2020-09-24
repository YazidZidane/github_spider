from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
# driver.maximize_window()

#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

# # 鼠标悬停至“设置”链接
# driver.find_element_by_link_text('设置').click()
# sleep(1)
# # 打开搜索设置
# driver.find_element_by_link_text("搜索设置").click()
# sleep(2)
# driver.find_element_by_xpath('//[@id="se-setting-3"]/span[3]/label').click() 
# driver.find_element_by_xpath('//[@id="se-setting-7"]/a[2]').click()




# # 获得百度搜索窗口句柄
# sreach_windows = driver.current_window_handle

# driver.find_element_by_link_text('登录').click()
# time.sleep(1)
# driver.find_element_by_class_name("pass-reglink.pass-link").click()


# # 获得当前所有打开的窗口的句柄
# all_handles = driver.window_handles

# # 进入注册窗口
# for handle in all_handles:
#     if handle != sreach_windows:
#         driver.switch_to.window(handle)
#         print('now register window!')
#         time.sleep(2)
#         driver.find_element_by_name("TANGRAM__PSP_4__userName").send_keys('username')
#         driver.find_element_by_name('TANGRAM__PSP_4__password').send_keys('password')
#         time.sleep(2)
#         # ……



# print('Before search================')
# # 打印当前页面title
# title = driver.title
# print(title)

# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)

# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(10)

# print('After search================')

# # 再次打印当前页面title
# title = driver.title
# print(title)

# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)

# # 获取结果数目
# user = driver.find_element_by_class_name('nums').text
# print(user)


# # 定位到要悬停的元素
# above = driver.find_element_by_id("su")
# # 对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(above).perform()
# time.sleep(5)
# driver.find_element_by_id("su").click()



# # 获得输入框的尺寸
# size = driver.find_element_by_id('kw').size
# print(size)

# # 返回百度页面底部备案信息
# text = driver.find_element_by_class_name("lh").text
# print(text)

# # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
# attribute = driver.find_element_by_id("kw").get_attribute('type')
# print(attribute)

# # 返回元素的结果是否可见， 返回结果为 True 或 False
# result = driver.find_element_by_id("kw").is_displayed()
# print(result)



# #访问新闻页面
# second_url='http://news.baidu.com'
# print("now access %s" %(second_url))
# driver.get(second_url)

# #返回（后退）到百度首页
# print("back to  %s "%(first_url))
# driver.back()

# #前进到新闻页
# print("forward to  %s"%(second_url))
# driver.forward()

driver.quit()