import math
#1
print(math.exp(10))
print(pow(math.log(5+pow(math.sin(8),2)),(1/6)))
print(math.floor(3.55))
print(math.ceil(4.80))
#2
imie = 'BARTEK'
naz = 'ZALUSKA'
print(imie.capitalize())
print(naz.capitalize())
#3
piosenka = 'la gja la vkw ja ch la la la goas la coa la docv la emdf'
print(piosenka.count('la'))
#4
print(imie[0])
print(imie[5])
#6
string = 'abc def ghi'
float = 12.3
szestnastkowe = 0x123abc
print(string)
print(float)
print(hex(szestnastkowe))
#5
print(string.split(' '))
#7
sporty1 = ['karate','pilka_nozna']
sporty2 = ['koszylowka','siatkowka']
sporty1.reverse()
sporty1.extend(sporty2)
print(sporty1)
#8
skrot={'np':'na przyklad','itp':'i tym podobne','itd':'i tak dalej'}
#9
gry={'tf2':'team fortress 2','mc':'minecraft','eu4':'europa universalis 4','hoi4':'hearts of iron 4','ck2':'crusader kings 2'}
x = 0
for key, value in gry.items():
    x += 1
print(x)
#10
zdanie = input()
print(zdanie.count('a'))
#11
a = input()
b = input()
c = input()
if a>b:
    if a>c:
        print('a')
    elif c==a:
        print('c')
    else:
        print('przynajmniej 2 liczby posiadaja taka sama najwieksza wartosc')
elif b>c:
    print('b')
elif b==a:
    print('c')
else:
    print('przynajmniej 2 liczby posiadaja taka sama najwieksza wartosc')
#12
liczby = [1,2,3.4,5.6]
for i in liczby:
    print(i*i)
#13
lista=[]
y=0
while y < 10:
    z = input()
    z=int(z)
    y += 1
    reszta = z % 2
    if reszta == 0:
        lista.insert(y,z)
print(lista)