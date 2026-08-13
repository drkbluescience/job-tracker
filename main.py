applications = []

def add_job(company, position, status):
    job = {
    "company": company,
    "position": position,
    "status": status
}

    applications.append(job)


def list_jobs():
    if applications:
        for i, v in enumerate(applications, start=1):
            print(f"{i}. {v['company']} - {v['position']} - {v['status']}")

    else:
        print("\nThere is no application!\n")   
    

def show_menu():
    txt = """
=== Job Application Tracker ===
1. Add Job"
2. List Jobs"
3. Exit"

Select an option:
"""
    slt = input(f"{txt}")

    if slt.isdigit():
        slt = int(slt)
        if if 0 < slt < 4:
            return slt
        else:
            return None
    
    else:
        print("Invalid option")
        return None


def main():
    slt = show_menu()

    if slt is not None:
        if slt == 1:
            print("Add Job selected")
            
            company = input("Company: ")
            position = input("Position: ")
            status = input("Status: ")

            add_job(company, position, status)
            print("\nJob added successfully.")

        elif slt == 2:
            print("List Jobs selected")
            list_jobs()

        elif slt == 3:
            print("Goodbye!")

    return slt



if __name__ == "__main__":
    res = None

    while True:
        res = main()
        if res == 3:
            break

