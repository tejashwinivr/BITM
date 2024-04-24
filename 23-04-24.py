'''test_string=input("enter the string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(zip(l,wordfreq))
print(dict(zip(l,wordfreq)))

my_dict={'apple':10,'banana':30,'angel':20,'balaji':40,'chennai':100,'cat':200}

for key,value in my_dict.items():
    if key[2].lower()=='l':
        print(f"the value of '{key}' is {value}")


#sum
a=[2,4,1,-3,-5,7]
sum1=sum2=sum3=0
for i in a:
    if i<0:
        sum1 += i
    elif i%2==0:
        sum2 += i
    else:
        sum3 += i
print("sum of negative numbers:",sum1)
print("sum of positive odd numbers:",sum2)
print("sum of positive even numbers:",sum3)
'''


a='''mango city-use single qts only inside double qts'''
print([word for word in a.split() if 's' in word])