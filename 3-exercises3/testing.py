from functions import *

def test_library():
    library.clear()
    add_book("1984", "George Orwell", 328)
    assert find_book("1984") == "book found"
    assert find_book("Unknown") == "Book not found."

def test_grades():
    grades.clear()
    add_student("Alice")
    add_grade("Alice", 90)
    add_grade("Alice", 70)
    assert get_average("Alice") == 80.0

def test_menu():
    menu.clear()
    add_dish("Pizza", 10.0, True)
    add_dish("Salad", 5.0, False)
    assert total_available_price() == 10.0
    change_availability()
    assert total_available_price() == 5.0

def test_warehouse():
    warehouse.clear()
    add_box("BoxA", 5)
    update_quantity("BoxA", 3)
    assert has_enough("BoxA", 8) == True
    assert has_enough("BoxA", 10) == False

def test_movies():
    movies.clear()
    add_movie("Inception")
    rate_movie("Inception", 5)
    rate_movie("Inception", 4)
    assert average_rating("Inception") == 4.5

def test_courses():
    courses.clear()
    add_course("Python", 50, 20)
    add_course("HTML", 20, 10)
    assert "Python" in filter_by_hour(40)
    assert "HTML" not in filter_by_hour(40)

def test_todos():
    todos.clear()
    add_task("Buy milk", "high")
    complete_task("Buy milk")
    result = filter_tasks(priority="high", status="completed")
    assert "Buy milk" in result

def test_wallet():
    wallet.clear()
    add_expense("food", 100)
    add_expense("transport", 50)
    percentages = expense_percentages()
    assert round(percentages["food"], 1) == 66.7
    assert round(percentages["transport"], 1) == 33.3

def test_pets():
    pets.clear()
    add_pet("Buddy", "dog", 5)
    result = older_than(3)
    assert result[0]["name"] == "Buddy"
    assert find_by_species("dog")[0]["name"] == "Buddy"

def test_gym():
    members.clear()
    register_member("John", "monthly", "late")
    assert "John" in unpaid_members()

def main():
    test_library()
    test_grades()
    test_menu()
    test_warehouse()
    test_movies()
    test_courses()
    test_todos()
    test_wallet()
    test_pets()
    test_gym()

main()
