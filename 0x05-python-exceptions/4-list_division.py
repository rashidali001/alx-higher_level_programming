#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division = []
    i = 0
    while i < list_length:
        try:
            value = my_list_1[i] / my_list_2[i]
            division.append(value)
        except ZeroDivisionError:
            print("division by 0")
            division.append(0)
        except IndexError:
            print("Out of range")
            division.append(0)
        except TypeError:
            print("wrong type")
            division.append(0)
        except ValueError:
            division.append(0)
        finally:
            pass

        i += 1
    return division
