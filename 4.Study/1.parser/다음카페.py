# 다음 카페 목록에 접근하기 
# 크롬 실행하기 

from selenium import webdriver

driver = webdriver.Chrome('../python/chromedriver')
driver.implicitly_wait(3)

driver.get("http://top.cafe.daum.net/_c21_/my_cafe")

#다음에 로그인을 하고 카페 목록으로 이동 
driver = webdriver.Chrome('/Users/jw/python/chromedriver')
driver.implicitly_wait(3) # 3초 대기 

driver.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

#아이디와 비밀번호 입력받기 
username = input('아이디를 입력하세요')
userpw = input('비밀번호를 입력하세요')

#다음 로그인 페이지에아이디와 비밀번호 입력 
# driver.find_element_by_id('id').send_keys(username)
driver.find_element_by_xpath('//*[@id="id"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="inputPwd"]').send_keys(username)
#로그인버튼을 클릭 
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

# 여러 페이지를 이동할때는 중간에 자시 대기 시간을 주어야 할 필요가 있다. 
import time
time.sleep(3)#3초 대기 

# 카페 목록 페이지로 이동
driver.get("http://top.cafe.daum.net/_c21_/my_cafe")
time.sleep(3)
# 카페 목록 중에서 첫번째 페이지로 이동 
# driver.find_element_by_xpath(" ")

# 직접 카페로 이동 - 카페 글쓰기 페이지로 이동
driver.get('http://cafe.daum.net/samhak7/_memo')

#특정 프레임으로 이동
driver.switch_to_frame('down')

# # 프레임 확인
# frames = driver.find_elements_by_css_selector('iframe')
# for frame in frames : 
#     print(frame.get_attribute('name'))

#글작성 란에 텍스트를 입력
driver.find_element_by_xpath('//*[@id="memoForm"]/div/table/tbody/tr[1]/td[1]/div/textarea').send_keys('파이썬에서의 매크로ㅎㅇ')
driver.find_element_by_xpath('//*[@id="memoForm"]/div/table/tbody/tr[1]/td[2]/a[1]/span[2]').click()



