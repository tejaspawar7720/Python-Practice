#import os
#os.remove("just_test.txt")
#with open("practice.txt", "r") as j :
 #   data = j.read()
  #  new_data = data.replace("Java","Python")
#print(new_data)


#with open("practice.txt", "w") as j :
#    j.write(new_data)
d ="learing"
def to_check():
    with open("practice.txt", "r") as i:
        data = i.read()
        if d in data:
            print("It exist")
        else:
            print("Not here ")
    
def check_the_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as j:
        while data:
            data = j.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1 

check_the_line()
        