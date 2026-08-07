def main():

    txt = """
=== Job Application Tracker ===
1. Add Job"
2. List Jobs"
3. Exit"

Select an option:
"""

    slt = int(input(f"{txt}"))
    
    if slt == 1:
        print("Add Job selected")
    elif slt == 2:
        print("List Jobs selected")
    elif slt == 3:
        print("Goodbye!")
    else:
        print("Invalid option")

    print(slt)


if __name__ == '__main__':
    main()

