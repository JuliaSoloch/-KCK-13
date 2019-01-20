import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseeg as ag
dane=pd.read_csv("/Users/juliasoloch/Desktop/sub-01_trial-06.csv", delimiter=',', engine='python')

plt.rcParams['font.size'] = 14

sygnal1=dane["Kolumna 1"]
sygnal2=dane["Kolumna 5"]

czestotliwoscProbkowania=200
t=np.linspace(0, 37.95, czestotliwoscProbkowania*37.95)


plt.plot(t, sygnal1)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")

'''
plt.show()
'''

przefiltrowany1=ag.pasmowozaporowy(sygnal1, czestotliwoscProbkowania, 49, 51)
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany1, czestotliwoscProbkowania, 1, 50)

plt.plot(przefiltrowany2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")

'''
plt.show()
'''

'''dane=dane.sort_values(by="Kolumna 1", ascending=False)
print(dane[["Kolumna 5", "Kolumna 1"]])'''

print(dane.at[5671, 'Kolumna 5'])
print(dane.at[6515, 'Kolumna 5'])
print(dane.at[5943, 'Kolumna 5'])
print(dane.at[3920, 'Kolumna 5'])
print(dane.at[6250, 'Kolumna 5'])
print(dane.at[3921, 'Kolumna 5'])
print(dane.at[5672, 'Kolumna 5'])
print(dane.at[3923, 'Kolumna 5'])
print(dane.at[6251, 'Kolumna 5'])
print(dane.at[2480, 'Kolumna 5'])
print(dane.at[6248, 'Kolumna 5'])
