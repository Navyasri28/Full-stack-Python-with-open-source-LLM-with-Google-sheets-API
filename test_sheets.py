import sheets_util

SHEET_URL = "https://docs.google.com/spreadsheets/d/1qKJ8URimPA9o-3IcWnqjAyXsNhNOeWiqZsi7L3mnhZY/edit?usp=sharing"

def test_connection():
    print("Testing connection to Google Sheets...")
    try:
        records = sheets_util.get_all_records(SHEET_URL)
        print("Success! Records found:", records)
    except Exception as e:
        print("Connection failed:", str(e))

if __name__ == "__main__":
    test_connection()
