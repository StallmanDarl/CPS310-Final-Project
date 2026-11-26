"""CPS 310 Recipe & Meal Planner starter application."""

from recipe_utils import (
    assign_recipe_to_day,
    create_weekly_meal_plan,
    filter_by_category,
    load_config,
    load_recipes,
    search_by_ingredient,
    search_by_name,
)

def display_recipe(recipe):
    """Display one recipe in a readable format."""
    print(f"\n{recipe['name']}")
    print("-" * len(recipe["name"]))
    print(f"Category: {recipe['category']}")
    print(f"Servings: {recipe['servings']}")
    print(f"Prep time: {recipe['prep_time']} minutes")
    print(f"Cook time: {recipe['cook_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")


def list_recipes(recipes):
    """Display a numbered list of recipe names."""
    if not recipes:
        print("\nNo recipes found.")
        return

    print("\nRecipes")
    print("-------")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['name']} ({recipe['category']})")


def choose_recipe(recipes):
    """Prompt the user to select and view a recipe."""
    list_recipes(recipes)
    if not recipes:
        return

    try:
        selection = int(input("\nEnter recipe number: "))
    except ValueError:
        print("Invalid selection.")
        return

    if selection < 1 or selection > len(recipes):
        print("Invalid selection.")
        return

    display_recipe(recipes[selection - 1])



def main():
    """Run the Recipe & Meal Planner application."""
    config = load_config("config.json")
    recipes = load_recipes(config["recipe_file"])
    meal_plan = create_weekly_meal_plan()

    while True:
        print(f"\n{config['app_title']}")
        print("=" * len(config["app_title"]))
        print("1. List all recipes")
        print("2. Search recipes by name")
        print("3. Search recipes by ingredient")
        print("4. Filter recipes by category")
        print("5. View recipe details")
        print("6. Build a 7-day meal plan")
        print("7. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            list_recipes(recipes)

        elif choice == "2":
            term = input("Enter recipe name: ").strip()
            list_recipes(search_by_name(recipes, term))

        elif choice == "3":
            ingredient = input("Enter an ingredient: ").strip()
            results = search_by_ingredient(recipes, ingredient)
            list_recipes(results)

        elif choice == "4":
            category = input("Enter category: ").strip()
            list_recipes(filter_by_category(recipes, category))

        elif choice == "5":
            choose_recipe(recipes)

        elif choice == "6":
            print("\n7-Day Meal Planner")
            print("------------------")

            for day in meal_plan:
                current = meal_plan[day]
                if current:
                    print(f"{day}: {current['name']}")
                else:
                    print(f"{day}: No meal assigned")

            while True:
                day = input(
                    "\nEnter a day to assign a recipe "
                    "(or type 'done' to return): "
                ).strip()

                if day.lower() == "done":
                    break

                if day.lower() not in [
                    existing_day.lower() for existing_day in meal_plan
                ]:
                    print("Invalid day. Please enter a valid weekday.")
                    continue

                list_recipes(recipes)

                try:
                    selection = int(input("Enter recipe number: "))
                except ValueError:
                    print("Invalid selection.")
                    continue

                if selection < 1 or selection > len(recipes):
                    print("Invalid selection.")
                    continue

                assign_recipe_to_day(
                    meal_plan,
                    day,
                    recipes[selection - 1],
                )

                print(f"{day.title()} updated successfully.")

            print("\nUpdated Meal Plan")
            print("-----------------")

            for day, recipe in meal_plan.items():
                if recipe:
                    print(f"{day}: {recipe['name']}")
                else:
                    print(f"{day}: No meal assigned")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-7.")

if __name__ == "__main__":
    main()
