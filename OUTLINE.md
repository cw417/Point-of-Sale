# Outline & Checklist for POS System w/ GUI

## Main Project Outline
- GUI
    1) Main Sales Page
        - LABELS:
            - Please type item to search for
            - Current Sale
                - Display items in current sale
                - Display sale totals
                    - Total w/ tax
                    - Total w/o tax
        - FIELD: Entry field for item search
        - BUTTON: Add item to sale
        - BUTTON: Remove item from sale (need to pop up next to each item?)
        - BUTTON: Enter custom price
            - FIELD: Space for float entry
                - Will pop up on button press
        - BUTTON: Clear Sale
        - BUTTON: Complete Sale
        - BUTTON: Add discount
            - FIELD: Enter discount by $
            - FIELD: Enter discount by %
            - LABELS:
                - Enter $
                - Enter %
                - Display discount $ total
                - Display discount % total
    2) Sales Ledger
        - Will display a list of the daily sales
        - BUTTON: Void Sale
    3) Totals Page
        - Show daily sales totals when on main Totals page
            - Can change to Monthly or Yearly totals w/ buttons
        - LABELS:
            - Total w/o tax
            - Total w/ tax
            - Total Debit
            - Total Credit
            - Total Cash
        - BUTTON: Change to specific date
            - Interface w/ calendar, or type YYYMMDD value?
        - BUTTON: Filter by YMD
        - BUTTON: Filter by Y/M/D Total
        - BUTTON: Display spreadsheet
        - BUTTON: Display
    4) Stock Page
        - Display stock items from dictionary
        - LABELS:
            - Item
            - Wholesale Price
            - Sales Price
        - BUTTON: Add new item
        - BUTTON: Remove item

## TODO
- POS
    - Interface with dictionary
    - Add items
    - Return total w/ & w/o tax
    - Log sales
    - Daily, monthly, yearly totals
    - Use pandas for CSV to log data
- GUI
    - Similar to Vend
    - Drop down, searchable item menu
        - Try to keep dict small, so less to search through and don't need nested items
- Stock Dictionary
    - Items will be limited to basic types that span certain prices - can add more detail later if needed
    - Figure out stock dictionary entry keys
