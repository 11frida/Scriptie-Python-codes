# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:10:23 2024

@author: frida
"""

from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy
import random

#maximale waarden voor huishoudgrootte, totaal aantal besmette personen en aantal indexgevallen voor kinderen en volwassenen (waarden lopen van 0 tot en met 6)
max_hg_kind=7
max_index_kind=7
max_besmetting_kind=7
max_hg_volw=7
max_index_volw=7
max_besmetting_volw=7
                                          
#kansen: 6d matrix met [hg_kind][hg_volw][index_kind][index_volw][besmetting_kind][besmetting_volw], initialiseer met nullen
kansen=[[[[[[0 for x_2 in range(max_besmetting_volw)] for x_1 in range(max_besmetting_kind)] for y_2 in range(max_index_volw)] for y_1 in range(max_index_kind)] for z_2 in range(max_hg_volw)] for z_1 in range(max_hg_kind)]
p_1 = sympy.symbols('p_1') #kans dat kind kind niet besmet
p_2 = sympy.symbols('p_2') #kind besmet volwasse niet
p_3 = sympy.symbols('p_3') #volw kind
p_4 = sympy.symbols('p_4') #volw volw

#kans is 1 bij geen index en geen besmettingen
for k in range(max_hg_kind):
    for l in range(max_hg_volw):
        kansen[k][l][0][0][0][0]=1
        
#kans is 0 bij geen index en wel besmettingen
for k in range(max_hg_kind):
    for l in range(max_hg_volw):
        for m in range(1,max_besmetting_kind):
            for n in range(1, max_besmetting_volw):
                kansen[k][l][0][0][m][n]=0 

#kansen met max huishoudgrootte 1
kansen[1][0][1][0][1][0]=1
kansen[1][0][1][0][0][0]=0
kansen[0][1][0][1][0][1]=1
kansen[0][1][0][1][0][0]=0

#iteratieve kansen
for hg_kind in range(0,max_hg_volw):
     for hg_volw in range(0,max_hg_volw):
         if hg_kind+hg_volw>1: #voor huishoudgrootte 1 zijn de kansen al bepaald
             for i_1 in range(0,hg_kind+1):
                 for i_2 in range(0,hg_volw+1):
                     if i_1+i_2>0: #voor geen indexgevallen zijn de kansen al bepaald
                         for x_1 in range(i_1,hg_kind+1):
                             for x_2 in range(i_2,hg_volw+1):
                                 for j_1 in range(0,hg_kind-i_1+1): #aantal kinderen besmet in 1e generatie
                                     for j_2 in range(0,hg_volw-i_2+1): #aantal volwassenen besmet in de 1e generatie
                                         kans_kind_niet_besmet=p_1**i_1*p_3**i_2
                                         kans_volw_niet_besmet=p_2**i_1*p_4**i_2
                                         kansen[hg_kind][hg_volw][i_1][i_2][x_1][x_2]=kansen[hg_kind][hg_volw][i_1][i_2][x_1][x_2]+math.comb(hg_kind-i_1,j_1)*kans_kind_niet_besmet**(hg_kind-i_1-j_1)*(1-kans_kind_niet_besmet)**j_1*\
                                         math.comb(hg_volw-i_2,j_2)*kans_volw_niet_besmet**(hg_volw-i_2-j_2)*(1-kans_volw_niet_besmet)**j_2*kansen[hg_kind-i_1][hg_volw-i_2][j_1][j_2][x_1-i_1][x_2-i_2]
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
    hg_kind=data[k][4]+data[k][5]+data[k][7]+data[k][8] #huishoudgrootte kind
    hg_volw=data[k][6]+data[k][9] #huishoudgrootte volwassenen
    i_kind=data[k][4]+data[k][5]#aantal indexgevallen kind
    i_volw=data[k][6] #aantal indexgevallen volwassenen
    x_kind=data[k][1]+data[k][2]+data[k][4]+data[k][5] #totaal aantal besmettingen kind
    x_volw=data[k][3]+data[k][6] #totaal aantal besmettingen kind
    kans=kansen[hg_kind][hg_volw][i_kind][i_volw][x_kind][x_volw]
    kanslijst.append(kans)
waarschijnlijkheid=math.prod([r for r in kanslijst])

def waarschijnlijkheidsfunctie(p_1waarde,p_2waarde,p_3waarde,p_4waarde): #geeft waarde van waarschijnlijkheidsfunctie in (p_1waarde,p_2waarde,p_3waarde,p_4waarde)
    waarschijnlijkheidswaarde=waarschijnlijkheid.subs({p_1:p_1waarde, p_2:p_2waarde,p_3:p_3waarde,p_4:p_4waarde})
    return waarschijnlijkheidswaarde

def posterior(p_1waarde,p_2waarde,p_3waarde,p_4waarde): #geeft waarde van posteriorfunctie in (p_1waarde,p_2waarde,p_3waarde,p_4waarde)
    prior=uniform.pdf(p_1waarde)*uniform.pdf(p_2waarde)*uniform.pdf(p_3waarde)*uniform.pdf(p_4waarde)
    posterior=prior*waarschijnlijkheidsfunctie(p_1waarde,p_2waarde,p_3waarde,p_4waarde)
    return posterior

waarden=[] 
waarde=[0.5,0.5,0.5,0.5] #startwaarde voor p_1,p_2,p_3,p_4
waarden.append(waarde)
reject=0 #houdt bij hoe vaak er afgewezen wordt
waarschijnlijkheden=[]
verhoudingen_1=[]
verhoudingen_2=[]
for i in range(1000000):
    random_getal= random.randint(0,3) #kies of p_1,p_2,p_3 of p_4 verandert wordt
    nieuwe_waarde=waarde.copy()
    nieuwe_waarde[random_getal]=waarde[random_getal]+np.random.normal(0,0.48)
    while nieuwe_waarde[random_getal]>1 or nieuwe_waarde[random_getal]<0: #zorgt dat de nieuwe coordinaat binnen [0,1] zit
        if nieuwe_waarde[random_getal]>1:
            nieuwe_waarde[random_getal]=2-nieuwe_waarde[random_getal]
        if nieuwe_waarde[random_getal]<0:
            nieuwe_waarde[random_getal]=-1*nieuwe_waarde[random_getal]
    kans=posterior(*waarde)
    nieuwe_kans=posterior(*nieuwe_waarde)
    #bepaal of de nieuwe waarde geaccepteerd wordt:
    if nieuwe_kans>=kans:
        waarde=nieuwe_waarde
    else:
        verhouding=nieuwe_kans/kans
        if np.random.rand()<verhouding: #kans op accepteren van verslechtering is verhouding
            waarde=nieuwe_waarde
        else: #de nieuwe waarde wordt niet geaccepteerd
            waarde=waarde
            reject=reject+1
    waarden.append(waarde)
    if i>=2000: #voor eerste 2000 iteraties bekijken we de verhoudingen niet
        verhouding_1=(1-waarde[3])/(1-waarde[1]) #geeft verhouding tussen besmettelijkheid volwassene en kind, bij het besmetten van volwassenen, notatie r_1 in verslag
        verhoudingen_1.append(verhouding_1)
        verhouding_2=(1-waarde[2])/(1-waarde[0]) #geeft verhouding tussen besmettelijkheid volwassene en kind, bij het besmetten van kinderen, notatie r_2 in verslag
        verhoudingen_2.append(verhouding_2)
    if i%10==0:
        waarschijnlijk=waarschijnlijkheidsfunctie(*waarde)
        waarschijnlijkheden.append(waarschijnlijk) #nodig voor plot maken van waarschijnlijkheid, plot alleen voor index deelbaar door 10
    if i%1000==0:
        print(i)

#waarschijnljkheid plot
plt.figure(figsize=(15,6),dpi=500)
iteratie=range(1,len(waarschijnlijkheden)+1)
plt.scatter(iteratie,waarschijnlijkheden,s=1,color='darkblue')
plt.xlabel('Iteratie')
plt.ylabel('Waarde waarschijnlijkheidsfunctie')
plt.title('Plot verloop waarschijnlijkheidsfunctie')
plt.show()

#waarschijnljkheid plot begin
plt.figure(figsize=(15,6),dpi=500)
waarschijnlijkheden=waarschijnlijkheden[0:9999]
iteratie=range(1,len(waarschijnlijkheden)+1)
plt.scatter(iteratie,waarschijnlijkheden,s=1,color='darkblue')
plt.xlabel('Iteratie')
plt.ylabel('Waarde waarschijnlijkheidsfunctie')
plt.title('Plot verloop waarschijnlijkheidsfunctie')
plt.show()

#histogram en schatting voor p_1, p_2, p_3 en p_4
plt.figure(figsize=(10,10),dpi=200)
waarden_1= [waarde[0] for waarde in waarden[2000:]] #eerste 2000 iteraties niet in histogram
plt.subplot(2,2,1)
plt.hist(waarden_1,bins=100,edgecolor='black') 
plt.title('Histogram van kansen $p_1$')
plt.xlabel('$p_1$')
plt.ylabel('Aantal')
schatting=np.percentile(waarden_1,50)
print(schatting)

waarden_2= [waarde[1] for waarde in waarden[2000:]]
plt.subplot(2,2,2)
plt.hist(waarden_2,bins=100,edgecolor='black')
plt.title('Histogram van kansen $p_2$')
plt.xlabel('$p_2$')
plt.ylabel('Aantal')
schatting=np.percentile(waarden_2,50)
print(schatting)

waarden_3= [waarde[2] for waarde in waarden[2000:]]
plt.subplot(2,2,3)
plt.hist(waarden_3,bins=100,edgecolor='black')
plt.title('Histogram van kansen $p_3$')
plt.xlabel('$p_3$')
plt.ylabel('Aantal')
schatting=np.percentile(waarden_3,50)
print(schatting)

waarden_4= [waarde[3] for waarde in waarden[2000:]]
plt.subplot(2,2,4)
plt.hist(waarden_4,bins=100,edgecolor='black')
plt.title('Histogram van kansen $p_4$')
plt.xlabel('$p_4$')
plt.ylabel('Aantal')
plt.tight_layout()
plt.show()
schatting=np.percentile(waarden_4,50)
print(schatting)

#plot van waarden die p_1,p_2,p_3 en p_4 aannemen
plt.figure(figsize=(15,24),dpi=500)
waarden_1_gefilterd=[waarde[0] for waarde in waarden[::10]] #plot alleen waarden met index deelbaar door 10
plt.subplot(4,1,1)
iteratie=range(1,len(waarden_1_gefilterd)+1)
plt.scatter(iteratie,waarden_1_gefilterd,s=1,color='darkblue')
plt.title('Waarden van $p_1$')
plt.xlabel('Iteratie')
plt.ylabel('$p_1$')

waarden_2_gefilterd=[waarde[1] for waarde in waarden[::10]]
plt.subplot(4,1,2)
iteratie=range(1,len(waarden_2_gefilterd)+1)
plt.scatter(iteratie,waarden_2_gefilterd,s=1,color='darkblue')
plt.title('Waarden van $p_2$')
plt.xlabel('Iteratie')
plt.ylabel('$p_2$')

waarden_3_gefilterd=[waarde[2] for waarde in waarden[::10]]
plt.subplot(4,1,3)
iteratie=range(1,len(waarden_3_gefilterd)+1)
plt.scatter(iteratie,waarden_3_gefilterd,s=1,color='darkblue')
plt.title('Waarden van $p_3$')
plt.xlabel('Iteratie')
plt.ylabel('$p_3$')

waarden_4_gefilterd=[waarde[3] for waarde in waarden[::10]]
plt.subplot(4,1,4)
iteratie=range(1,len(waarden_4_gefilterd)+1)
plt.scatter(iteratie,waarden_4_gefilterd,s=1,color='darkblue')
plt.title('Waarden van $p_4$')
plt.xlabel('Iteratie')
plt.ylabel('$p_4$')
plt.tight_layout()
plt.show()

#betrouwbaarheidsinterval voor p_1,p_2,p_3 en p_4
onder=np.percentile(waarden_1,2.5)
print(onder)
boven=np.percentile(waarden_1,97.5)
print(boven)
onder=np.percentile(waarden_2,2.5)
print(onder)
boven=np.percentile(waarden_2,97.5)
print(boven)
onder=np.percentile(waarden_3,2.5)
print(onder)
boven=np.percentile(waarden_3,97.5)
print(boven)
onder=np.percentile(waarden_4,2.5)
print(onder)
boven=np.percentile(waarden_4,97.5)
print(boven)

print(reject/1000000*100) #print het percentage van de nieuwe waarden die afgewezen werd

#correlatie tussen p_2 en p_4 en tussen p_1 en p_3
plt.figure(figsize=(12,6),dpi=200)
plt.subplot(1,2,1)
plt.plot(waarden_1,waarden_3,'ko', markersize=0.1)
plt.title('Correlatie tussen $p_1$ en $p_3$')
plt.xlabel('$p_1$')
plt.ylabel('$p_3$')
print('correlatie coefficient')
corr_1= np.corrcoef(waarden_1, waarden_3)
print(corr_1)
plt.subplot(1,2,2)
plt.plot(waarden_2,waarden_4, 'o', markersize=0.1) #lichtblauw
plt.title('Correlatie tussen $p_2$ en $p_4$')
plt.xlabel('$p_2$')
plt.ylabel('$p_4$')
plt.show()
corr_2= np.corrcoef(waarden_2, waarden_4)
print(corr_2)

#maak een histogram, schatting en betrouwbaarheidsinterval voor verhoudingen_1 en verhoudingen_2
plt.figure(figsize=(11,5),dpi=200)
plt.subplot(1,2,1)
gekozen_bins_1=np.arange(0,20, 0.5)
plt.hist(verhoudingen_1,bins=gekozen_bins_1,edgecolor='black')
plt.title('Histogram verhouding tussen besmettelijkheid \n volwassene en kind, bij het besmetten van volwassenen')
plt.xlabel('Verhouding')
plt.ylabel('Aantal')

plt.subplot(1,2,2)
gekozen_bins_2=np.arange(0,3, 0.1)
plt.hist(verhoudingen_2,bins=gekozen_bins_2,edgecolor='black')
plt.title('Histogram verhouding tussen besmettelijkheid \n volwassene en kind, bij het besmetten van kinderen')
plt.xlabel('Verhouding')
plt.ylabel('Aantal')
plt.show()

schatting=np.percentile(verhoudingen_1,50)
print(schatting)
onder=np.percentile(verhoudingen_1,2.5)
print(onder)
boven=np.percentile(verhoudingen_1,97.5)
print(boven)

schatting=np.percentile(verhoudingen_2,50)
print(schatting)
onder=np.percentile(verhoudingen_2,2.5)
print(onder)
boven=np.percentile(verhoudingen_2,97.5)
print(boven)

print(max(verhoudingen_1))
print(max(verhoudingen_2))
