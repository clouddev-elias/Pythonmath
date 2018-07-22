# Python 3
# Plott funksjonen f(x) = x^3 - 20.0 for å finne hvor f(x)=0 har røtter

from matplotlib import pyplot

def f(x):
    return x**3 - 20.0

# lag en tabell (liste) med x-verdier
x = [i/2.-1. for i in range(15)]
print("x = ",x)

# lag en tabell (liste) til funksjonsverdiene f(x), og sett alle elementene
# lik null
fx = [0. for i in range(15)]

# regn ut f(x) for x-verdiene i listen
for i in range(15):
    fx[i] = f(x[i])

pyplot.plot(x,fx,'-')
pyplot.grid(True)
pyplot.xlabel('x')
pyplot.ylabel('f(x)')
pyplot.show()
