##counter = 0
##def my_calls_counter():
##     global counter
##     counter += 1
##     print (counter)
## 
##print ('=' * 60)
##print ("Funtion calls:")
##my_calls_counter()
##my_calls_counter()




def my_calls_counter():
     a = 0
     def count():
          nonlocal a
          print (a)
          a += 1
         
     return count


f = my_calls_counter()
f()
f()
f()
f()

##if __name__ == "__main__":
##     print("OK")
##else:
##     print("false")

