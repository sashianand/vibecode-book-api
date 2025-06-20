# VibeCode Book API

A FastAPI application for managing a collection of books and their reviews.

## Features

- Get a list of all books.
- Add a new book.
- Add a review to a book.
- CORS enabled for all origins.
- In-memory data storage.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd VibeCode
    ```

2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Deployment

### Option 1: Vercel (Recommended)

1. Create an account at [Vercel](https://vercel.com/)
2. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```
3. Login to Vercel:
   ```bash
   vercel login
   ```
4. Deploy:
   ```bash
   vercel
   ```
5. For production deployment:
   ```bash
   vercel --prod
   ```

### Option 2: Railway

1. Create an account at [Railway](https://railway.app/)
2. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```
3. Login to Railway:
   ```bash
   railway login
   ```
4. Initialize and deploy:
   ```bash
   railway init
   railway up
   ```

### Option 3: Render

1. Create an account at [Render](https://render.com/)
2. Connect your GitHub repository
3. Create a new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Option 4: Heroku

1. Create an account at [Heroku](https://heroku.com/)
2. Install Heroku CLI
3. Deploy:
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

## API Endpoints

- `GET /books`: Retrieve a list of all books.
- `POST /books`: Add a new book to the library.
- `POST /books/{book_id}/reviews`: Add a review to a specific book. 