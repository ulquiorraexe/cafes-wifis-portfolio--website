# Cafe Website Portfolio Project

This project is my first website built using Flask, SQLite, and HTML. The website displays information about various cafes, with each page dedicated to a specific cafe. The data is fetched from a SQLite database and rendered dynamically using Flask.

## Project Overview

The website consists of 21 HTML pages (`1.html` to `21.html`), each representing a different cafe. Each page provides the following information:

- Cafe name
- Location (London Bridge)
- Number of seats
- Coffee price
- Available amenities (e.g., phone calls, toilets, sockets, wifi)

### Technology Used:
- **Flask**: Web framework to render HTML templates and handle routing.
- **SQLite**: Database used to store information about cafes.
- **HTML**: Structure of the pages.
- **CSS**: For styling, included through external files.

### Features:
- Dynamic rendering of cafe data on individual pages.
- Each page shows unique details about the cafe, including its name, location, and amenities.
- Pages are accessible via routes like `/one`, `/two`, `/three`, ..., up to `/twenty-one`.

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ulquiorraexe/cafes-wifis-portfolio--website.git
   cd cafes-wifis-portfolio--website

2. **Set up a virtual environment:**
   
   For Python 3.x, create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies:**
   
   Install Flask and other required packages using pip:
   ```bash
   pip install flask

4. **Set up the database:**
   
   Ensure that the `cafes.db` SQLite database is located in the `instance/` directory. If it’s not already present, you may need to     create it based on your own database schema.

5. **Run the application:**

   Start the Flask development server:
   ```bash
   python main.py

6. **Open the website:**

   Navigate to `http://127.0.0.1:5002/` to view the website.

## File Structure

  - `main.py`: The Flask application that routes to various HTML pages and renders data from the SQLite database.
  - `templates/`: Contains all HTML files (`1.html` to `21.html`).
  - `static/`: Contains CSS and JavaScript files for styling and interactivity.

## Usage 

When you visit different routes of the site, such as `/one`, `/two`, etc., each will render a page with specific cafe details. You can modify and expand the database with more cafes, or adjust the HTML templates to display additional information.

## Future Improvements

  - Refactor the code to avoid repetition by using a loop to generate routes dynamically.
  - Add error handling for invalid database connections or missing data.
  - Integrate a more sophisticated front-end framework (e.g., React) for better interactivity.
  - Improve the design using a CSS framework like Bootstrap or Tailwind.

## License

This project does not have a license.
