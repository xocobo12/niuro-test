# Niuro Test P#latform

This platform is a test for Streamlit and its serves to stablish conventions inside the team.


## How to run the project

### Create virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Run the project

```bash
streamlit run app.py
```

## Conventions

- Python with linter flake8.
- Commit messages with conventional commits.
- Branch naming with the following pattern: `{type}/{description}`.
- Folder structure.

## Technologies

- Python 3.10.15

## Dependencies 
The project uses the following libraries (detailed in `requirements.txt`):

  - `setuptools>=69.0.2`: Package management and distribution utilities.
  - `streamlit==1.38.0`: Framework for building interactive web apps for data analysis and machine learning.
  - `python-dotenv==1.0.0`: For managing environment variables.
  - `SQLAlchemy>=2.0.0`: A powerful ORM for database interactions.
  - `bcrypt==4.0.1`: Secure password hashing for authentication.
  - `PyJWT>=2.5.0`: JSON Web Token library for authentication.
  - `numpy>=1.26.0`: Essential package for numerical computations.
  - `pandas>=2.1.4`: Data manipulation and analysis.
  - `matplotlib==3.8.0`: Data visualization library.
  - `pytest>=7.5.0`: Framework for running unit tests.
  - `flake8==6.1.0`: Linting tool for ensuring code quality.
  - `python-decouple==3.8`: Manage configuration settings easily.