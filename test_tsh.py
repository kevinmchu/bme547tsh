# test_tsh.py
# Author: Kevin Chu
# Last Modified: 2/14/19

import pytest
from tsh import get_diagnosis


@pytest.mark.parametrize("people, expected", [([{"firstname": "Anne",
                                                 "lastname": "Boynton",
                                                 "age": "45",
                                                 "gender": "Female",
                                                 "tsh": [3.5, 3.6, 1.8, 2.8,
                                                         1.9, 3.4, 3, 3.6,
                                                         3, 4]}],
                                               "normal thyroid function"),
                                              ([{"firstname": "Kamal",
                                                 "lastname": "Solaiman",
                                                 "age": "31",
                                                 "gender": "Male",
                                                 "tsh": [2.7, 1.4, 2.5, 3.1,
                                                         0.4, 1.8, 3.1, 3,
                                                         3.8, 0.9, 2.3]}],
                                               "hyperthyroidism"),
                                              ([{"firstname": "Larissa",
                                                 "lastname": "Webb",
                                                 "age": "46",
                                                 "gender": "Female",
                                                 "tsh": [6.3, 6.7, 6.3, 7.6,
                                                         2.1, 6.9, 7.1, 4.1,
                                                         7.2, 3.5, 2.9]}],
                                               "hypothyroidism"),
                                              ([{"firstname": "John",
                                                 "lastname": "Doe",
                                                 "age": "60",
                                                 "gender": "Male",
                                                 "tsh": [1, 1.2, 1.3, 1.4,
                                                         1.5, 2, 2.4, 1.5]}],
                                               "normal thyroid function"),
                                              ([{"firstname": "Jane",
                                                 "lastname": "Doe",
                                                 "age": "58",
                                                 "gender": "Female",
                                                 "tsh": [3.4, 2.7, 3.1, 3.2,
                                                         3.7, 2.9, 2.4, 3.7]}],
                                               "normal thyroid function"),
                                              ([{"firstname": "Bob",
                                                 "lastname": "Smith",
                                                 "age": "72",
                                                 "gender": "Male",
                                                 "tsh": [0.5, 0.9, 1.1, 0.4,
                                                         0.7, 0.8, 0.6, 1.2,
                                                         0.6, 0.8]}],
                                               "hyperthyroidism"),
                                              ([{"firstname": "Monte",
                                                 "lastname": "Swarup",
                                                 "age": "51",
                                                 "gender": "Male",
                                                 "tsh": [2.4, 3.1, 3.5, 3.6,
                                                         3.2, 3.3, 3.5, 3.8,
                                                         4.1, 3.6, 3.7, 3.8]}],
                                               "hypothyroidism")])
def test_get_diagnosis(people, expected):
    """Test the get_diagnosis function

    test_get_diagnosis performs unit tests on
    the get_diagnosis function from tsh.py.

    Args:
        people (list): list of dictionaries
        expected: the expected diagnosis

    Returns:
        nothing
    """
    people_updated = get_diagnosis(people)
    answer = (people_updated[0])["diagnosis"]

    assert answer == expected
