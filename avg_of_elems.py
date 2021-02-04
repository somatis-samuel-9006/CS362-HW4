
def avg_of_elems(input_list):
    try:
        average = sum(input_list) / len(input_list)
        return average
    except ZeroDivisionError:
        return "The list is empty"



