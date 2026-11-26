#!/usr/bin/env python3
"""One Star for Monday — prints a one-star review of Monday as a restaurant, one line.

The review works like a real diner's complaint: a bad table by the
kitchen, yesterday's coffee, today's meetings, and a bill for the week.
"""
LINE = "One star. Monday sat me by the kitchen, served yesterday's coffee with today's meetings, and billed me for the week."

def get_line():
    """Return the one-star review line."""
    return LINE


if __name__ == "__main__":
    print(get_line())
