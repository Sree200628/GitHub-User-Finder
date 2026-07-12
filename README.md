# GitHub User Finder using Python API

## Project Overview

GitHub User Finder is a simple Python project that fetches public GitHub user details using the GitHub REST API. The user enters a GitHub username, and the application displays the user's public profile information.

## Features

* Search any public GitHub user
* Display user's name
* Display username
* Display followers count
* Display following count
* Display public repositories count
* Display profile URL
* Show **"User not found!"** for invalid usernames

## Technologies Used

* Python
* Requests Library
* GitHub REST API

## Project Structure

```
GitHub_User_Finder/
│── main.py
│── requirements.txt
└── README.md
```

## How to Run

1. Clone or download the project.
2. Install the required package:

```
pip install -r requirements.txt
```

3. Run the program:

```
python main.py
```

## Sample Output

```
Enter GitHub Username: octocat

Name: The Octocat
Username: octocat
Followers: 23264
Following: 9
Public Repositories: 8
Profile URL: https://github.com/octocat
```

## Future Improvements

- Display user's repositories
- Search history
- Dark mode
- Export user details to PDF or CSV
- Responsive design for mobile devices


## Author

Sreenithi B.
