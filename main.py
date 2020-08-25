count = 0
type_of_bread_total = []
filling_total = []
size_total = []
number_of_baguettes_sold = 0
while(True):
    print("Enter O to order or enter E to end the day")
    End_day = input()
    if(End_day == "O"):
        print("Baguettes size available:15 or 30")
        print("Input your Baguettes Size by typing 15 or 30")
        Baguettes_size = int(input())
        Baguettes_size_valid = False
        while(Baguettes_size_valid == False):
            if(Baguettes_size == 15 or Baguettes_size == 30):
                Baguettes_size_valid = True
            else:
                print("Baguettes Size not valid, please input again")
                Baguettes_size = int(input())
        print("Baguettes bread available in white,brown or seeded")
        print("Input your Baguettes bread by typing white,brown or seeded")
        Baguettes_bread = input()
        Baguettes_bread_valid = False
        while(Baguettes_bread_valid == False):
            if(Baguettes_bread == "white" or Baguettes_bread == "brown" or Baguettes_bread == "seeded"):
                Baguettes_bread_valid = True
            else:
                print("Baguettes bread not valid, please input again")
                Baguettes_bread = input()
        print("Filling available:Beef,Chicken,Cheese,Egg,Tuna,Turkey")
        print("Please enter the filling of your choice")
        Filling_list = ["Beef","Chicken","Cheese","Egg","Tuna","Turkey"]
        Filling = input()
        Filling_valid = False
        while(Filling_valid == False):
            for item in Filling_list:
                if(item == Filling):
                    Filling_valid = True
            if(Filling_valid == False):
                print("Filling not valid,please enter again")
                Filling = input()
        print("Please enter number of Salad you wanted to add")
        number_of_salad = int(input())
        number_of_salad_valid = False
        while(number_of_salad_valid == False):
            if(number_of_salad <= 3):
                number_of_salad_valid = True
            else:
                print("number of salad is more than 3, maxinum of 3 is allow, please enter again")
                number_of_salad = int(input())
        salad = []
        Salad_list = ["Lettuce","Tomato","Sweetcorn","Cucumber","Peppers"]
        print("Salad available:Lettuce,Tomato,Sweetcorn,Cucumber,Peppers")
        for i in range(number_of_salad):
            print("Please enter your salad")
            salad_input = input()
            salad_input_valid = False
            while(salad_input_valid == False):
                for item in Salad_list:
                    if(salad_input == item):
                        salad_input_valid = True
                if(salad_input_valid == False):
                    print("Salad not valid,please enter again")
                    salad_input = input()
            salad.append(salad_input)
        print("Enter Y to confirm the order")
        confirm_order = input()
        if(confirm_order == "Y"):
            count = count + 1
            print("your order number:")
            print(count)
            print("your Baguettes Size")
            print(Baguettes_size)
            size_total.append(Baguettes_size)
            print("your Baguettes Bread")
            print(Baguettes_bread)
            type_of_bread_total.append(Baguettes_bread)
            print("your filling")
            print(Filling)
            filling_total.append(Filling)
            print("your salads")
            print(salad)
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