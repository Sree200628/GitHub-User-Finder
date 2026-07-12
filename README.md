
# GitHub User Finder using Python API

## Project Overview

GitHub User Finder is a Flask-based web application that uses the GitHub REST API to fetch and display public GitHub user profile information. Users can search for any public GitHub username and instantly view details such as profile picture, bio, company, location, followers, repositories, and profile link.
## Output
<img width="647" height="922" alt="Screenshot 2026-07-12 221327" src="https://github.com/user-attachments/assets/0d254892-dc28-42b5-b8ef-4408edef58e6" />
## Features

- Search any public GitHub user
- Display profile picture
- Display user's name
- Display username
- Display bio
- Display company
- Display location
- Display followers count
- Display following count
- Display public repositories count
- Display account creation date
- Open GitHub profile using profile URL
- Show **"User not found!"** for invalid usernames

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Requests Library
- GitHub REST API

---

## Project Structure

```text
GitHub_User_Finder/
│── app.py
│── main.py
│── requirements.txt
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## How to Run

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

4. Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Project Workflow

```text
User
   │
   ▼
Enter GitHub Username
   │
   ▼
Click Search
   │
   ▼
Flask Application
   │
   ▼
GitHub REST API
   │
   ▼
JSON Response
   │
   ▼
Display User Details
```

---

## Future Improvements

- Display user's repositories
- Add dark mode
- Save search history
- Export user details to PDF or CSV
- Improve mobile responsiveness

---

## Author

**Sreenithi B.**
