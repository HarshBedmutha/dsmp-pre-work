# --------------
##File path for the file 
file_path 


#Code starts here
def read_file(path):
    file = open(file_path,'r')
    sentence = file.readline()
    file.close()
    return sentence
#   print(sentence)

sample_message = read_file(file_path)




# --------------
#Code starts here

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quot=(int(message_b)//int(message_a))
    
    #Returning the quotient in string format
    return str(quot)

#Calling the function to read file  
message_1=read_file(file_path_1)
print(message_1)
#Calling the function to read file
message_2=read_file(file_path_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)

#Code ends here


# --------------
#Code starts here
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    sub = ""
    if message_c == "Red":
        sub = "Army General"
    elif message_c == "Green":
        sub = "Data Scientist"  
    elif message_c == "Blue":
        sub = "Marine Biologist"    
    return sub

secret_msg_2 = substitute_msg(message_3)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)
    
def compare_msg(message_d,message_e):
    a_list = message_d.split()
    #print(a_list)
    b_list = message_e.split()
    #print(b_list)
    c_list = [element for element in a_list if element not in b_list]
    #print(c_list)
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4,message_5)




# --------------
#Code starts here
message_6 = read_file(file_path_6)
print(message_6)
def extract_msg(message_f):
    a_list = message_f.split()
    print(a_list)
    even_words = lambda x : (len(x)%2==0)
    b_list = list(filter(even_words,a_list))
    #print(b_list)
    final_msg = " ".join(b_list)
    return str(final_msg)

secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4,
 secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg =(secret_msg_3 +" "+ secret_msg_1+" " + secret_msg_4+" " + secret_msg_2)
#print(secret_msg)

def write_file(secret_msg,path):
    opened = open(path,"a+")
    opened.write(secret_msg)
    opened.close

write_file(secret_msg,final_path)
print(secret_msg)



