numbers = [4, 7, 2, 9, 4, 1, 7, 8, 2, 4]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
        print("unique num= ",unique)
        print("\nfrequency of each no= ")
        for u in unique:
            count=0
            for n in numbers:
              if n == u :
                count+=1
                print(u,"appears",count,"times")
                largest=numbers[0]
                second_largest=numbers[0]
                for num in numbers:
                    if num>largest:
                        largest=num
                    elif num>second_largest and num!=largest:
                        second_largest=num
                        print("\nsecond largest= ",second_largest)
            
        