# CPS 310 Final Project
## Recipe & Meal Planner

A Python-based recipe management and meal planning
application developed for CPS 310.

## Features

### Recipe Management
- Load recipes from JSON files.
- List all available recipes.
- Search recipes by name.
- Search recipes by ingredient.
- Filter recipes by category.
- View recipe details.

### Meal Planning
- Create a seven-day meal plan.
- Assign recipes to individual weekdays.
- View the current weekly meal plan.
- Replace previously assigned meals.

### Planned Features
- Generate grocery lists from weekly meal plans.

## Project Structure

- `app.py` - Main application and user interface.
- `recipe_utils.py` - Recipe and meal planning functions.
- `recipes.json` - Recipe data.
- `config.json` - Application configuration.
- `test_recipe_utils.py` - Automated tests.
- `requirements.txt` - Python dependencies.

## Requirements

- Python 3.12 or newer.
- Git.
- Dependencies listed in `requirements.txt`.

## Setup

### Windows

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the application:

```powershell
python app.py
```

## Running Tests

Run the complete test suite:

```powershell
python -m pytest -v
```

## Development

Features are developed on separate Git branches
and integrated into `main` through GitHub Pull Requests.

Automated tests are used to verify existing and
new application functionality.

## Future Development

- Generate grocery lists from weekly meal plans.
- Add Docker support.
- Configure automated testing with GitHub Actions.
- Expand documentation and security practices.
