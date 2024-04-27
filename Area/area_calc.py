def trojkat(a, H):
    POLE = 1/3 * a * H
    return POLE

def kwadrat(a):
    kwadrat = a * a
    return kwadrat
#poprawiono wzór na pole prostokąta i nazwę
def prostkat(a, b):
    p = a * b
    return p

def romb(a, b, H):
    powierzchnia = 1/2 * (a + b) * H
    return powierzchnia

print("Pole trójkąta:", trojkat(3, 6))
print("Pole kwadratu:", kwadrat(6))
print("Pole prostokąta:", prostkat(5, 6))
print("Pole rombu:", romb(2, 3, 56))