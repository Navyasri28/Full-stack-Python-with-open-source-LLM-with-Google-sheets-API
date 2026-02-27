# Full-Stack Python with Google Sheets API

A FastAPI-based web application that integrates with Google Sheets for user data management, featuring a modern **Cyber-Glass** frontend.

🔗 **Google Sheet:** [View Sheet](https://docs.google.com/spreadsheets/d/1qKJ8URimPA9o-3IcWnqjAyXsNhNOeWiqZsi7L3mnhZY/edit?usp=sharing)

## Features

- **Add Users** — Submit username & password to Google Sheets via API
- **View Users** — Fetch and display all users in a dynamic table
- **Delete Users** — Remove users directly from the sheet
- **Cyber-Glass UI** — Premium glassmorphism design with animations

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Uvicorn |
| Sheets Integration | gspread, Google OAuth2 |
| Frontend | HTML, CSS, JavaScript |
| Design | Glassmorphism, Space Grotesk font |

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Navyasri28/Full-stack-Python-with-open-source-LLM-with-Google-sheets-API.git
   cd Full-stack-Python-with-open-source-LLM-with-Google-sheets-API
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn gspread google-auth
   ```

3. **Add your credentials**
   - Place your Google Service Account `credentials.json` in the project root
   - Share the Google Sheet with your service account email as **Editor**

4. **Run the app**
   ```bash
   python main.py
   ```

5. **Open in browser**
   ```
   http://localhost:8000
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the frontend UI |
| `GET` | `/users` | Get all users from the sheet |
| `POST` | `/add-user` | Add a new user (`{ "username": "...", "password": "..." }`) |
| `DELETE` | `/delete-user/{username}` | Delete a user by username |

## Project Structure

```
├── main.py            # FastAPI app with endpoints
├── sheets_util.py     # Google Sheets helper functions
├── credentials.json   # Service account credentials (not tracked)
├── static/
│   ├── index.html     # Frontend UI
│   ├── style.css      # Cyber-Glass styling
│   └── script.js      # API interaction logic
└── README.md
```
