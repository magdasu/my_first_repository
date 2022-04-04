import datetime

def aa():
    print("Moje pierwsze repo! Magda")
    print("Siema!")

def dzis():
    d = datetime.date.today()
    today = d.strftime("%d/%m/%Y")
    print(today)

aa()
dzis()