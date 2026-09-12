# Central Database of Dealerships & Customer Reviews Portal

A modern Full-Stack Dealerships and Reviews web application built as part of the IBM Full Stack Software Developer Capstone Project. This platform centralizes car dealerships across the United States, allowing customers to view dealership details, browse sentiment-analyzed reviews, submit verified reviews, and filter dealerships by state.

---

## Architecture & Microservices

The application is structured around a multi-tier microservices architecture:

1. **Dealerships Website (Django Application)**
   - **User Management & Authentication**: Secure registration, login, logout, and role-based permissions via Django's authentication system.
   - **Car Inventory Management**: SQLite database storing `CarMake` and `CarModel` models with full Django admin interface integration.
   - **Django Proxy Service**: Unified API gateway routing client requests to backend Express and Sentiment Analyzer microservices.
   - **Frontend Delivery**: Hosts responsive HTML static views (`Home.html`, `About.html`, `Contact.html`) and the built React Single Page Application (SPA).

2. **Dealerships & Reviews Service (Express + MongoDB)**
   - Express.js REST API backed by MongoDB.
   - Manages persistent collections for Dealerships and Customer Reviews.
   - Endpoints:
     - `GET /fetchDealers`: Retrieve all dealership locations across the country.
     - `GET /fetchDealers/:state`: Filter dealerships by US state.
     - `GET /fetchDealer/:id`: Retrieve single dealership details by ID.
     - `GET /fetchReviews`: Retrieve all customer reviews.
     - `GET /fetchReviews/dealer/:id`: Retrieve reviews specific to a dealer ID.
     - `POST /insert_review`: Insert a newly submitted customer review.

3. **Sentiment Analyzer Service (Flask + NLTK VADER)**
   - Python microservice running on IBM Cloud Code Engine / Docker container.
   - Analyzes textual reviews and classifies them into `positive`, `neutral`, or `negative` sentiment using NLTK's VADER SentimentIntensityAnalyzer.
   - Endpoint:
     - `GET /analyze/:text`: Analyzes review sentiment in real-time.

4. **Modern React Frontend**
   - Built with React 18 and React Router v6.
   - Interactive components:
     - **Dealers**: Table of dealerships with instant state filtering and review access.
     - **Dealer Details**: Rich dealer overview cards displaying customer reviews with sentiment indicator icons.
     - **Post Review**: Review submission form with vehicle make/model dropdowns, date picker, and purchase confirmation.
     - **Authentication**: Modal login dialog and dedicated registration page.

---

## Tech Stack

- **Backend**: Python 3, Django, Flask, Node.js, Express.js
- **Database**: SQLite (Django ORM), MongoDB (Mongoose)
- **Frontend**: React, React Router, HTML5, CSS3, Bootstrap 5, JavaScript (ES6+)
- **Natural Language Processing**: NLTK (VADER Sentiment Analyzer)
- **DevOps & Containers**: Docker, Docker Compose, Kubernetes, GitHub Actions (Flake8 & JSHint)

---

## Setup & Running Locally

### 1. Prerequisites
- Python 3.10+
- Node.js v18+ and npm
- Docker and Docker Compose (or local MongoDB)

### 2. Environment Configuration
Create or update `server/djangoapp/.env`:
```env
backend_url=http://localhost:3030
sentiment_analyzer_url=http://localhost:5050/
```

### 3. Start Dealerships & Reviews Service (Express + MongoDB)
```bash
cd server/database
docker-compose up -d
# Or run with Node and local MongoDB:
npm install
node app.js
```
The service runs on `http://localhost:3030`.

### 4. Start Sentiment Analyzer Microservice
```bash
cd server/djangoapp/microservices
pip install -r requirements.txt
python -m flask run --host=0.0.0.0 --port=5050
```
The service runs on `http://localhost:5050`.

### 5. Build the React Frontend
```bash
cd server/frontend
npm install
npm run build
```

### 6. Run the Django Server
```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Visit `http://localhost:8000/` in your browser.

---

## Continuous Integration & Linting

Continuous integration is managed via GitHub Actions in `.github/workflows/main.yml`:
- **Python Linting**: Automated checks across Python files with `flake8`.
- **JavaScript Linting**: Automated checks across JavaScript files with `jshint`.

---

## License

This project is licensed under the Apache License 2.0.