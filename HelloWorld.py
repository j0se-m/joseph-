#string

#firstName = 'jose'
#surName = 'Majimaji'
#fullName = firstName.capitalize() + ' ' +  surName
#print(fullName)
#print(len(firstName))
#print(len(surName))
#print(firstName.endswith('e'))
#print(firstName.startswith('jo'))
#numbers
#addition= 2+6
#multiplication = 20 * 30
#mod = 10 % 6
#print(addition)
#print(multiplication)
#print(mod)
#boolean

#age = 12
#if age>=18:
    #print("is adult and is allowed to have an id")
#else:
       # print("is not adult and is not allowed to have a id")
       # is_Adult = False
       # if is_Adult:
         #   print("is adult")
        #else: 
          #  print("is not adult")
          #LISTS
#cars=['bmw','tesla', 'benz', 'toyota', 'honda']

#for car in cars:
  #  if car== 'tesla':
   #     print(car.upper())
    #else:
     #  print(car.capitalize())
     #WHILE
#num =0
#while num<=10:
  #  print(num)
   # num= num + 1
   #FUNCTIONS




def check_age(age):
  if age<18:
      print ("oops you are not an adult")
  else:
        print("hoorey you are an adult")
        check_age(18)
        check_age(99)
        check_age(17)
       
    
    