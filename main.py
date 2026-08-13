STATUS_OPTIONS = {
    1: "Applied",
    2: "Interview",
    3: "Offer",
    4: "Rejected"
}

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
            print(f"\n{i}. {v['company']} - {v['position']} - {v['status']}")

    else:
        print("\nThere is no application!\n")   
    

def show_menu():
    txt = """
=== Job Application Tracker ===
1. Add Job
2. List Jobs
3. Update Status
4. Exit

Select an option:
"""

    slt = input(f"{txt}")

    if slt.isdigit():
        slt = int(slt)
        if 0 < slt < 5:
            return slt
        else:
            print("Invalid option")
            return None
    
    else:
        print("Invalid option")
        return None

def take_status():
    status_menu = """
    Select status:

1. Applied
2. Interview
3. Offer
4. Rejected
"""
    status_no = input(f"{status_menu}")

    if status_no.isdigit():
        status_no = int(status_no)
        if status_no in STATUS_OPTIONS.keys():
            return STATUS_OPTIONS.get(status_no)
    
    return None

def update_status():
    if not applications:
        print("There is no application!")

    else:
        list_jobs()
        app_number = input("\nSelect application number:")
        if app_number.isdigit():
            app_number = int(app_number)

            if 0 < app_number <= len(applications):
                status = None

                while True:
                    status = take_status()
                    if status is not None:
                        applications[app_number-1]["status"] = status
                        print("Status updated successfully.")
                        break
            else:
                print("Invalid option")
        else:
            print("Invalid option")
            

def main():
    slt = show_menu()

    if slt is not None:
        if slt == 1:
            print("Add Job selected")
            
            company = input("Company: ")
            position = input("Position: ")
            status = None

            while True:
                status = take_status()
                if status is not None:
                    break
                print("Enter a valid option")

            add_job(company, position, status)
            print("\nJob added successfully.")

        elif slt == 2:
            print("List Jobs selected")
            list_jobs()

        elif slt == 3:
            update_status()


        elif slt == 4:
            print("Goodbye!")

    return slt



if __name__ == "__main__":
    res = None

    while True:
        res = main()
        if res == 4:
            break

