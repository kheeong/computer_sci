count = 0
type_of_bread_total = []
filling_total = []
size_total = []
number_of_baguettes_sold = 0

def input_Baguettes_size():
    print("Baguettes size available:15 or 30")
    print("Input your Baguettes Size by typing 15 or 30")
    Baguettes_size = int(input())
    while (Baguettes_size != 15 and Baguettes_size != 30):
        print("Baguettes Size not valid, please input again")
        Baguettes_size = int(input())
    return Baguettes_size

def input_Baguettes_bread():
    print("Baguettes bread available in white,brown or seeded")
    print("Input your Baguettes bread by typing white,brown or seeded")
    Baguettes_bread = input()

    while(Baguettes_bread != "white" and Baguettes_bread != "brown" and Baguettes_bread != "seeded"):
        print("Baguettes bread not valid, please input again")
        Baguettes_bread = input()
    return Baguettes_bread

def input_filling():
    print("Filling available:Beef,Chicken,Cheese,Egg,Tuna,Turkey")
    print("Please enter the filling of your choice")
    Filling_list = ["Beef","Chicken","Cheese","Egg","Tuna","Turkey"]
    Filling = input()
    filling_valid = False
    while(True):
        for item in Filling_list:
            if(item == Filling):
                filling_valid = True
        if(filling_valid == True):
            break
        print("Filling not valid,please enter again")
        Filling = input()
    return Filling

def input_salad():
    print("Please enter number of Salad you wanted to add")
    number_of_salad = int(input())
    while(True):
        if(number_of_salad <= 3):
            break
        else:
            print("number of salad is more than 3, maxinum of 3 is allow, please enter again")
            number_of_salad = int(input())
    salad = []
    Salad_list = ["Lettuce","Tomato","Sweetcorn","Cucumber","Peppers"]
    print("Salad available:Lettuce,Tomato,Sweetcorn,Cucumber,Peppers")
    for i in range(number_of_salad):
        print("Please enter your salad")
        salad_input = input()
        salad_valid = False
        while(True):
            for item in Salad_list:
                if(salad_input == item):
                    salad_valid = True
            if(salad_valid == True):
                break
            print("Salad not valid,please enter again")
            salad_input = input()
        salad.append(salad_input)
    return salad

while(True):
    print("Enter O to order or enter E to end the day")
    End_day = input()
    if(End_day == "O"):
        Gobal_Baguettes_size = input_Baguettes_size()
        Gobal_Baguettes_bread = input_Baguettes_bread()
        Gobal_filling = input_filling()
        Gobal_salad = input_salad()
        print("Enter Y to confirm the order or enter C to alter your order or enter X to discard your order")
        confirm_order = input()
        while(True):
            if(confirm_order == "C"):
                while(True):
                    print("Please type which order you wanted to alter")
                    print("Type Baguettes Size,Baguettes Bread,Filling or Salads")
                    alter_order = input()
                    if(alter_order == "Baguettes Size"):
                        Gobal_Baguettes_size = input_Baguettes_size()
                        break
                    elif(alter_order == "Baguettes Bread"):
                        Gobal_Baguettes_bread = input_Baguettes_bread()
                        break
                    elif(alter_order == "Filling"):
                        Gobal_filling = input_filling()
                        break
                    elif(alter_order == "Salads"):
                        Gobal_salad = input_salad()
                        break
                    else:
                        print("Please input a valid order to alter")
            if(confirm_order == "Y"):
                count = count + 1
                print("Your order number:")
                print(count)
                print("Your Baguettes Size")
                print(Gobal_Baguettes_size)
                size_total.append(Gobal_Baguettes_size)
                print("Your Baguettes Bread")
                print(Gobal_Baguettes_bread)
                type_of_bread_total.append(Gobal_Baguettes_bread)
                print("Your filling")
                print(Gobal_filling)
                filling_total.append(Gobal_filling)
                print("your salads")
                print(Gobal_salad)
                break
            elif(confirm_order == "X"):
                print("order discarded")
                break
            print("Enter Y to confirm the order or enter C to alter your order or enter X to discard your order")
            confirm_order = input()
    else:
        break

number_of_baguettes_sold = count
Filling_list = ["Beef","Chicken","Cheese","Egg","Tuna","Turkey"]
number_of_filling = [0,0,0,0,0,0]

for item in filling_total:
    index = Filling_list.index(item)
    number_of_filling[index] = number_of_filling[index] + 1

index_of_filling_max = number_of_filling.index(max(number_of_filling))
index_of_filling_min = number_of_filling.index(min(number_of_filling))

print("Most popular Filling:")
print(Filling_list[index_of_filling_max])
print("Percentage:")
print(max(number_of_filling)/number_of_baguettes_sold)
print("Least popular Filling:")
print(Filling_list[index_of_filling_min])
print("Percentage:")
print(min(number_of_filling)/number_of_baguettes_sold)