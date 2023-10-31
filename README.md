# recipe-website

# Functionality Requirements

### All submissions must implement the following functionality:

User accounts: Users can create accounts, log into their accounts and log out.
Creating recipes: Users can create new recipes. Recipes will include a title, a general description, the number of persons the recipe is for, a cooking time estimation, a list of ingredients with their quantities, and a list of steps.
Reading recipes: Users can read recipes.
Rating recipes: Users can rate recipes. You can choose the rating system (an upvote/downvote system, a star rating system, etc.). Each user can rate a recipe only once. They can change their rate later.
Bookmarking recipes: Users can bookmark recipes, so that they can easily find them later.
Uploading photos: When users cook a recipe, they can take a photo and upload it. Users that read a recipe can see all its photos. Any user can upload photos for a recipe, even if they aren't the actual creators of the recipe.
Data model
Your project must support the following data model for the mandatory functionality. You can change the data model if you have justified reasons to do so. For example, you can enrich this data model because of the needs of any additional features you implement (add new entities, add new properties to some entities, etc.), or if you believe a different schema is better in the context of your design of the project.

### The main entities to store in the database are:

Users: Users are identified by an email and they authenticate with a password, which has to be stored salted and encrypted in the database. They also have a name that will be publicly displayed with the recipes they create and the photos they upload.
Recipes: Recipes have a title, a general description, the user who created them, the number of persons the recipe is for, a cooking time estimation, a list of ingredients and quantities (see quantified ingredients below) and a list of steps (see steps below). Note that there is a many-to-one relationship between recipes and users (many recipes can be created by the same user, but a recipe is created by just one user).
Ingredients: Ingredients have a name (e.g. flour, eggs, olive oil, etc.).
Quantified ingredients: A quantified ingredient represents the quantity of an ingredient to be used in a specific recipe. Quantities are expressed with two fields: a number and a unit of measurement (e.g. 1 kilo, 2 units, 1/2 teaspoon, 100 milliliter, etc.). Note that there is a many-to-one relationship between quantified ingredients and ingredients (many quantified ingredients can be related to the same ingredient, but a quantified ingredient is related to just one ingredient). The same relationship exists between quantified ingredients and recipes (many quantified ingredients can belong to the same recipe, but a quantified ingredient belongs to just one recipe).
Steps: A step in a recipe is a description of a cooking action that has to be performed in order to cook the recipe. It consists in a textual description of the action and its sequence number in the recipe. There is a many-to-one relationship between steps and recipes.
Ratings: A rating consists in a user, a recipe and a value. The value can be a number of stars, a Boolean value (upvote/downvote), etc., depending on the rating system you choose. There is a many-to-one relationship between ratings and users and between ratings and recipes.
Photos: Any user can upload photos for a recipe, even if they aren't the actual creators of the recipe. A photo has the following properties: the user who uploaded it, the recipe it belongs to and, if you follow the suggestions about photo upload, the file extension of the photo. There are many-to-one relationships between photos and users and between photos and recipes.

# Views
Your application has to provide at least the following views:

Main view (authentication is not required): This is the main page of the application. A few recipes are featured here, according to the criteria you choose (the latest ones, the ones with the highest ratings, random ones, etc.). Each recipe links to its recipe view.
Recipe view (authentication is not required): The detailed information of a recipe is displayed in this view. The view receives the recipe identifier as a parameter. In this view, authenticated users can bookmark the recipe, rate it and upload a photo for it. Every mention of a recipe in the application must link to this view.
User view (authentication is not required): This view displays the name of the user, the list of recipes they have created and the photos they have uploaded for recipes. In addition, the list of bookmarked recipees is presented if the authenticated user is the same user this view is displaying (i.e. users are viewing their own profile). The view receives the user identifier as a parameter. Every mention of a user's name in the application must link to this view.
Recipe creation view (an authenticated user is required): Users can create a new recipe from this view. In particular, users will be able to enter the title, the general description, cooking time, and number of people the recipe is for. They will also be able to add ingredients with their quantities, as well as cooking steps. When adding ingredients, users should be able to select an ingredient from the list of existing ingredients or create a new one.
Take the list of views above as a suggestion. You are free to design your application with different views as long as you provide the same functionality. You can also change these views in order to accommodate additional features.

## Suggestions about recipe creation
One possible way to implement the creation of a recipe is as follows:

First, the user enters everything about the recipe in a form, except ingredients and steps. This form could be placed at the main view of the application or in a separate view.
Then, the application shows a view with the current data of the recipe. From this view, the creator of the recipe and:
Add an ingredient: The user selects an ingredient from the list of ingredients that already exist in the application, or creates a new ingredient if it isn't in the list. The datalist feature of HTML forms can be useful for this (see the slides for more information). The user will also select the quantity of that ingredient and units (grams, milliliters, etc.).
Add a step: Users enter the textual description of the step. From the point of view of the mandatory functionality, the user is expected to insert steps in order. Therefore, you aren't required to implement the possibility of reordering, editing or deleting steps.
Mark the recipe as complete: Users can mark the recipe as complete when they have finished entering all the ingredients and steps. You may need to add an extra Boolean column to the Recipe model for specifying whether it's complete.
After users add a new ingredient or step in the view above, they are redirected again to the same view.
After users mark the recipe as complete, they are redirected to the recipe view of that recipe, and aren't allowed to edit it anymore.
With the approach above, you'll need:

One controller function and one template for displaying the form that asks for the title, general description, etc. of the new recipe (step 1 above). Alternatively, this form could be integrated into de main view template.
One controller function for receiving the data from that form and storing the recipe object.
One controller function and one template for displaying the current state of the recipe and asking for the next ingredient or step (step 2 above).
One controller function for receiving the data about an ingredient and quantity, and storing them.
One controller function for receiving the data about a step, and storing it.
One controller function for marking the recipe as complete.
Note that only the user who is creating the recipe should be able to access these controller functions for that specific recipe. Remember to check that the user is authenticated and that the recipe belongs to the authenticated user before doing any action in your controllers.

Nevertheless, you are free to choose other ways of entering recipes and implementing this feature. One possible alternative is using JavaScript to create the recipe at the client side and send it to the server when the user has finished entering it. Its correct implementation would be awarded additional functionality points because of the use of JavaScript.
