# bill = 2500
# discount = 150

# if bill >2000:
#     print('Bill is greater than 2000')
#     bill = bill-discount
# else:
#     print("bill is less than 2000")

# print("final bill is "  , bill)    

# grade=input("enter marks")

# grade = int(grade)

# if grade >=90:
#     print('A')
# elif grade>=80:
#     print('B')
# elif grade >=70:
#     print('C')
# elif grade >=60:
#     print('D')
# elif grade>= 50:
#     print('E')
# else:
#     print('F')            


# names =['GF','sam','sofia','Caro','Raph']

# for name in names:
#     print(name)

# message ="I LOVE GOD "

# for i in range(7):
#     print(message)


# cars =['toyota','subaru','BMW','benz','tiguan']
# car_i_want= input('type the car you want:')

# for car in cars:
#     if car == car_i_want:
#         print(f'car matched is {car_i_want}')
#         break
#     else:
#         print(f'sorry NO car matched available car are {cars} ')
    

# groups=[['rose','brenda'],['georg','GF']]

# for group in groups:
#     groups[0].append('sam')
#     for name in group:
#         print(name)

# nums=[1,2,3,4,5,6]
# square =[]

# for num in nums:
#     square.append(num * num)
#     print(square)

# nums=[1,2,3,4,5,6]
# square=[num*num for num in nums]
# print(square)

# groups=[['GF','sam','rose'],['george','mike','sofia']]
# for group in groups :
#     for name in group:
#       print(name)

#functions

# def add(a,b):
#     sum=a+b
#     return sum



# total= add(7,7)
# print(f'the total is :{total}'


#functions when number of arguments is unknown

# def add(*nums):
#     sum=0
#     for num in nums:
#         sum +=num
#         return sum
    
# print('total is :',add(2, 3, 4, 5))    


#enclosed functions

# def add(a,b):
#     sum = a+b
#     def double():
#         double= sum*2
#         double()
#         print(double)
#     return double


# print(add(2,7) )

#lambda functions

# add= lambda x:x+10
# print(add(7))


# 

# square=lambda num:num*num
# print(square(7))

# def large_power(base,exponent):
#     result=base**exponent

#     if result > 5000:
#         return True
#     else:
#         return False
    

# print(large_power(20,20))


# 

def calculate_dsicount(price,disount_percent):
    if disount_percent>=20:
        discount_amount=((disount_percent/100)*price)
        final_price=price-discount_amount
        return final_price
    else:
        return price
    


original_amount= float(input('input original amount'))
dicount_percent =float(input('input percent discount'))

final_amount=calculate_dsicount(original_amount,dicount_percent)

print(f'final price is {final_amount}')
    




