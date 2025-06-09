# BRUR Payment System

Our university built a semi-online semester fee payment system which I didn't like. So, I decided to experiment and see if it was possible to make a better system. This website is just for demo purposes, not for actual usage.

## Live website

https://brur-pay.mahmudul.com.bd/

## Password for departments

Password for all departments is the same: `1234`

Department usernames include:

- cse
- eee
- eng
- math
- bengali
- chemistry

> **Note:** Not all usernames are included.

## Features

1. Accept payment from students
2. Automatically send email to user on payment
3. Automatically send email to user on payment updates
4. Automatically send email to user on payment verification
5. Automatically send email to user on payment denial
6. Separate admin panel for each department

## Known limitations

- Not suitable for multi-year payment receiving

## Known bugs

There are no known bugs. If you find any, please report them.

## Future plan

- Complete multi-year payment receiving system
- Separate student and teacher accounts
- Improve user interface
- Integrate Bkash payment gateway

> **Note:** Currently I'm busy with my exams, so I couldn't simulate many circumstances. I'll try to make this project better as soon as I'm free.

## Tech Stack

- Python 3.9+
- Django 3.2
- PostgreSQL (ArrayField support)
- HTML, CSS (Bootstrap)
- Deployed on Heroku

## Requirements

- Python 3.10 or newer
- pip
- PostgreSQL database server (or use SQLite for demo)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/brur-payment.git
   cd brur-payment
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # PowerShell
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create a superuser for Django admin:
   ```bash
   python manage.py createsuperuser
   ```

## Configuration

- Rename `.env.example` to `.env` and update the following settings:
  - `SECRET_KEY`
  - `DATABASE_URL` (e.g., PostgreSQL connection)
  - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`

## Usage

- Start the development server:
  ```bash
  python manage.py runserver
  ```
- Visit the home page at `http://localhost:8000/`
- Department staff can log in via `http://localhost:8000/accounts/login/` and manage payments under each department's admin panel.
- Students can submit payments at `http://localhost:8000/payment/` and recover codes at `http://localhost:8000/pay-code/`

## Project Structure

```
brur-payment/
├── BRUR_payment/         # Django project settings
├── easy_admin/           # Department admins views and URLs
├── payment/              # Payment models, views, templates
├── users/                # Custom user model
├── templates/            # Base and email templates
├── requirements.txt
├── README.md
└── manage.py
```
