import math 

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*l)+(l*t)
    print(f"Luas balok adalah {hitung}")
    
def l_kubus(sisi):
    hitung = 6 * (sisi * sisi)
    print(f"Luas kubus adalah {hitung}")

def l_tabung(r2, t):
    hitung = 6 * (r2 + t)
    print(f"Luas tabung adalah {hitung}")
    
def l_limas(a, st):
    hitung = math.sqrt(3) * a * st
    print(f"Luas limas adalah {hitung}")
    
def l_prisma(alas, tinggi):
    hitung = 1/2 * alas *tinggi
    print(f"Luas prisma adalah {hitung}")
    
    

    
