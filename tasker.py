# test - 456
# 123
# SHELLSHOCK
# 456
import argparse #yuliakordunova for irina
# 45
#balabuda
#Valeriia Balatska
import argparse #yuliakordunova
import json  # We use JSON to store date to file
import datetime


def get_current_date(format):
    # Python is well know
    # for hard work with time
    # https://www.programiz.com/python-programming/datetime/current-datetime
    now = datetime.datetime.now()
    return now.strftime(format)

def get_args():
    parser = argparse.ArgumentParser(description='pyTasker - easy tasker sample')
    parser.add_argument(
        '--create',
        help="Interactive task creation"
    )
    parser.add_argument(
        '--modify',
        help="Interactive task modification"
    )
    parser.add_argument(
        '--delete',
        help="Interactive task deletion"
    )
    parser.add_argument(
        '--show',
        help="Show current agenda"
    )
    parser.add_argument(
        '--show-date',
        help="Show agenda for some date"
    )
    args = parser.parse_args()
    return args

def get_db():
    try:
        # If data available and we can read
        # we convert is to JSON format
        with open(DB_FILE, 'r') as db_read_file:
            db = json.load(db_read_file)
        return db
    except ValueError:
        # But!
        # If it is empty, will get Error: Cant load empty data!
        # If so, we will catch those error, and Handle It by using {}
        # empty dict. Empty dict is not empty data, and json.loads
        # knows how to read it!
        print "[!!] No data in DB."
        return {}

def create():
    # Input: https://www.geeksforgeeks.org/taking-input-in-python/
    name = str(raw_input("Name of task:"))
    date = str(raw_input("Date of task:"))
    db[date] = name


def main():
    args = get_args()

    db = get_db()
    db["today"] = TODAY

    if args.create:
        create(db)


    print db
    with open(DB_FILE, 'w') as db_write_file:
        json.dump(db, db_write_file, sort_keys=True, indent=4)
    #print(dump_db)

    # f.write(dump_db)
    # f.close()


# Config
DB_FILE='tasker.db'
FORMAT="%Y/%m/%d"# %H:%M:%S"
TODAY=get_current_date(FORMAT)

if __name__ == '__main__':
    print("pyTasker")
    main()
