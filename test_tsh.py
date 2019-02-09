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
                                               "hypothyroidism")])
def test_get_diagnosis(people, expected):
    people_updated = get_diagnosis(people)
    answer = (people_updated[0])["diagnosis"]

    assert answer == expected
