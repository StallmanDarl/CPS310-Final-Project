
"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]


def search_by_ingredient(recipes, ingredient_name):
    """Return recipes containing an ingredient matching the search term."""
    ingredient_name = ingredient_name.strip().lower()

    if not ingredient_name:
        return []

    matching_recipes = []

    for recipe in recipes:
        for ingredient in recipe.get("ingredients", []):
            name = ingredient.get("name", "").lower()

            if ingredient_name in name:
                matching_recipes.append(recipe)
                break

    return matching_recipes


DAYS_OF_WEEK = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def create_weekly_meal_plan():
    """Create an empty meal plan containing all seven days."""
    return {day: None for day in DAYS_OF_WEEK}


def assign_recipe_to_day(meal_plan, day, recipe):
    """Assign a recipe to a specific day of the week."""
    matching_day = next(
        (existing_day for existing_day in meal_plan
         if existing_day.lower() == day.strip().lower()),
        None,
    )

    if matching_day is None:
        raise ValueError("Invalid day of the week.")

    meal_plan[matching_day] = recipe
