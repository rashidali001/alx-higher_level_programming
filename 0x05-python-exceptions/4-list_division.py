#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division = []
    i = 0
    while i < list_length:
        value = 0
        try:
            value = my_list_1[i] / my_list_2[i]
            division.append(value)
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("Out of range")
        except TypeError:
            print("wrong type")
        except ValueError:
            print("division by 0")
        finally:
            division.append(value)
        i += 1
    return division
