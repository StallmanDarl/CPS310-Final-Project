# CPS 310 Final Project — Checkpoint 1 Reflection

## 1. Feature Selection

Which three features did you select?

- Recipe Management: Search by Ingredient
- Meal Planning: Build a 7-Day Meal Plan
- Grocery / Calculations: Generate a Grocery List

**Response:**

I selected these features because they work together to create a useful meal planning workflow. Ingredient searching makes it easier to find recipes based on available ingredients, while the weekly meal planner allows users to organize their meals. Generating a grocery list will connect the selected recipes to the ingredients needed for the week.

I also chose these features because they build naturally on the starter project's existing recipe data and JSON structure.

## 2. Current Progress

Which two features have you meaningfully implemented so far?

**Response:**

I have implemented ingredient-based recipe searching and seven-day meal planning.

Ingredient searching allows users to search for recipes using full or partial ingredient names. Searches are case-insensitive and return recipes containing matching ingredients.

The meal planner allows users to assign recipes to individual weekdays, view their weekly assignments, and replace previously assigned meals. Both features are integrated into the application's main menu.

## 3. Most Difficult Feature

Which feature has been the most difficult so far?

**Response:**

The seven-day meal planner has been the most challenging feature because it required introducing a new way of organizing and managing recipe data. I needed to create a structure that associates individual recipes with specific weekdays while handling invalid selections and allowing existing assignments to be replaced.

Integrating the functionality into the existing application without disrupting its original features also required additional consideration.

## 4. GitHub Issues

Identify the GitHub Issues you created for your planned work.

**Response:**

I created the following GitHub Issues:

- Issue #1: Implement ingredient-based recipe search.
- Issue #2: Implement seven-day meal planning.
- Issue #3: Generate grocery lists from meal plans.

The Issues helped divide the project into three manageable features. They also provided a way to track planned functionality and establish clear goals for implementation and testing.

## 5. Branch / Pull Request

Identify one branch or pull request that best represents your development process so far.

**Response:**

The `feature/ingredient-search` branch and its associated Pull Request, #4, best represent my development process.

I implemented ingredient-based searching separately from the main branch, integrated the functionality into the application, and added automated tests before submitting the changes for review.

Keeping this work separate from `main` allowed me to develop and verify the feature without affecting the existing application. After reviewing the changes, I merged the Pull Request into `main`.

## 6. Meaningful Commit

Identify one commit you consider meaningful.

**Response:**

The commit `3bb2897d490e365cd5d86d2da0eeb3d5d6bd109a` titled `Add ingredient-based recipe search` was particularly meaningful.

It introduced the ingredient-search functionality, integrated it into the application menu, and included automated tests for the new behavior.

Keeping these related changes together made the implementation easier to review and maintain.

## 7. Testing

What new tests have you added for your features?

**Response:**

I expanded `test_recipe_utils.py` with eleven additional tests.

The ingredient-search tests verify:
- Matching recipes by ingredient.
- Case-insensitive searching.
- Partial ingredient matching.
- Empty results when no matches exist.
- Handling blank search terms.

The meal-planning tests verify:
- Creation of a seven-day meal plan.
- Initially empty assignments.
- Assigning recipes to weekdays.
- Case-insensitive weekday selection.
- Replacing existing assignments.
- Rejecting invalid weekdays.

I also ran the complete pytest suite to verify that the original functionality continued working alongside the new features.

## 8. Bug or Mistake

Describe one bug, mistake, or unexpected behavior you encountered.

**Response:**

While considering ingredient searching, I identified a potential issue where a recipe could appear multiple times if it contained multiple ingredients matching the search term. This would produce unnecessary duplicate results. I addressed this by using a break statement after finding the first matching ingredient in each recipe. This ensures that each recipe is only returned once, even if multiple ingredients match the search, even if the search is not any ingredient verbatim.

## 9. Current Code Quality

Identify one part of your current code that you would improve if you had more time before this checkpoint.

**Response:**

One improvement would be adding persistent storage for weekly meal plans.

Currently, the meal plan exists in memory and is reset when the application restarts. Saving and loading meal plans through JSON would allow users to retain their weekly assignments between sessions.

This would also make the application more useful for repeated meal planning.

## 10. Remaining Plan

What work remains before the final submission?

**Response:**

The primary remaining feature is grocery list generation based on the recipes assigned to the weekly meal plan.

I also plan to improve the application's documentation, add Docker support, configure automated testing through GitHub Actions, and review security and privacy practices.

Before final submission, I will expand the automated tests, verify the complete application, and ensure the README accurately describes the finished functionality and setup instructions.