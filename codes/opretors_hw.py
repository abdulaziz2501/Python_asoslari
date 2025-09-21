#p-8

#st1 = "Hello"
#st2 = "world"
#print(len(st1)+len(st2))
#print(st1+" "+st2)

#p-9

#st1 = input("enter word1: ")
#st2 = input("enter word2: ")
#x = len(st1)/len(st2)
#print (x, type(x))

#p-10

#number = 12345
#count=0
#while number !=0:
#    count =count+number%10
#    number =int(number/10)
#print (count)
    
#p-11

#number = 1234567
#while number!=0:
#    print(number%10, end="")
#    number = number//10

#p-12

#start=1
#number=20
#while start<=20:
#    if start%2==0:
#        print(start)
#    start +=1

#p-13

#name="Mukhtor"
#age=20
#print(f"My name is {name} and I am {age} years old")

#p-14

#string="Bavariya"
#x=list(string)
#temp=x[0]
#x[0]=x[-1]
#x[-1]=temp
#print("".join(x))

#p-15

#test_str = "( )"
#print("The original string is : " + str(test_str))
#test=test_str.split()
#mid_str = "CAMBRIDGE"
#mid_pos = len(test) // 2
#test.insert(mid_pos,mid_str)
#print( "Formulated String : "+ str(" ".join(test)))

#p-16

#word ="bavariya"
#if len(word)%4==0:
#    print(word[0:4]+word[6:8]+word[4:6])

#p-17

#word = "lonely"
#print (word[0:1].upper()+word[1:5]+word[5:6].upper())

#p-18

#sense = "welcome to najot ta'lim. najot ta'lim awesome, isn't it?"
#res = sense.count("najot ta'lim")
#print ("najot ta'lim = " + str(res))

#p-19

#num1 = int(input("num1 kiriting: "))
#num2 = int(input("num2 kiriting: "))
#num3 = int(input("num3 kiriting: "))

#if num1>num2 and num1>num3:
#    print(num1)
#elif num2>num3 and num2>num1:
#    print(num2)
#elif num3>num1 and num3>num2:
#    print(num3)
#else:
#    print("sonlar teng")

#p-20

#word = "bavariya"
#res=word.count('a')
#print("a = " + str(res))

#p-21

#sense = "Hayot go'zal yashamoq zavqli"
#res = len(sense.split())
#print ("count: of sense: " + str(res))

#p-22

#name ="Lionel Messi"
#print(f"Men {name} man")

#p-23

#word = "bavariya"
#for i in range (len(word)):
#    if i%2==0:
#        print(word[i].upper(), end="")
#    else:
#        print(word[i].lower(), end="")

#p-24-7

#start = 1
#stop = 140
#while start<=stop:
#    if start%2==0:
#        print (start)
#    start+=1

#p-24-8

#start = 100
#stop = 240
#while start<=stop:
#    if start%2:
#        print (start)
#    start+=1

#p-25

"""
def summation(n):
    sum = 0
    j = 1
     
    for i in range(1, n + 1):
        sum = sum + j
        j = (j * 10) + 1
         
    return sum
         
n = 8
print(summation(n))
"""

"""
import math
 
def summation(n):
    return int((pow(10, n + 1) -
                    10 - (9 * n)) / 81);
 
print(summation(5));
"""




















































