# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 09:10:25 2023

@author: frida
"""

import sympy
import matplotlib.pyplot as plt
import math
p = sympy.symbols('p')
#p_inx is kans op x besmettingen bij i indexgevallen en n personen niet geinfecteerd bij begin vd uitbraak
p_111 = p
p_121 = p**2
p_123 = 2*p*(1-p)**2 + (1-p)**2
p_131 = p**3
p_132 = 3*(1-p)*p**4
p_134 = (1-p)**3 + 6*(1-p)**3*p**3 + 3*(1-p)**3*p**2 + 3*(1-p)**4*p + 6*(1-p)**3*p**2
p_141 = p**4
p_142 = 4*(1-p)*p**6
p_143 = 12*(1-p)**2*p**7 + 6*(1-p)**2*p**6
p_144 = 24*(1-p)**3*p**7 + 12*(1-p)**3*p**6 + 24*(1-p)**3*p**6 + 12*(1-p)**4*p**5 + 4*(1-p)**3*p**4
p_145 = (1-p)**4 + 16*(1-p)**4*p**3 + 24*(1-p)**4*p**6 + 36*(1-p)**4*p**5 + 12*(1-p)**5*p**4 + 6*(1-p)**6*p**2 + 24*(1-p)**5*p**3 + \
    24*(1-p)**4*p**4 + 12*(1-p)**5*p**2 + 4*(1-p)**6*p + 24*(1-p)**4*p**5 + 12*(1-p)**5*p**4
p_151 = p**5
p_212 = p**2
p_213 = 2*p*(1-p) + (1-p)**2
p_222 = p**4
p_223 = 4*(1-p)*p**4 + 2*(1-p)**2*p**3
p_224 = (1-p)**4 + 4*(1-p)**3*p + 4*(1-p)**2*p**2 + 4*(1-p)**2*p**3 + 2*(1-p)**3*p**2
p_232 = p**6
p_234 = 12*(1-p)**2*p**6 + 12*(1-p)**3*p**5 + 3*(1-p)**4*p**4 + 12*(1-p)**2*p**7 + 6*(1-p)**3*p**6
p_314 = 3*(1-p)*p**2 + 3*(1-p)**2*p + (1-p)**3
p_324 = 2*(1-p)**3*p**4 + 6*(1-p)**2*p**5 + 6*(1-p)*p**6
p_414 = p**4

kansen=[p_111, p_121, p_123, p_131, p_132, p_134, p_141, p_142, p_143, p_144, p_145, p_151,
    p_212, p_213, p_222, p_223, p_224, p_232, p_234, p_314, p_324, p_414]
#lijst coefficienten geeft hoe vaak de kansen voorkomen in de data
coefficienten= [2, 8, 1, 17, 3, 4, 2, 2, 1, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1]
waarschijnlijkheid=sum([c*sympy.log(kans) for c,kans in zip(coefficienten,kansen)]) #log waarschijnlijkheidsfunctie

#bepaal maximum van waarschijnlijkheid
afgeleide=sympy.diff(waarschijnlijkheid,p)
nulpunt=sympy.nsolve(afgeleide,p,0.5) #beginwaarde 0.5
print(nulpunt)

#plot waarschijnlijkheid
sympy.plot(waarschijnlijkheid, (p, 0, 1),title='Plot van log waarschijnlijkheidsfunctie', xlabel='p', ylabel='l(p)',color='darkblue',dpi=300)
plt.show()

#betrouwbaarheidsinterval
informatie=1/59*sum([c*(sympy.diff(sympy.log(kans),p))**2 for c,kans in zip(coefficienten,kansen)])
informatie_nulpunt=informatie.subs(p,nulpunt)
ondergrens=nulpunt-1.96/math.sqrt(59*informatie_nulpunt)
bovengrens=nulpunt+1.96/math.sqrt(59*informatie_nulpunt)
print(ondergrens,bovengrens)
