def trojkat(a, H):
    POLE = 1/2 * a * H #Poprawiony wzór na pole trójkąta
    return POLE

def kwadrat(a):
    kwadrat = a * a
    return kwadrat

def prostkat(a, b):
    p = a * b #Poprawiony wzór na pole prostokąta
    return p

def romb(a, b, H):
    powierzchnia = 1/2 * (a + b) * H
    return powierzchnia

print("Pole trójkąta:", trojkat(3, 6))
print("Pole kwadratu:", kwadrat(6))
print("Pole prostokąta:", prostkat(5, 6))
print("Pole rombu:", romb(2, 3, 56))
