from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E1001\n"
        "Department: IT\n"
        "Salary: 60000"
    )

    assert employee_details("Alice", "E1001", "IT", 60000) == expected_output