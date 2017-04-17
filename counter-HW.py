
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


