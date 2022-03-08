import sys
import math
#zad1
a='Pierwszy '
b='program'
print(a+b)
c=43
d=21.5
suma=c+d
print(suma)
e=13+10j
print(e)

#zad2


# a=int(input('wpisz pierwsza liczbe '))
# b=int(input('wpisz druga liczbe '))
# print('suma jest rowna ',a+b)
# print('roznica jest rowna ',a-b)
# print('iloczyn jest rowny ',a*b)
# print('iloraz jest rowny ',a/b)
# print('dzielenie calkowite jest rowne ',a//b)
# print('reszta z dzielenia jest rowna ',a%b)
# print('potega a do b pierwszy sposob ',a**b)
# print('potega a do b drugi sposob ',pow(a,b))

#zad3

f=5
f+=6
print(f)
g=15
g-=5
print(g)
h=9
h*=5
print(h)
i=4
i/=2
print(i)
j=5
j**=4
print(j)
k=3
k%=2
print(k)

#zad4

l=math.exp(10)
print(l)
m=math.floor(3.55)
n=math.ceil(4.80)
print(m,n)
#zad5

imie='AREK'
nazwisko='NOWOSIAK'
print(imie.capitalize())
print(nazwisko.capitalize())

#zad6

piosenka='la la la'
print(piosenka.count('la'))

#zad7
tytul='terminator'
print(tytul[1],tytul[9])

#zad8

print(piosenka.split(' '))

#zad9

zmienna_a='jakis tekst'
zmienna_b=165.65
zmienna_c=88
print(str(zmienna_a))
print(float(zmienna_b))
print(hex(zmienna_c))
