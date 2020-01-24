# Outline & Checklist for POS System w/ GUI

## Main Project Outline
- GUI
    1) Main Sales Page
        - Two entry fields for "Item" and "Price"
        - "Add to Sale" button to add entered items to current_sale and clear entry fields
        - "Get Total" button to get subtotal and total for current_sale
        - "New Sale" button to append current sale to json, create pandas dataframe with items and prices

    2) Sales Ledger
        - Will display sales ledger
        - Entry fields to specify start and end dates


    3) Totals Page
        - Buttons to display daily, monthly, and weekly totals
        - Will be accessing pandas dataframe to do calculations
        
    4) Stock Page
        - Page to display items listed in stock.json
        - Button to enter new items to be appended as dictionary to stock.json
        - Search, add, and modify values in item dictionaries

## TODO
- POS
    - Interface with dictionary
    - Add items
    - Return totals
    - Log sales
    - Data breakdown
    - Use pandas for CSV to log data
- GUI
    - Similar to Vend
    - Drop down, searchable item menu
        - Try to keep dict small, so less to search through and don't need nested items
- Stock Dictionary
    - Items will be limited to basic types that span certain prices - can add more detail later if needed
    - Figure out stock dictionary entry and how to interface with json
