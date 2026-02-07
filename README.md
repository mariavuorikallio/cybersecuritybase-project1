# Cybersecurity Base - Project 1

* This is the first project for the Cybersecurity Base course (2026). 
* The application is a simple Django-based marketplace designed to demonstrate common web vulnerabilities based on the **OWASP Top 10 (2021)**.

**Note:** This application intentionally contains security vulnerabilities for educational purposes. Corresponding fixes are included as commented-out code in the same files.

----

## How to Install and Run

### 1. **Clone the repository:**
   ```bash
   git clone https://github.com/mariavuorikallio/cybersecuritybase-project1.git cd cybersecuritybase-project1
   ```
   
### 2. **Install Dependencies: Make sure you have Python installed. Install Django:**
   ```bash
   pip install django
   ```
   
### 3. **Database Setup: Run the migrations to set up the local SQLite database:**
   ```bash
   python manage.py migrate
   ```
   
### 4. **Run the Application: Start the development server:**
   ```bash
   python manage.py runserver
   ```
### The application will be available at http://127.0.0.1:8000/.

## Vulnerabilities and Fixes

This project demonstrates five security flaws based on the **OWASP Top 10: 2021** list. Each flaw is present in the active code, and its corresponding fix is provided as a commented-out code block directly below the vulnerability.

### Demonstrated Flaws:
* **A01:2021 – Broken Access Control:** * CSRF vulnerability in the "Add to Cart" functionality.
    * Unprotected checkout page accessible without authentication.
* **A03:2021 – Injection:** * SQL Injection vulnerability in the product search feature.
* **A05:2021 – Security Misconfiguration:** * Improper error handling in product details, leading to potential information disclosure.
* **A09:2021 – Security Logging and Monitoring Failures:** * Sensitive session data (cart contents) being printed to server logs.

For detailed descriptions and steps to reproduce each flaw, please refer to the project report.


