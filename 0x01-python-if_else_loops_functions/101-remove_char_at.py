#!/usr/bin/python3
def remove_char_at(str, n):
    i = f"{str[:n]:s}{str[(n + 1):]}" \
        if n >= 0 else str
    return i
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security

