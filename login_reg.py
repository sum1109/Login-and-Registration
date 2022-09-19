# importing module and assigning special character and numbers.
import re
spec_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
num = re.compile('[0,1,2,3,4,5,6,7,8,9]')

# Defining class and, methods in the class for Email ID

class email_id:
  def __init__(self,input_assign):
    self.input_assign=input_assign
  
  def special_character_check(self):
    global res
    if(spec_char.search(self.input_assign[0]) == None):
      res=self.num_check()
      return res
    else:
      print("Your first character cannot be a special character")
      return False
     

    
  def num_check(self):
    if(num.search(self.input_assign) == None):
      print("Please add atleast one number !")
      return False
    else:
      if (num.search(self.input_assign[0]) == None):
        res=self.at_the_rate_check()
        return res
      else:
        print("Your first character cannot be a number")
        return False
       

  def at_the_rate_check(self):
    if re.search(r'@',self.input_assign) == None:
      print("@ missing !")
      return False
    else:
      if  re.search(r'@',self.input_assign).start() <= 0:
        print("You cannot assign '@' as the first character")
        return False
      else:
          res=self.dot_check()
          return res 
    


  def dot_check(self):
    if re.search(r'\.',self.input_assign) == None:
      print("'.' missing !")
      return False
    else:
        if re.search(r'@',self.input_assign).start() > re.search(r'\.',self.input_assign).start():
          print("You cannot assign '.' before '@'")
          return False
        else:
            if "@." in self.input_assign:
              print("You cannot assign '.' right after '@'")
              return False
            else:
                res=self.space1_check()
                return res


  def space1_check(self):
    global count1
    count1 = 0
    for i in self.input_assign:
      if (i.isspace()) == True:
        count1+=1
    
    if count1 > 0:
      print("Dont add spaces !")
      return False
    else:
      return True

# Defining class and, methods in the class for password 

class pass_word:
  def __init__(self,user_password):
    self.user_password = user_password

  def len_check(self):
    if 5 < len(self.user_password) < 16 :
      res_ult= self.spec_char_check()
      return res_ult
    else:
      print("Password too short !")
      return False
  
  def spec_char_check(self):
    if(spec_char.search(self.user_password) != None):
      res_ult = self.num_ber_check()
      return res_ult
    else:
      print("Please add a special character")
  
  def num_ber_check(self):
    if (num.search(self.user_password) != None):
      res_ult = self.case_check()
      return res_ult
    else:
      print("Please add a number")

  def case_check(self):
    count_upper =0
    count_lower = 0
    
    for i in self.user_password:
      if (i.isupper()) == True:
        count_upper += 1
      elif (i.islower()) == True:
        count_lower += 1
    
    if count_upper > 0:
      res_ult = self.space_check()
      return res_ult
    else:
      print("Add atleast one upper case value")
      return False
    
    if count_lower > 0:
      res_ult = self.space_check()
      return res_ult
    else:
      print("Add atleast one lower case value")
      return False

  def space_check(self):
    global count
    count = 0
    for i in self.user_password:
      if (i.isspace()) == True:
        count+=1
    
    if count > 0:
      print("Dont add spaces !")
      return False
    else:
      return True
 




# Defining functions for user

def forgot_pass(Id):
  global email_id_confirm
  email_id_confirm = False
  df2 = open("user_credentials_new.txt", "r")
  for i in df2:
        a, b = i.split(",")   
        b=b.strip()
        if a==Id:
          print("Your password is: ",b)
          email_id_confirm = True
        else:
          email_id_confirm = False

  if email_id_confirm == False:
    print("Email Id doesn't exist. Please register with us.")
  else:
    print("Hope we resolved your issue.")

  df2.close()


def log_in(name,password):
    #global validate_username
    validation = False
    df = open("user_credentials_new.txt", "r")
    for i in df:
        a, b = i.split(",")   
        b=b.strip()
        if a==name and b==password:
             validation = True
             break
        else:
          validation = False
    
    df.close()       
    if validation == True:
      print("Log In is Successful !!")
    else:
      print("The credentials entered are incorrect. Login unsuccessful !!")
      re_route = " "
      while re_route != "R" or re_route != "FP":
        re_route =input("Register or Forgot password (Enter R for Register and FP for forgot password) :")
        if re_route == "R":
          new_val = "register"
          access(new_val)
          break
        elif re_route == "FP":
          validate_username = input("Please enter your registered email Id: ")
          forgot_pass(validate_username)
          break
        else:
          print("Invalid response submitted !!. Please select R for Register or FP for forgot password")


def register(name, password):
    df = open("user_credentials_new.txt", "a")
    df.write(name + "," + password+"\n")
    df.close()
    print("Your credentials have been stored. You have successfully registered. Congratulations !!")
 

# Designing user interface

def access(option):
  global name
  global valid_result_email 
  global valid_pass_result

  if (option == "login"):
        name = input("Enter your Email Id: ")
        password = input("Enter your password: ")
        log_in(name, password)

  else:
    print("Welcome to registration")

    valid_result_email = False
    while valid_result_email != True:
      name = input("Create your Email Id: ")
      input_assign = email_id(name)
      valid_result_email = input_assign.special_character_check()

      if valid_result_email == True:
        print("Email entered fulfills the criteria. Email Id successfully created!. Lets create your password.")
        valid_pass_result =False
        while valid_pass_result != True:
            password = input("Please enter password: ")
            user_password = pass_word(password)
            valid_pass_result = user_password.len_check()

            if valid_pass_result ==True:
              print("Password entered fulfills the criteria.")
              register(name, password)
        
def begin():
    global option  
    print("Welcome!")
    option = input("login or register (Enter login or register): ")
    if(option != "login" and option != "register"):
      print("Invalid option!")
      begin()

 
#creating file
df = open("user_credentials_new.txt","a")
df.close()
# Initiating program
begin()
access(option)
#ctrl + m + i to exit any entry !

