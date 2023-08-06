import pkgutil
import json
import curses

from .periodic_table import periodicTable

def main():
    elements = json.loads(pkgutil.get_data(__name__, "elements.json"))
    ptable = periodicTable(elements)
    curses.wrapper(ptable.main)

if __name__ == "__main__":
    main()
