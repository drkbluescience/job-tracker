from database import init_db, drop_tables, insert, fetch_all, update

STATUS_OPTIONS = {
    1: "Applied",
    2: "Interview",
    3: "Offer",
    4: "Rejected"
}

def add_job(company, position, status):
    job_id = insert(
        "applications",
        {
            "company": company,
            "position": position,
            "status": status
        }
    )

    return job_id


def list_jobs():
    jobs = fetch_all("applications")

    if jobs:
        for job in jobs:
            print(
                f"\n{job[0]}."
                f"{job[1]} - "
                f"{job[2]} - "
                f"{job[3]}"
            )

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
        return STATUS_OPTIONS.get(status_no)
    
    return None

def update_status():
    jobs = fetch_all("applications")

    if not jobs:
        print("There is no application!")
        return
    
    list_jobs()

    app_id = input("\nSelect application ID:")

    if not app_id.isdigit():
        print("Invalid application ID.")
        return
            
    app_id = int(app_id)

    job_ids = [job[0] for job in jobs]

    if app_id not in job_ids:
        print("Application not found.")
        return
    
    while True:
        status = take_status()

        if status is not None:
            break

        print("Enter a valid option.")
    
    updated_rows = update("applications", 
                            {"status": status},
                            "id = ?",
                            (app_id,))
    
    if updated_rows > 0:
        print("\nStatus updated successfully.")
    else:
        print("\nStatus could not be updated.")

            

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

            job_id = add_job(company, position, status)

            if job_id is not None:
                print(f"\nJob added successfully. ID: {job_id}")
            else:
                print("\nJob could not be added.")

        elif slt == 2:
            print("List Jobs selected")
            list_jobs()

        elif slt == 3:
            update_status()


        elif slt == 4:
            print("Goodbye!")

    return slt



if __name__ == "__main__":
    init_db()
    tables = ["products"]
    # drop_tables("jobs.db", tables=tables)

    res = None

    while True:
        res = main()
        if res == 4:
            break

