from src.pre_built.counter import count_ocurrences
import pytest


ERRORS = {
    "MISSING_PARAM": "missing 1 required positional argument: 'word'",
    "FILE_NOT_FOUND": 'data/file_that_does_not_exist.csv',
    "NO_PARAMS": "missing 2 required positional arguments: 'path' and 'word'",
}


def test_counter():
    assert count_ocurrences("data/jobs.csv", "marketing") == 1259
    assert count_ocurrences("data/jobs.csv", "MARKETING") == 1259
    with pytest.raises(TypeError, match=ERRORS["MISSING_PARAM"]):
        count_ocurrences("data/jobs.csv")
    with pytest.raises(FileNotFoundError, match=ERRORS["FILE_NOT_FOUND"]):
        count_ocurrences("data/file_that_does_not_exist.csv", "marketing")
    with pytest.raises(TypeError, match=ERRORS["NO_PARAMS"]):
        count_ocurrences()
