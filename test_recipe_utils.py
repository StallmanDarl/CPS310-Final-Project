"""Tests for the Recipe & Meal Planner."""

import pytest, json

from recipe_utils import (
    assign_recipe_to_day,
    create_weekly_meal_plan,
    filter_by_category,
    load_config,
    load_recipes,
    search_by_ingredient,
    search_by_name,
)

def test_search_by_name_finds_partial_match():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "chicken")
    assert result == [{"name": "Chicken Alfredo", "category": "Dinner"}]


def test_search_by_name_is_case_insensitive():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "SMOOTHIE")
    assert result == [{"name": "Berry Smoothie", "category": "Snack"}]


def test_search_by_name_returns_empty_list_when_no_match():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert search_by_name(recipes, "pizza") == []


def test_filter_by_category_returns_matching_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]
    result = filter_by_category(recipes, "Dinner")
    assert result == [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]


def test_filter_by_category_is_case_insensitive():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert filter_by_category(recipes, "dinner") == [
        {"name": "Chicken Alfredo", "category": "Dinner"}
    ]


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "app_title": "Test Planner",
                "recipe_file": "recipes.json",
                "default_servings": 2,
            }
        ),
        encoding="utf-8",
    )
    result = load_config(config_file)
    assert result["app_title"] == "Test Planner"
    assert result["default_servings"] == 2


def test_load_recipes_reads_json(tmp_path):
    recipe_file = tmp_path / "recipes.json"
    sample = [
        {
            "name": "Test Recipe",
            "category": "Lunch",
            "servings": 2,
            "prep_time": 5,
            "cook_time": 10,
            "ingredients": [],
        }
    ]
    recipe_file.write_text(json.dumps(sample), encoding="utf-8")
    assert load_recipes(recipe_file) == sample


def test_search_by_ingredient_finds_matching_recipes():
    recipes = [
        {
            "name": "Chicken Alfredo",
            "ingredients": [
                {"name": "chicken breast"},
                {"name": "fettuccine"},
            ],
        },
        {
            "name": "Berry Smoothie",
            "ingredients": [
                {"name": "berries"},
                {"name": "milk"},
            ],
        },
    ]

    result = search_by_ingredient(recipes, "chicken")

    assert [recipe["name"] for recipe in result] == [
        "Chicken Alfredo"
    ]


def test_search_by_ingredient_is_case_insensitive():
    recipes = [
        {
            "name": "Chicken Alfredo",
            "ingredients": [
                {"name": "chicken breast"},
            ],
        }
    ]

    assert search_by_ingredient(recipes, "CHICKEN") == recipes


def test_search_by_ingredient_supports_partial_matches():
    recipes = [
        {
            "name": "Chicken Alfredo",
            "ingredients": [
                {"name": "chicken breast"},
            ],
        }
    ]

    assert search_by_ingredient(recipes, "breast") == recipes


def test_search_by_ingredient_returns_empty_when_no_match():
    recipes = [
        {
            "name": "Chicken Alfredo",
            "ingredients": [
                {"name": "chicken breast"},
            ],
        }
    ]

    assert search_by_ingredient(recipes, "tomato") == []


def test_search_by_ingredient_returns_empty_for_blank_search():
    recipes = [
        {
            "name": "Chicken Alfredo",
            "ingredients": [
                {"name": "chicken breast"},
            ],
        }
    ]

    assert search_by_ingredient(recipes, "   ") == []


def test_create_weekly_meal_plan_contains_seven_days():
    meal_plan = create_weekly_meal_plan()

    assert len(meal_plan) == 7

    assert list(meal_plan.keys()) == [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]


def test_create_weekly_meal_plan_starts_empty():
    meal_plan = create_weekly_meal_plan()

    assert all(recipe is None for recipe in meal_plan.values())


def test_assign_recipe_to_day():
    meal_plan = create_weekly_meal_plan()

    recipe = {
        "name": "Chicken Alfredo",
        "category": "Dinner",
    }

    assign_recipe_to_day(meal_plan, "Monday", recipe)

    assert meal_plan["Monday"] == recipe


def test_assign_recipe_to_day_is_case_insensitive():
    meal_plan = create_weekly_meal_plan()

    recipe = {"name": "Berry Smoothie"}

    assign_recipe_to_day(meal_plan, "monday", recipe)

    assert meal_plan["Monday"] == recipe


def test_assign_recipe_to_day_replaces_existing_recipe():
    meal_plan = create_weekly_meal_plan()

    first_recipe = {"name": "Chicken Alfredo"}
    second_recipe = {"name": "Tomato Basil Pasta"}

    assign_recipe_to_day(meal_plan, "Monday", first_recipe)
    assign_recipe_to_day(meal_plan, "Monday", second_recipe)

    assert meal_plan["Monday"] == second_recipe


def test_assign_recipe_to_invalid_day_raises_error():
    meal_plan = create_weekly_meal_plan()

    recipe = {"name": "Chicken Alfredo"}

    with pytest.raises(ValueError):
        assign_recipe_to_day(meal_plan, "Funday", recipe)
