first = 8
second = 4
third = 6
if first == second and first == third:
        print(2)
elif second == first and first == third and second == third:
        print(3)
else:
        print(0)
first = 6
second = 4
third = 6
if first == second or first == third:
        print(2)
elif second == first or first == third or second == third:
        print(3)
else:
        print(0)
first = 8
second = 8
third = 8
if not first == second and first == third:
         print(2)
elif  first == second and first == third and second == third:
         print(3)
else:
         print(0)



