
from rich.console import Console
from rich.table import Table

from .storage import load_employees,save_employees
from .validators import parse_salary, is_valid_email
from .models import add_employee

def show_employees():
    employees = load_employees()

    table = Table(title="Employees")

    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Department", style="yellow")
    table.add_column("Salary", justify="right")

    for emp in employees:
        table.add_row(
            str(emp["id"]),
            emp["name"],
            emp["department"],
            f"{emp['salary']:,.2f}"
        )

    console = Console()
    console.print(table)


def main():
    employees = load_employees()

    while True:
        print("\n=== Employee Manager ===")
        print("1. List employees")
        print("2. Add employee")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_employees()

        elif choice == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            department = input("Department: ").strip()
            salary = parse_salary(input("Salary: "))

            if not name or not department or salary is None or not is_valid_email(email):
                print("Invalid input - employee not added.")
                continue
            add_employee(
                employees, name, email, department, salary
            )
            save_employees(employees)
            print("Employee added successfully.")

        elif choice == "3":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
