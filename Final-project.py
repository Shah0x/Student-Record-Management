students = []
def add_student():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    student = {"id": id, "name": name, "marks": marks}
    students.append(student)
    print("Student added.")
def view_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
def search_by_id():
    id = input("Enter ID to Search: ")
    for s in students:
        if s["id"] == id:
            print(f"Found: ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
            return
    print("Not found.")
def search_by_name():
    name = input("Enter Name to Search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
            return
    print("Not found.")
def bubble_sort_by_marks():
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j]["marks"] > students[j + 1]["marks"]:
                students[j], students[j + 1] = students[j + 1], students[j]
    print("Sorted by Marks using Bubble Sort.")
def selection_sort_by_name():
    n = len(students)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[j]["name"].lower() < students[min_idx]["name"].lower():
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]

    print("Sorted by Name using Selection Sort.")
while True:
    print("\n====== Student Record Menu ======\n")
    print("-- [1] Add Student")
    print("-- [2] View Students")
    print("-- [3] Search by ID")
    print("-- [4] Search by Name")
    print("-- [5] Sort by Marks (Bubble Sort)")
    print("-- [6] Sort by Name (Selection Sort)")
    print("-- [7] Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_by_id()
    elif choice == '4':
        search_by_name()
    elif choice == '5':
        bubble_sort_by_marks()
    elif choice == '6':
        selection_sort_by_name()
    elif choice == '7':
        print(">>>>>>> Exiting... Done! <<<<<<<")
        break
    else:
        print("__________________________")
        print("Invalid choice. Try again.")
