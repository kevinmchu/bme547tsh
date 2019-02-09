# bme547tsh

This is the TSH testing assignment for BME 547, Spring 2019.

The python files are tsh.py and test_test.py

## tsh.py

This program takes a txt file containing personal information. To change the read in file, go to the if __name__ == "__main__" section and replace filename with the correct name of the file.  The txt file must be formatted as follows:

```
Firstname Lastname
Age
Gender
TSH, result1, result2, result3, ...
```

Alternatively, the age and gender lines may be switched, and the code will produce the expected output.

The program sorts the TSH results in ascending order and diagnoses the patient's thyroid function based on their TSH results. This program creates json files with the following information:

```
Firstname
Lastname
Age
Gender
Diagnosis
TSH
```

## test_tsh.py

This program implements unit tests for tsh.py.
