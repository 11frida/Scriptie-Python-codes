# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:35:32 2023

@author: frida
"""
import numpy as np
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

primary_cases=[] #aantal indexgevallen
for i in range(59):
    primary_case=data[i][4]+data[i][5]+data[i][6]
    primary_cases.append(primary_case)
gemiddelde=np.mean(primary_cases)
standaardafwijking=np.std(primary_cases)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

uninfected_members=[] #aantal niet geinfecteerde personen bij het begin van de uitbraak
for i in range(59):
    uninfected=data[i][7]+data[i][8]+data[i][9]
    uninfected_members.append(uninfected)
gemiddelde=np.mean(uninfected_members)
standaardafwijking=np.std(uninfected_members)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)
gezin=[]
for i in range(59):
    gezin.append(data[i][0])

infections=[] #aantal indexgevallen en personen besmet tijdens de uitbraak
for i in range(59):
    infection=data[i][1]+data[i][2]+data[i][3]+data[i][4]+data[i][5]+data[i][6]
    infections.append(infection)
gemiddelde=np.mean(infections)
standaardafwijking=np.std(infections)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

primary_cases_kind=[]
for i in range(59):
    primary_case_kind=data[i][4]+data[i][5]
    primary_cases_kind.append(primary_case_kind)
gemiddelde=np.mean(primary_cases_kind)
standaardafwijking=np.std(primary_cases_kind)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

uninfected_members_kind=[]
for i in range(59):
    uninfected_kind=data[i][7]+data[i][8]
    uninfected_members_kind.append(uninfected_kind)
gemiddelde=np.mean(uninfected_members_kind)
standaardafwijking=np.std(uninfected_members_kind)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)
print('---------------')

primary_cases_volw=[]
for i in range(59):
    primary_case_volw=data[i][6]
    primary_cases_volw.append(primary_case_volw)
gemiddelde=np.mean(primary_cases_volw)
standaardafwijking=np.std(primary_cases_volw)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

uninfected_members_volw=[]
for i in range(59):
    uninfected_volw=data[i][9]
    uninfected_members_volw.append(uninfected_volw)
gemiddelde=np.mean(uninfected_members_volw)
standaardafwijking=np.std(uninfected_members_volw)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

huishoudgrootte=[]
for i in range(59):
    hg=data[i][4]+data[i][5]+data[i][6]+data[i][7]+data[i][8]+data[i][9]
    huishoudgrootte.append(hg)

infections_kind=[]
for i in range(59):
    infection_kind=data[i][1]+data[i][2]+data[i][4]+data[i][5]
    infections_kind.append(infection_kind)
gemiddelde=np.mean(infections_kind)
standaardafwijking=np.std(infections_kind)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

infections_volw=[]
for i in range(59):
    infection_volw=data[i][3]+data[i][6]
    infections_volw.append(infection_volw)
gemiddelde=np.mean(infections_volw)
standaardafwijking=np.std(infections_volw)
print("Gemiddelde:",gemiddelde)
print("Standaardafwijking:",standaardafwijking)

#geeft alle combinaties van primary_cases_kind,primary_cases_volw,uninfected_members_kind,uninfected_members_volw,infections_kind,infections_volw,huishoudgrootte (gesorteerd)
combinations=list(zip(primary_cases_kind,primary_cases_volw,uninfected_members_kind,uninfected_members_volw,infections_kind,infections_volw,huishoudgrootte))
print(sorted(combinations))

#geeft alle unieke combinaties van primary_cases_kind,primary_cases_volw,uninfected_members_kind,uninfected_members_volw,infections_kind,infections_volw,huishoudgrootte(gesorteerd)
unique_combinations=list(set((combinations)))
print(sorted(unique_combinations))


#geeft alle combinaties van infections, uninfected members, primary_cases (gesorteerd)
combinations=list(zip(infections, uninfected_members, primary_cases))
print(sorted(combinations))

#geeft alle unieke combinaties van infections, uninfected members, primary_cases (gesorteerd)
unique_combinations=list(set(combinations))
print(sorted(unique_combinations))

