import os
#%% El primer ejercicio busca crear una función que encuentre la proporción de números positivos, negativos y ceros en una matriz dada:

def plusMinus(arr):
    positivos = 0
    negativos = 0
    ceros = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            ceros += 1
        elif arr[i] > 0:
            positivos += 1
        else:
            negativos += 1

    print(positivos / len(arr))
    print(negativos / len(arr))
    print(ceros / len(arr))



#%% sumar los 4 elementos menores y los 4 elementos mayores de una lista en python, los array son de 5 numeros

def miniMaxSum(arr):
    ordenatearr = sorted(arr)
    mini = sum(ordenatearr[:-1])
    maxi = sum(ordenatearr[1:])
    print(mini, maxi)



#%%  Given a time in -hour AM/PM format, convert it to military (24-hour) time. Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    print(ntime)
    return str(ntime[:-2])

#%%

def breakingRecords(scores):

    mayor = scores[0]
    menor = scores[0]
    conteomenores = 0
    conteomayores = 0
    for i in range(len(scores)):
        if scores[i] < menor:
            menor = scores[i]
            conteomenores += 1
        elif scores[i] > mayor:
            mayor = scores[i]
            conteomayores += 1
        else:
            pass
    return(conteomayores, conteomenores)


#%% The included code stub will read an integer, , from STDIN.Without using any string methods, try to print the following:
n = 0     #I don't remember what are n, but the solution is right

#Solution
for i in range(n):
    string = string + str(i + 1)
print(string)


#%% You are given two sets,  and . Your job is to find whether set  is a subset of set . If set  is subset of set , print True. If set  is not a subset of set , print False.

T = int(input())

for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))

#%% Calcule leap year =
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    return leap

#%% Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
x = int(input())
y = int(input())
z = int(input())
n = int(input())

arraylist = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k == n:
                pass
            else:
                arraylist.append([i,j,k])
print(arraylist)

#%% Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
maximo = max(arr)
segundo = min(arr)
for i in arr:
    if i > segundo and i < maximo:
        segundo = i
    else:
        pass
print(segundo)

#%%

scorelist = []
Result = []
if __name__ == '__main__':
    for _ in range(int(input())):
        Name = input()
        Score = float(input())
        Result += [[Name, Score]]
        scorelist += [Score]
    b = sorted(list(set(scorelist)))[1]
    for a, c in sorted(Result):
        if c == b:
            print(a)

#%% The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal


notas = student_marks[query_name]
promedio = float(sum(notas) / len(notas))
print("{:.2f}".format(promedio))   #se debe poner el format al print, sino HR toma la respuesta como erronea.

