import sqlite3
import csv
import zipfile
import os


FILENAME = 'db.sqlite'
TEMP_LOCATION = 'temp/'

HEADERS = [
    "Transaction Date",
    "Amount",
    "Notes",
    "Imported Description",
    "Account Name",
    "Account Type",
    "Account Off Budget",
    "Account Closed",
    "Category",
    "Category Is Income",
    "Category Group",
    "Payee"
]

TRANSACTION_QUERY = """
SELECT
	substr(t.date,1,4) || '-' || substr(t.date,5,2) || '-' || substr(t.date,7,2) AS "date",
	t.amount/100.0000,
	t.notes,
	t.imported_description,
	a.name,
	a.type,
	a.offbudget,
	a.closed,
	c.name AS "category",
	c.is_income,
	cg.name AS "category_group",
	p.name AS "payee"
FROM transactions t
	LEFT JOIN accounts a ON t.acct = a.id
	LEFT JOIN categories c ON t.category = c.id
	LEFT JOIN category_groups cg ON c.cat_group = cg.id
	LEFT JOIN payees p ON t.description = p.id
WHERE
t.tombstone = 0
AND t.starting_balance_flag = 0
AND t.transferred_id IS NULL
ORDER BY t.date desc
"""

def main():

    zipPath = None
    csvPath = None

    while True:
        try:
            zipPath = input('Enter path to export zip:')

            if (not os.path.exists(zipPath)):
                raise Exception(f'File {zipPath} does not exist')

            break

        except Exception as err:
            print(err)

    csvPath = input('Enter output csv path:')

    if (not csvPath):
        csvPath = 'ActualTo.csv'

    # extract archive
    archive = zipfile.ZipFile(zipPath, 'r')
    archive.extract(FILENAME, TEMP_LOCATION)

    # read sqlite3
    con = sqlite3.connect(TEMP_LOCATION + FILENAME)
    cur = con.cursor()

    res = cur.execute(TRANSACTION_QUERY)

    # Write to csv
    with open(csvPath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(res)

    con.close()
    # remove temp sqlite.db
    os.remove(TEMP_LOCATION + FILENAME)


if __name__ == '__main__':
    main()
