# Whisky Distillery App

## Description
The Whisky Distillery App is a Flask-based web application that serves as a repository for whiskies and their associated distilleries. It allows users to store and retrieve detailed information about various whiskies, including tasting notes, distillery details, and more.

## Features
- Manage whiskies with detailed attributes:
  - Name
  - Distillery
  - Alcohol percentage
  - Whisky type (e.g., blended, single malt)
  - Bottle size (cl)
  - Price
  - Peated or not
  - Negotiant (if applicable)
  - Tasting notes (nose, appearance, palate, finish)
  - User tasting details (rating, date)
  - Photo
- Manage distillery details:
  - Name
  - Country
  - Notes
- SQLite database support with SQLAlchemy and Flask-Migrate for version control.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd whisky_distillery_app
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Directory Structure
```
whisky_distillery_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   └── static/
├── migrations/
├── config.py
├── run.py
├── requirements.txt
├── README.md
```

## Requirements
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## Contributing
Feel free to fork this repository and submit pull requests. Any contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
