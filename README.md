# Infilect_Assignment_SDE
This project implements a FastAPI application for processing matrices and finding maximal rectangle areas within them. It provides an API endpoint where users can submit matrices, and the application returns the maximal rectangle area present within each matrix.

Setup this project By 
1. Clone this repo
`git clone https://github.com/aryagirigoudar/Infilect_Assignment_SDE.git`
2. Install Dependencies:
Navigate to your project directory and install the required dependencies using pip:
Copy code
`pip install -r req.txt`
Ensure you have all the required dependencies listed in requirements.txt, including fastapi, uvicorn, psycopg2, and any others.
3. Set Up Environment Variables:
If you're using environment variables for database connection details or other sensitive information, make sure to set them up. You can use a .env file or set them directly in your environment.
4. Run the Database:
Make sure your PostgreSQL database server is running. If not, start it using your preferred method.
5. Run the FastAPI Application:
Run your FastAPI application  using uvicorn:
`uvicorn app:app.py --reload`
Here, app:app indicates the module and instance of the FastAPI application. --reload enables auto-reloading for development.
6. Accessing the API:
Once the application is running, you can access the API at http://localhost:8000 by default. You can make POST requests to http://localhost:8000/execute/ to process matrices.

For Database table Structure
I have included .sql file download and install pgAdmin 
and import using sql file 
