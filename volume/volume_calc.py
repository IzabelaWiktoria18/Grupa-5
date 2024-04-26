import  math #skierhu1UEP | do math.pi potrzebne

def objetosc_szescianu(a):
    return a*a*a
def objetosc_prostopadloscianu(a, b, c):
    return a*b*c
def objetosc_graniastoslupa(pole_podstawy, wysokosc_graniastoslupa):
    return pole_podstawy*wysokosc_graniastoslupa
def objetosc_stozka(wysokosc_stozka, promien_podstawy):
    return (1/3) * math.pi * math.pow(promien_podstawy, 2) * wysokosc_stozka  #skierhu1UEP | promien podstawy do potegi i pi