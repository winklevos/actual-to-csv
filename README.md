# actual-to-csv

Extracts CSV from Actual export/backup

This Python script takes an [export](https://actualbudget.github.io/docs/Getting-Started/using-actual/settings#export) from Actual budget and create a flat csv for use in Excel.

## Requirements

- Actual Budget Export
- Python3 ([how to run](https://realpython.com/run-python-scripts/))

## Running

1. Clone the source or script to your local machine
2. Run the [script](/src/main.py)
3. Input the full path to the Actual export `.zip`
4. (Optional) Input a full path for the resulting `.csv`

## Outputs

### Includes

- All transactions from all closed and open accounts

### Excludes

- Deleted transactions
- Starting balance transactions
- Transfer transactions

### Fields

- Transation Date
- Amount
- Notes
- Imported Description
- Account Name
- Account Type
- Account Off Budget
- Account Closed
- Category
- Cateogry Is Income
- Category Group
- Payee

