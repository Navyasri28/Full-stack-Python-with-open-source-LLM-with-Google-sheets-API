import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Path to the service account credentials file
CREDENTIALS_FILE = 'credentials.json'

def get_sheets_client():
    """Authenticates and returns a gspread client."""
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPE)
    client = gspread.authorize(creds)
    return client

def get_worksheet(sheet_url, worksheet_name=None):
    """Opens a Google Sheet by URL and returns a worksheet."""
    client = get_sheets_client()
    sh = client.open_by_url(sheet_url)
    if worksheet_name:
        return sh.worksheet(worksheet_name)
    return sh.get_worksheet(0)

def add_row(sheet_url, row_data):
    """Appends a row of data to the specified Google Sheet."""
    sheet = get_worksheet(sheet_url)
    sheet.append_row(row_data)
    return {"status": "success", "message": "Row added successfully"}

def get_all_records(sheet_url):
    """Retrieves all records from the specified Google Sheet."""
    sheet = get_worksheet(sheet_url)
    return sheet.get_all_records()

def delete_row(sheet_url, username):
    """Deletes a row from the specified Google Sheet based on the username."""
    sheet = get_worksheet(sheet_url)
    all_records = sheet.get_all_records()
    
    # Assuming the first column is 'username'
    # Row index in gspread is 1-indexed and header is row 1
    for i, record in enumerate(all_records):
        if record.get("username") == username:
            # i+2 because i starts at 0, and we add 2 (1 for header, 1 for 1-indexing)
            sheet.delete_rows(i + 2)
            return {"status": "success", "message": f"User {username} deleted successfully"}
    
    return {"status": "error", "message": f"User {username} not found"}
