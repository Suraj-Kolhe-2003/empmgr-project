
# empmgr/report.py

def department_summary(employees):
    """Return employee count and average salary per department."""
    summary = {}

    for emp in employees:
        department = emp["department"]

        if department not in summary:
            summary[department] = {
                "headcount": 0,
                "total_salary": 0
            }

        summary[department]["headcount"] += 1
        summary[department]["total_salary"] += emp["salary"]

    for department in summary:
        count = summary[department]["headcount"]
        total = summary[department]["total_salary"]

        summary[department]["average_salary"] = total / count

    return summary
