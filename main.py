from function import *
import datetime


def main():
    expense_file_path = "gastos.csv"

    menu = ["Introducir Gasto", "Ver gastos"]
    for i, category_name in enumerate(menu):
            print(f" {i + 1}. {category_name}")
    value_range = f"[1 - {len(menu)}]"

    selected_menu = int(input(f"Escoge un numero de categoria {value_range}: "))
    print(selected_menu)
 
    if selected_menu == 1:
        #get user input expense
        expense = get_user_eexpenses()
        #write into file
        save_as_file(expense, expense_file_path)

    #read file into expenses
    if selected_menu == 2:
        sumary_expenses(expense_file_path)



def get_user_eexpenses():
    expense_name = input("Nombre: ")
    expense_amount = float(input("Cuanto cuesta: "))
    now = datetime.datetime.now()
    expense_month = now.strftime("%m")
    expense_year = now.strftime("%Y")
    year_int = int(expense_year)
    month_int = int(expense_month)
    

    expense_category = [
        "Alquiler",
        "Comida",
        "Ocio",
        "Inversion",
    ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Escoge un numero de categoria {value_range}: ")) -1
        
        try:
            value_range = f"[1 - {len(expense_category)}]"
        except Exception:
            print(f"Pusistes algo que no era un numero >:( ")
        
        if selected_index in range(len(expense_category)):
            cat = expense_category[selected_index]

            new_expense = Expense(name = expense_name, amount = expense_amount, category = cat, month = month_int, year = year_int)
            return new_expense
        else:
            print(f"Categoria invalida. Vuelve a intentarlo")


def save_as_file(expense: Expense, expense_file_path):
    print(f"Guardando {expense} en {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}, {expense.month}, {expense.year}\n")
    

def sumary_expenses(expense_file_path):
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            striped_line = line.strip()
            expense_name, expense_amount, expense_category, expense_month, expense_year = striped_line.split(",")
            line_expenses = Expense(expense_name, expense_amount, expense_category, expense_month, expense_year)
            expenses.append(line_expenses)
            print(line_expenses)

if __name__ == "__main__" :
    main()
