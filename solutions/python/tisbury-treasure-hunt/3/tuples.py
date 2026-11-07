"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[-1]    

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return tuple(azara_record[-1]) == rui_record[1]

def create_record(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return azara_record + rui_record
    return "not a match"

def clean_up(records):
    result = ""
    for record in records:
        cleaned_record = (record[0], record[2], record[3], record[4])
        result += str(cleaned_record) + "\n"
    return result
