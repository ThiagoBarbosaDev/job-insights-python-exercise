from src.pre_built.sorting import sort_by


mock = [
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2005-04-10"},
    {"min_salary": "2000", "max_salary": "10000", "date_posted": "2006-04-10"},
    {"min_salary": "5000", "max_salary": "5500", "date_posted": "2007-04-10"},
]


expected_min_salary = [
    {"min_salary": "2000", "max_salary": "10000", "date_posted": "2006-04-10"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2005-04-10"},
    {"min_salary": "5000", "max_salary": "5500", "date_posted": "2007-04-10"},
]


expected_max_salary = [
    {"min_salary": "2000", "max_salary": "10000", "date_posted": "2006-04-10"},
    {"min_salary": "5000", "max_salary": "5500", "date_posted": "2007-04-10"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2005-04-10"},
]


expected_date_posted = [
    {"min_salary": "5000", "max_salary": "5500", "date_posted": "2007-04-10"},
    {"min_salary": "2000", "max_salary": "10000", "date_posted": "2006-04-10"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2005-04-10"},
]


def test_sort_by_criteria():
    min_mock = mock
    max_mock = mock
    date_mock = mock
    sort_by(max_mock, "max_salary")
    assert max_mock == expected_max_salary

    sort_by(min_mock, "min_salary")
    assert min_mock == expected_min_salary

    sort_by(date_mock, "date_posted")
    assert date_mock == expected_date_posted
