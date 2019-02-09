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
        line = line.replace("\n", "") # strip newlines
        if line == "END":
            break
        else:
            if i % 4 == 1:
                person = {}
                names = line.split(" ")
                person["firstname"] = names[0]
                person["lastname"] = names[1]
            elif i % 4 == 2:
                person["age"] = line
            elif i % 4 == 3:
                person["gender"] = line
            else:
                results = line.split(",")
                person["tsh"] = results[1:]
                people.append(person)
                
            i+=1

    fileobj.close()

    return people

def get_diagnosis(people):
    for person in people:
        if float(min(person["tsh"])) < 1.0:
            person["diagnosis"] = "hyperthyroidism"
        elif float(min(person["tsh"])) > 4.0:
            person["diagnosis"] = "hypothyroidism"
        else:
            person["diagnosis"] = "normal thyroid function"

    return people

if __name__ == "__main__":
    filename = "test_data.txt"
    people = read_text_file(filename)
    people = get_diagnosis(people)
    print(people)
