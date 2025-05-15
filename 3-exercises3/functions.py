
# 1. Library Book Tracker
library = []

def add_book(name, author, pages):
    library.append({"name": name, "author": author, "pages": pages})

def find_book(book):
    for b in library:
        if b["name"] == book:
            return "book found"
    return "Book not found."

def show_books():
    for b in library:
        print(b["name"], "-", b["author"], "-", b["pages"], "pages")


# 2. Student Grade Manager
grades = {}

def add_student(name):
    grades[name] = []

def add_grade(name, grade):
    if name in grades:
        grades[name].append(grade)

def get_average(name):
    if name in grades and len(grades[name]) > 0:
        return sum(grades[name]) / len(grades[name])
    return 0.0


# 3. Restaurant Menu Editor
menu = {}

def add_dish(name, price, is_available):
    menu[name] = {"price": price, "available": is_available}

def change_availability():
    for dish in menu.values():
        dish["available"] = not dish["available"]

def total_available_price():
    total = 0
    for dish in menu.values():
        if dish["available"]:
            total += dish["price"]
    return total


# 4. Warehouse Box Counter
warehouse = {}

def add_box(name, quantity):
    warehouse[name] = quantity

def update_quantity(name, quantity):
    if name in warehouse:
        warehouse[name] += quantity

def has_enough(name, needed):
    if name in warehouse:
        return warehouse[name] >= needed
    return False


# 5. Movie Rating System
movies = {}

def add_movie(name):
    movies[name] = []

def rate_movie(name, rating):
    if name in movies:
        movies[name].append(rating)

def average_rating(name):
    if name in movies and len(movies[name]) > 0:
        return sum(movies[name]) / len(movies[name])
    return 0.0


# 6. Online Course Tracker
courses = {}

def add_course(name, duration, enrolled):
    courses[name] = {"duration": duration, "enrolled": enrolled}

def update_enrollment(name, new_enrollment):
    if name in courses:
        courses[name]["enrolled"] = new_enrollment

def filter_by_hour(min_hours):
    result = []
    for name, course in courses.items():
        if course["duration"] >= min_hours:
            result.append(name)
    return result


# 7. To-Do List Organizer
todos = {}

def add_task(name, priority):
    todos[name] = {"priority": priority, "status": "pending"}

def complete_task(name):
    if name in todos:
        todos[name]["status"] = "completed"

def filter_tasks(priority=None, status=None):
    result = []
    for name, task in todos.items():
        if (priority is None or task["priority"] == priority) and \
           (status is None or task["status"] == status):
            result.append(name)
    return result


# 8. Digital Wallet
wallet = {}

def add_expense(category, amount):
    if category in wallet:
        wallet[category] += amount
    else:
        wallet[category] = amount

def total_spent():
    return sum(wallet.values())

def expense_percentages():
    total = total_spent()
    if total == 0:
        return {}
    result = {}
    for category, amount in wallet.items():
        result[category] = (amount / total) * 100
    return result


# 9. Pet Adoption Center
pets = []

def add_pet(name, species, age):
    pets.append({"name": name, "species": species, "age": age})

def find_by_species(species):
    result = []
    for pet in pets:
        if pet["species"] == species:
            result.append(pet)
    return result

def older_than(age):
    result = []
    for pet in pets:
        if pet["age"] > age:
            result.append(pet)
    return result


# 10. Gym Membership System
members = {}

def register_member(name, plan, status):
    members[name] = {"plan": plan, "status": status}

def change_plan(name, new_plan):
    if name in members:
        members[name]["plan"] = new_plan

def unpaid_members():
    result = []
    for name, member in members.items():
        if member["status"] == "late":
            result.append(name)
    return result

