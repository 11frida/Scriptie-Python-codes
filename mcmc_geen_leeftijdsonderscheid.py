# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:42:35 2023

@author: frida
"""

from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy

#maximale waarden voor huishoudgrootte, totaal aantal besmette personen en aantal indexgevallen (waarden lopen van 0 tot en met 6)
max_hg=7
max_index=7
max_besmetting=7

#kansen: 3d matrix met [hg][index][besmetting], initialiseer met nullen
kansen=[[[0 for x in range(max_besmetting)] for y in range(max_index)] for z in range(max_hg)]

#kansen zonder indexgevallen
for k in range(max_hg):
    kansen[k][0][0]=1
for k in range(max_hg):
    for l in range(1,max_besmetting):
        kansen[k][0][l]=0
        
#kansen met huishoudgrootte 1        
kansen[1][1][1]=1
kansen[1][1][0]=0

#iteratieve kansen
p=sympy.symbols('p')
for hg in range(2,max_hg):
    for i in range(1,hg+1):
        for x in range(1,hg+1):
            for j in range(0,hg-i+1):
                kansen[hg][i][x]=kansen[hg][i][x]+(1-p**i)**j*(p**i)**(hg-i-j)*kansen[hg-i][j][x-i]*math.comb(hg-i,j)

#elke lijst in de data geeft: nummer van het huishouden,j1,j2,j3,a1,a2,a3,n1,n2,n3,c1,c2,c3,outbreak_start,outbreak_end,conditioning
#zie voor uitleg variabelen bijlage 6.1
data=[[1,0,0,0,0,0,1,2,2,1,0,0,0,102,115,0],
[3,0,0,0,0,0,1,3,1,1,0,0,0,114,162,0],
[5,0,0,0,0,1,1,0,0,1,0,0,0,113,224,0],
[7,0,0,0,0,1,0,0,1,2,0,0,0,121,191,0],
[13,0,0,0,0,0,1,0,1,1,0,0,0,161,174,0],
[24,0,0,0,0,1,0,1,0,2,0,0,0,88,112,0],
[27,0,2,0,0,0,2,1,2,0,0,0,0,92,160,0],
[37,0,0,1,0,0,1,0,3,1,0,0,0,217,231,0],
[49,0,1,0,0,1,2,0,2,0,0,0,0,225,249,0],
[58,0,0,0,0,0,1,1,1,1,0,0,0,213,306,0],
[61,0,0,0,0,0,2,0,2,0,0,0,0,133,160,0],
[62,0,0,0,0,0,1,0,1,0,0,0,0,239,310,0],
[63,0,0,0,0,1,0,1,1,1,0,0,0,108,133,0],
[80,0,0,2,0,1,0,0,0,2,0,0,0,230,255,0],
[85,0,0,0,0,1,0,1,1,2,0,0,0,296,309,0],
[86,0,0,0,1,0,0,0,3,2,0,0,0,285,298,0],
[92,0,0,0,0,1,1,0,2,1,0,0,0,198,213,0],
[105,2,0,0,1,0,0,2,0,2,0,0,0,63,77,0],
[116,0,0,0,0,0,2,1,0,0,0,0,0,99,129,0],
[117,0,0,0,0,0,1,1,0,2,0,0,0,34,47,0],
[123,2,0,1,0,0,1,2,0,1,0,0,0,165,219,0],
[125,0,0,1,0,0,1,2,0,1,0,0,0,50,64,0],
[127,0,0,0,1,0,0,0,0,2,0,0,0,50,63,0],
[136,1,0,0,1,0,0,1,0,2,0,0,0,219,240,0],
[138,0,0,0,1,0,0,1,0,2,0,0,0,284,297,0],
[139,0,0,0,0,0,1,2,0,1,0,0,0,92,156,0],
[145,0,0,1,2,0,1,0,0,1,0,0,0,212,251,0],
[152,0,0,1,0,0,1,2,0,1,0,0,0,112,170,0],
[157,0,0,0,0,0,1,2,0,1,0,0,0,53,72,0],
[159,0,0,0,0,0,1,2,0,1,0,0,0,182,196,0],
[163,2,0,1,0,0,1,2,0,1,0,0,0,110,136,0],
[171,0,0,1,1,0,1,0,0,1,0,0,0,126,152,0],
[173,0,0,0,0,0,1,1,0,1,0,0,0,102,123,0],
[174,2,0,1,0,0,1,2,0,1,0,0,0,133,152,0],
[176,1,0,0,0,0,2,1,0,0,0,0,0,52,66,0],
[184,0,0,0,3,0,1,0,0,1,0,0,0,64,77,0],
[191,0,0,0,1,0,0,0,0,2,0,0,0,58,71,0],
[196,0,0,0,1,0,0,1,0,2,0,0,0,189,224,0],
[200,0,0,1,1,0,1,1,0,1,0,0,0,108,213,0],
[203,2,0,0,0,0,2,2,0,0,0,0,0,188,230,0],
[210,2,0,2,1,0,0,2,0,2,0,0,0,205,231,0],
[217,1,0,0,1,0,2,1,0,0,0,0,0,225,248,0],
[224,1,0,2,1,0,0,2,0,2,0,0,0,188,231,0],
[228,0,0,0,0,0,1,2,0,1,0,0,0,210,227,0],
[231,0,0,0,0,0,1,1,0,1,0,0,0,227,266,0],
[245,0,0,0,1,0,0,0,0,3,0,0,0,108,138,0],
[253,0,0,1,1,0,0,2,0,2,0,0,0,294,308,0],
[254,0,0,0,0,0,1,2,0,1,0,0,0,197,271,0],
[257,0,0,0,0,0,1,1,0,1,0,0,0,112,133,0],
[273,0,0,0,0,0,1,1,0,1,0,0,0,150,250,0],
[280,1,0,2,1,0,0,1,0,2,0,0,0,205,238,0],
[286,0,0,0,0,0,1,3,0,1,0,0,0,203,264,0],
[287,0,0,0,0,0,1,2,0,1,0,0,0,135,163,0],
[289,0,0,0,0,0,1,1,0,0,0,0,0,140,172,0],
[293,0,0,0,0,0,1,2,0,1,0,0,0,256,281,0],
[298,0,0,0,0,0,1,2,0,1,0,0,0,154,175,0],
[299,2,0,2,1,0,0,2,0,2,0,0,0,275,304,0],
[300,0,0,0,0,0,1,2,0,1,0,0,0,184,221,0],
[304,0,0,0,0,0,1,1,0,1,0,0,0,184,313,0]]

kanslijst=[]
#bepaal voor elk huishouden de kans en voeg toe aan 'kanslijst'
for k in range(59):
    hg=data[k][4]+data[k][5]+data[k][6]+data[k][7]+data[k][8]+data[k][9] #huishoudgrootte
    i=data[k][4]+data[k][5]+data[k][6] #aantal indexgevallen
    x=data[k][1]+data[k][2]+data[k][3]+data[k][4]+data[k][5]+data[k][6] #totaal aantal besmettingen
    kans=kansen[hg][i][x]
    kanslijst.append(kans)
waarschijnlijkheid=math.prod([r for r in kanslijst]) #waarschijnlijkheid is product van alle kansen

def waarschijnlijkheidsfunctie(p_waarde): #geeft waarde van waarschijnlijkheidsfunctie in p_waarde
    waarschijnlijkheidswaarde=waarschijnlijkheid.subs(p,p_waarde)
    return waarschijnlijkheidswaarde

def posterior(p_waarde): #geeft waarde van posteriorfunctie in p_waarde
    prior= uniform.pdf(p_waarde)
    posterior=prior*waarschijnlijkheidsfunctie(p_waarde)
    return posterior

waarden=[]
waarde=0.5 #startwaarde voor p
waarden.append(waarde)
reject=0 #houdt bij hoe vaak er afgewezen wordt
kans=posterior(waarde)
waarschijnlijkheden=[]
for i in range(100000):
    nieuwe_waarde=waarde+np.random.normal(0,0.09) #reject met kans 0.66
    while nieuwe_waarde>1 or nieuwe_waarde<0: #zorgt dat nieuwe_waarde binnen [0,1] zit
        if nieuwe_waarde>1:
            nieuwe_waarde=2-nieuwe_waarde
        if nieuwe_waarde<0:
            nieuwe_waarde=-1*nieuwe_waarde
    nieuwe_kans=posterior(nieuwe_waarde)
    #bepaal of nieuwe_waarde geaccepteerd wordt:
    if nieuwe_kans>=kans:
        waarde=nieuwe_waarde
        kans=nieuwe_kans
    else: #nieuwe_waarde wordt niet geaccepteerd
        verhouding=nieuwe_kans/kans
        if np.random.rand()<verhouding: #kans op accepteren van verslechtering is verhouding
            waarde=nieuwe_waarde
            kans=nieuwe_kans
        else:
            waarde=waarde
            kans=kans
            reject=reject+1
    waarden.append(waarde)
    waarschijnlijk=waarschijnlijkheidsfunctie(waarde) #nodig voor plot maken van waarschijnlijkheidsfunctie
    waarschijnlijkheden.append(waarschijnlijk)
    if i%1000==0:
        print(i)

print(reject/100000)

#traceplot
plt.figure(figsize=(15,6),dpi=500)
iteratie=range(1,len(waarden)+1)
plt.scatter(iteratie,waarden,s=1,color='darkblue')
plt.title('Plot verloop waarden van p')
plt.xlabel('Iteratie')
plt.ylabel('p')
plt.show()

#waarschijnljkheid plot
plt.figure(figsize=(15,6),dpi=500)
iteratie=range(1,len(waarschijnlijkheden)+1)
plt.scatter(iteratie,waarschijnlijkheden, s=1, color='darkblue')
plt.title('Plot verloop waarschijnlijkheidsfunctie')
plt.xlabel('Iteratie')
plt.ylabel('Waarde waarschijnlijkheidsfunctie')
plt.show()

#waarschijnlijkheid plot eerste 2500 iteraties
plt.figure(figsize=(15,6),dpi=500)
waarschijnlijkheden=waarschijnlijkheden[0:2499]
iteratie=range(1,len(waarschijnlijkheden)+1)
plt.plot(iteratie,waarschijnlijkheden, linewidth=0.1, color='darkblue')
plt.title('Plot verloop waarschijnlijkheidsfunctie eerste 2500 iteraties')
plt.xlabel('Iteratie')
plt.ylabel('Waarde waarschijnlijkheidsfunctie')
plt.show()

#histogram
waarden=waarden[500:]
plt.hist(waarden,bins=100,edgecolor='black')
plt.title('Histogram van kansen p')
plt.xlabel('p')
plt.ylabel('Aantal')
plt.show()

#betrouwbaarheidsinterval
onder=np.percentile(waarden,2.5)
print(onder)
schatting=np.percentile(waarden,50)
print(schatting)
boven=np.percentile(waarden,97.5)
print(boven)
