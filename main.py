from tkinter import *

# Create main window
root = Tk()
root.title("Personal Fitness Meal Planner")
root.geometry("500x500")

# Placeholder data
foods = [
    {"name": "Chicken Breast", "calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    {"name": "Brown Rice", "calories": 215, "protein": 5, "carbs": 45, "fats": 1.6},
    {"name": "Broccoli", "calories": 55, "protein": 4.5, "carbs": 11, "fats": 0.6},
]

# Variables
selected_foods = []
calorie_limit = 2000
total_calories = 0

# Functions
def add_food():
    food = food_var.get()
    for item in foods:
        if item["name"] == food:
            selected_foods.append(item)
            update_display()
            break

def update_display():
    global total_calories
    total_calories = sum([f["calories"] for f in selected_foods])
    food_list.delete(0, END)
    for item in selected_foods:
        food_list.insert(END, f'{item["name"]} - {item["calories"]} cal')
    total_cal_label.config(text=f"Total Calories: {total_calories}")

# GUI Elements
Label(root, text="Select a Food Item:").pack(pady=10)
food_var = StringVar(root)
food_var.set(foods[0]["name"])  # Default value
food_dropdown = OptionMenu(root, food_var, *[f["name"] for f in foods])
food_dropdown.pack()

add_button = Button(root, text="Add Food", command=add_food)
add_button.pack(pady=10)

Label(root, text="Selected Foods:").pack(pady=10)
food_list = Listbox(root, height=10, width=40)
food_list.pack(pady=10)

total_cal_label = Label(root, text=f"Total Calories: {total_calories}")
total_cal_label.pack(pady=10)

root.mainloop()
