# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:12:53 2023

@author: frida
"""
from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt
import math
import random

def waarschijnlijkheid(p_1,p_2,p_3,p_4):
    p5=p_2*p_4
    p7=p_1*p_2**2
    p13=p_3*p_4
    p24=p_1*p_2**2
    p58=p_3**2*p_4
    p61=p_3**4
    p62=p_3
    p63=p_1**2*p_2
    p80=(1-p_2)**2+2*p_2*(1-p_2)*(1-p_4)
    p116=p_3**2
    p117=p_3*p_4**2
    p123=(1-p_3)**2*(1-p_4)+2*p_3**2*(1-p_1)*(1-p_3)*(1-p_4)+2*p_1*(1-p_3)**2*p_3*(1-p_4)+2*(1-p_1)*(1-p_3)**2*p_3*(1-p_4)+p_4*(1-p_3)**2*(1-p_2)**2+\
        2*p_2*(1-p_2)*(1-p_3)**2*p_4+p_3**2*(1-p_3)**2*(1-p_4)+2*p_3**3*(1-p_4)*(1-p_3)*(1-p_1)+2*(1-p_3)**2*p_3*p_4*p_1*(1-p_2)+2*(1-p_3)*p_3*p_4*(1-p_1)*p_2*(1-p_2)+\
            2*(1-p_3)*p_3*p_4*(1-p_1)*(1-p_2)
    p125=p_3**4*(1-p_4)
    p127=p_2**2
    p136=(1-p_1)*p_2**4
    p138=p_1*p_2**2
    p139=p_3**2*p_4
    p145=(1-p_2)**2*(1-p_4)+(1-p_2)**2*p_4+2*(1-p_2)*p_2*(1-p_4)+p_2**2*(1-p_4)+2*p_2*(1-p_2)*p_4
    p152=p_3**4*(1-p_4)
    p157=p_3**2*p_4
    p159=p_3**2*p_4
    p163=(1-p_3)**2*(1-p_4)+2*p_3**2*(1-p_1)*(1-p_3)*(1-p_4)+2*p_1*(1-p_3)**2*p_3*(1-p_4)+2*(1-p_1)*(1-p_3)**2*p_3*(1-p_4)+p_4*(1-p_3)**2*(1-p_2)**2+\
        2*p_2*(1-p_2)*(1-p_3)**2*p_4+p_3**2*(1-p_3)**2*(1-p_4)+2*p_3**3*(1-p_4)*(1-p_3)*(1-p_1)+2*(1-p_3)**2*p_3*p_4*p_1*(1-p_2)+2*(1-p_3)*p_3*p_4*(1-p_1)*p_2*(1-p_2)+\
            2*(1-p_3)*p_3*p_4*(1-p_1)*(1-p_2)
    p171=(1-p_3)*p_1+p_3*(1-p_1)+(1-p_3)*(1-p_1)
    p173=p_3*p_4
    p174=(1-p_3)**2*(1-p_4)+2*p_3**2*(1-p_1)*(1-p_3)*(1-p_4)+2*p_1*(1-p_3)**2*p_3*(1-p_4)+2*(1-p_1)*(1-p_3)**2*p_3*(1-p_4)+p_4*(1-p_3)**2*(1-p_2)**2+\
        2*p_2*(1-p_2)*(1-p_3)**2*p_4+p_3**2*(1-p_3)**2*(1-p_4)+2*p_3**3*(1-p_4)*(1-p_3)*(1-p_1)+2*(1-p_3)**2*p_3*p_4*p_1*(1-p_2)+2*(1-p_3)*p_3*p_4*(1-p_1)*p_2*(1-p_2)+\
            2*(1-p_3)*p_3*p_4*(1-p_1)*(1-p_2)
    p176=(1-p_3)**2+2*p_3*(1-p_3)
    p191=p_2**2
    p196=p_1*p_2**2
    p200=(1-p_2)*(1-p_4)*p_1*p_3**2+(1-p_4)*p_1*p_3**2*p_2+(1-p_2)*p_1*p_3**3*p_4
    p203=(1-p_3)**4+4*(1-p_3)**3*p_3+4*p_3**2*(1-p_3)**2+4*p_3**3*(1-p_3)*(1-p_1)+2*p_3**2*(1-p_3)**2*(1-p_1)
    p217=(1-p_1)*p_3**2+(1-p_1)*(1-p_3)**2+2*p_1*p_3*(1-p_3)+2*(1-p_1)*p_3*(1-p_3)+(1-p_3)**2*p_1
    p228=p_3**2*p_4
    p231=p_3*p_4
    p245=p_2**3
    p254=p_3**2*p_4
    p257=p_3*p_4
    p273=p_3*p_4
    p280=2*(1-p_2)*p_2*p_1*(1-p_3)*(1-p_4)+2*(1-p_2)*p_2*p_1*(1-p_4)*p_3*(1-p_3)+2*(1-p_2)*p_2*p_1*p_4*(1-p_3)*(1-p_2)+2*(1-p_1)*p_2**3*(1-p_2)*(1-p_4)+(1-p_1)*p_2**2*(1-p_2)**2+\
        (1-p_2)**2*p_1*(1-p_3)**2+2*(1-p_2)**2*p_1*(1-p_3)*p_3+2*(1-p_2)*(1-p_1)*p_2**2*(1-p_4)+2*(1-p_2)**2*(1-p_1)*p_2*(1-p_4)+2*(1-p_2)**2*(1-p_1)*p_2*p_4
    p287=p_3**2*p_4
    p289=p_3
    p293=p_3**2*p_4
    p298=p_3**2*p_4
    p300=p_3**2*p_4
    p304=p_3*p_4    
    kansen=[p5,p7,p13,p24,p58,p61,p62,p63,p80,p116,p117,p123,p125,p127,p136,p138,p139,p145,p152,p157,p159,p163,p171,p173,p174,p176,p191,p196,p200,p203,
    p217,p228,p231,p245,p254,p257,p273,p280,p287,p289,p293,p298,p300,p304,]
    waarschijnlijkheidwaarde=math.prod([kans for kans in kansen])
    return waarschijnlijkheidwaarde

def posterior(p_1,p_2,p_3,p_4):
    waarschijnlijkheidswaarde=waarschijnlijkheid(p_1, p_2, p_3, p_4)
    prior=uniform.pdf(p_1)*uniform.pdf(p_2)*uniform.pdf(p_3)*uniform.pdf(p_4)
    posteriorwaarde=prior*waarschijnlijkheidswaarde
    return posteriorwaarde

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
        waarschijnlijk=waarschijnlijkheid(*waarde)
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

#waarschijnlijkheid plot begin
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
