from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: somu\n"
        "Employee ID: E306\n"
        "Department: IT\n"
        "Salary: 100000"
    )

    assert employee_details("somu", "E306", "IT", 100000) == expected_output
