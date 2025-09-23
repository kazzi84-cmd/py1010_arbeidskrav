"""
Created on Thu Sep 11 21:30:32 2025

@author: karin aalmo (kazzi84@hotmail.com)

PfR: Oppgave 3.1, Formatert utskrift av beløp med renter.

"""

belop = 10000   # Beløp som settes inn på konto.
aar = 5         # Antall år beløpet står på konto.
rente = 1.85    # Rente i prosent.

saldo = round (belop * (1 + rente/100)**aar, 2)     # Saldo på kontoen etter
                                                    # gitt antall år, med gitt
                                                    # rente.
print(saldo)

