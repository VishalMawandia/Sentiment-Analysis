from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
temp_len=-1

def flatten(arr):
	new_arr = []
	for x in arr:
		if type(x) == type([]):
			new_arr.extend(flatten(x))
		else:
			new_arr.append(x)
	return new_arr

f = open('data.csv','w')
f.write("Book_Name	Genre\n")
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.ranker.com/fact-lists/books/genre')
result=driver.find_element_by_id('listopedia__columns')
time.sleep(3)
result=result.find_elements_by_tag_name('a')
while(len(result) != temp_len):
	temp_len=len(result)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)
	result=driver.find_element_by_id('listopedia__columns')
	result=result.find_elements_by_tag_name('a')
Genre_list=[]
Edited_Genre_list=[]
Genre_links=[]
for x in result:
	Genre_links.append(x.get_attribute('href'))
	Genre_list.append(x.text)
#print(len(Genre_links))
#print(len(Genre_list))
for i in range(len(Genre_list)):
	Edited_Genre_list.append(Genre_list[i].replace('Famous ',''))
	
for i in range(len(Genre_links)):
	driver.get(Genre_links[i])
	class0=driver.find_element_by_id('list')
	class1=class0.find_elements_by_class_name('listItem__h2')
	class2=[ x.find_elements_by_class_name('listItem__data') for x in class1 ]
	class2=flatten(class2)
	class3=[ x.find_elements_by_class_name('listItem__title') for x in class2 ]
	class3=flatten(class3)
	for z in class3:
		f.write(z.text+'\t'+ str(i)+'\n')
driver.close()
f.close()