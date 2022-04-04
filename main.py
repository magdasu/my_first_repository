import time

def aa():
    a = input("Wpisz swoje imie: ")
    print(f"Moje pierwsze repo! {a}")
    print("Siema!")

def godzina():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t")
    print("Jest godzina ", current_time)
aa()
godzina()