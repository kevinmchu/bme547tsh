def read_text_file(filename):
    """Read personal information from given file

    read_text_file takes a filename that contains information from
    various individuals. This information includes their first and
    last name, age, gender, and TSH test results. For each person,
    the function creates a dictionary with personal information.
    Each dictionary is then appended to a list (called people),
    which is returned from the function.

    Args:
        filename (string): name of file

    Returns:
        people (list): list with dictionaries containing info

    """
    # List where each element is a dictionary with personal info
    people = []

    # File object
    fileobj = open(filename, "r")

    # Line number
    i = 1

    # We create the person dictionary and store info as key-value pairs
    for line in fileobj:
        line = line.replace("\n", "")  # strip newlines
        if line == "END":
            break
        else:
            if i % 4 == 1:
                person = {}
                names = line.split(" ")
                person["firstname"] = names[0]
                person["lastname"] = names[1]
            elif i % 4 == 2 or i % 4 == 3:
                # Some age/gender lines are mixed up
                if line.isnumeric():
                    person["age"] = line
                else:
                    person["gender"] = line
            else:
                results = line.split(",")
                person["tsh"] = results[1:]
                people.append(person)

            i += 1

    fileobj.close()

    return people


def sort_tsh(people):
    """Sort tsh results in ascending order

    sort_tsh takes a list of dictionaries that contains
    information from various individuals. The function takes
    the TSH results and sorts them in ascending order.

    Args:
        people (list): list of dictionaries with personal info

    Returns:
        people_updated (list): list with sorted TSH results
    """
    people_updated = []
    for person in people:
        (person["tsh"]).sort()
        people_updated.append(person)

    return people_updated


def get_diagnosis(people):
    """Diagnose patient given TSH results

    get_diagnosis takes a list of dictionaries that contain
    information from various individuals. The function extracts
    the results for the tsh key. If the person has any test
    results < 1.0, they are diagnosed with hyperthyroidism.
    If they have any test results > 4.0, they are diagnosed with
    hypothyroidism. Otherwise, they are diagnosed as having normal
    thyroid function.

    Args:
        people (list): list of dictionaries with personal info

    Returns:
        people_updated (list): same as input but with diagnosis key-values
    """
    people_updated = []
    for person in people:
        if float(min(person["tsh"])) < 1.0:
            person["diagnosis"] = "hyperthyroidism"
        elif float(max(person["tsh"])) > 4.0:
            person["diagnosis"] = "hypothyroidism"
        else:
            person["diagnosis"] = "normal thyroid function"

        people_updated.append(person)

    return people_updated


def save_diagnoses(people):
    """Save patient information to json file

    save_diagnoses takes a list of dictionaries that contains
    information from various individuals. The function saves
    the information from each patient in their own json file.

    Args:
        people (list): list of dictionaries with personal info

    Returns:
        nothing
    """
    import json
    for person in people:
        filename = person["firstname"] + "-" + person["lastname"]
        save_file = open(filename, "w")
        json.dump(person, save_file)
        save_file.close()

    return


if __name__ == "__main__":
    filename = "test_data.txt"
    people = read_text_file(filename)
    people = sort_tsh(people)
    people = get_diagnosis(people)
    save_diagnoses(people)
