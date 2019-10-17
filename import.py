import baim
def main():
    p = 12
    l = 6

    luas = baim.luasPersegi(p, l)
    kel  = baim.kelilingPersegi(p, l)

    print("PERSEGI")
    print("Panjang\t: ", p)
    print("Lebar\t: ", l)
    print("Luas\t= ", luas)
    print("Keliling\t= ", kel)

if __name__ == "__main__":
    main()
    
