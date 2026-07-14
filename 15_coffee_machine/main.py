from machine_data import milk
from machine_data import coffee
from machine_data import water
from machine_data import machine_money
from art import machine
from art import espresso
from art import cappuchino
from art import lattee
import machine_data

def price_display(choice):
    if choice==1 and machine_data.milk>=100 and machine_data.coffee>=20 and machine_data.water>=100:
        print("you choosed cappuchino that will be 150/-")
        machine_data.machine_money+=150
        machine_data.milk-=100
        machine_data.coffee-=20
        machine_data.water-=100
    elif choice==2 and machine_data.milk>=50 and machine_data.coffee>=50 and machine_data.water>=100:
        print("you choosed espressoo that will be 100/-")
        machine_data.machine_money+=100
        machine_data.milk-=50
        machine_data.coffee-=50
        machine_data.water-=100
    elif choice==3 and machine_data.milk>=200 and machine_data.coffee>=10 and machine_data.water>=50:
        print("you choosed lattee that will be 200/-")
        machine_data.machine_money+=200    
        machine_data.milk-=200
        machine_data.coffee-=10
        machine_data.water-=50 
    elif choice==4 or 5:
        return
    else:
        print("you dont have enough material ask for restock >>>>")

    if choice==1 or 2 or 3:
        note1=int(input("200 rs note:"))
        note2=int(input("100 rs note:"))
        note3=int(input("50 rs note:"))
        note_total=note1*200+note2*100+note3*50
        change=0
    if choice==1:
        change=note_total-150
    elif choice==2:
        change=note_total-100
    elif choice==3:
        change=note_total-200
    
    print(f"you gave {note_total} here is you're return:{change}")
def art_display(choice):
    if choice==1:
        print(cappuchino)      
    elif choice==2:
        print(espresso)   
    elif choice==3:
        print(lattee)

def refill_display():
    machine_data.milk+=1000
    machine_data.coffee+=1000
    machine_data.water+=1000
    print("yo're refill is done")


print(machine)

#ask what do you want (espresso,latte,cappuchino)

while True:
    choice=int(input("""
    1.cappuchino
    2.espresso
    3.lattee 
    4.no order
    what would you like to have (1,2,3,4) :"""))
    if choice==4:
        print("THANK YOU !!")
        break
    elif choice==5:
        print("Here is you're report: ")
        print(f"""
milk={machine_data.milk}
water={machine_data.water}
coffee={machine_data.coffee}
""")
        refill=input("want to refill yes or no: ").lower()
        if refill=="yes":
            refill_display()
        else:
            print("EXITED AUTHOR MODE>>>>>")
    elif choice!=1 or 2 or 3 or 4 or 5:
        print("invalid choice!!! choose again")

    price_display(choice)
    art_display(choice)
    print(machine_data.machine_money)
    print(f"milk--{machine_data.milk} coffee--{machine_data.coffee} water--{machine_data.water}")
