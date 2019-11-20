第十一章  测试代码
page 103 - 108 

11.1 测试函数 
def get_formatted_name(first, last):
    full_name=first+" "+last
    return full_name.title()

	
from name_function import get_formatted_name

print("Enter 'q' at any time to quit")

while True:
    first=input("\nPlease give me a first name: ")

    if first=='q':
        break
    last=input("Please give me a last name: ")

    if last=='q':
        break

    formatted_name=get_formatted_name(first,last)
    print("\t Neatly formatted name: "+formatted_name+'.')

	
11.1.1 单元测试和测试用例

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	