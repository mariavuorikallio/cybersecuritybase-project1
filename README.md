# Cybersecurity Base - Project 1

* This is the first project for the Cybersecurity Base course (2026). 
* The application is a simple Django-based marketplace designed to demonstrate common web vulnerabilities (OWASP Top 10).

----

## How to Install and Run

### 1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mariavuorikallio/cybersecuritybase-project1.git](https://github.com/mariavuorikallio/cybersecuritybase-project1.git)
   cd cybersecuritybase-project1
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

## Vulnerabilities Included

### This project demonstrates the following flaws (OWASP 2021):
    
    * A01:2021-Broken Access Control (Checkout & CSRF issues)
    * A03:2021-Injection (SQL Injection in Search)
    * A05:2021-Security Misconfiguration (Unsafe error handling)
    * A09:2021-Security Logging and Monitoring Failures (Sensitive data logging)

The fixes for these flaws are included in the source code as commented-out blocks.Vulnerabilities Included
