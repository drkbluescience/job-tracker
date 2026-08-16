⌘ + Space → Terminal: python3 --version

-------

mkdir -p ~/Projects/job-tracker
cd ~/Projects/job-tracker

-------

python3 -m venv .venv
source .venv/bin/activate

--------

which python

-------

touch main.py
touch .gitignore

-------

.gitignore içine kendin şunları yaz:

.venv/
__pycache__/
.DS_Store

-------------

git init

---------

job-tracker/
├── .venv/
├── .gitignore
└── main.py

---------

DB connection
      ↓
Generic CRUD
      ↓
Table whitelist
      ↓
Business logic


---------
database.py

get_connection()
      │
      ├── init_db()
      ├── insert()
      ├── fetch_all()
      ├── update()
      ├── delete()
      └── drop_tables()

---------

main.py
   │
   ├── Add Job
   │      ↓
   │    insert()
   │
   ├── List Jobs
   │      ↓
   │    fetch_all()
   │
   ├── Update Job
   │      ↓
   │    update()
   │
   └── Delete Job
          ↓
        delete()

---------

DB connection
      ↓
Generic CRUD
      ↓
Table whitelist
      ↓
Business logic

---------

enisezengin@Enise-MacBook-Pro job-tracker % sqlite3 jobs.db
SQLite version 3.51.0 2025-06-12 13:14:41
Enter ".help" for usage hints.
sqlite> .tables
applications  products    
sqlite> .tables
applications
sqlite> SELECT * FROM applications;
sqlite> .headers on
sqlite> .mode column
sqlite> 