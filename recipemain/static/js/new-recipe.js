$(document).ready(function () {
    $( '#multiple-select-custom-field' ).select2( {
        theme: "bootstrap-5",
        width: $( this ).data( 'width' ) ? $( this ).data( 'width' ) : $( this ).hasClass( 'w-100' ) ? '100%' : 'style',
        placeholder: $( this ).data( 'placeholder' ),
        closeOnSelect: false,
        tags: true
    } );
    
});

function addIngredientRow() {
    // Clone the existing row
    var newRow = document.querySelector('.ingredient-row').cloneNode(true);

    // Clear the input values in the cloned row
    var inputs = newRow.querySelectorAll('input, select');
    inputs.forEach(function (input) {
        input.value = '';
    });

    // Append the new row to the form
    document.getElementById('ingredient-form').appendChild(newRow);

    // Collect values from all rows
    var allRows = document.querySelectorAll('.ingredient-row');
    var ingredientsData = [];

    allRows.forEach(function (row) {
        var ingredientName = row.querySelector('#ingredient').value;
        var amount = row.querySelector('#amount').value;
        var unit = row.querySelector('#unit').value; 

        var ingredientData = {
            ingredientName: ingredientName,
            amount: amount,
            unit: unit
        };
        ingredientsData.push(ingredientData);
    });
    console.log('Ingredients Data:', ingredientsData);
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('recipe-form').addEventListener('submit', function (event) {
        // Ingredient Data
        var allRows = document.querySelectorAll('.ingredient-row');
        var ingredientsData = [];

        allRows.forEach(function (row) {
            var ingredientName = row.querySelector('#ingredient').value;
            var amount = row.querySelector('#amount').value;
            var unit = row.querySelector('#unit').value; 
    
            var ingredientData = {
                ingredientName: ingredientName,
                amount: amount,
                unit: unit
            };
            ingredientsData.push(ingredientData);
        });

        // Steps Data
        var allSteps = document.querySelectorAll('.step-textarea');
        var stepsData = [];

        allSteps.forEach(function (textarea) {
            var stepText = textarea.value.trim();
            if (stepText !== '') {
                stepsData.push(stepText);
            }
        });

        var hiddenIngredientsInput = document.createElement('input');
        hiddenIngredientsInput.type = 'hidden';
        hiddenIngredientsInput.name = 'ingredientsData';
        hiddenIngredientsInput.value = JSON.stringify(ingredientsData);
        this.appendChild(hiddenIngredientsInput);

        // Create hidden input for steps data
        var hiddenStepsInput = document.createElement('input');
        hiddenStepsInput.type = 'hidden';
        hiddenStepsInput.name = 'stepsData';
        hiddenStepsInput.value = JSON.stringify(stepsData);
        this.appendChild(hiddenStepsInput);

        // Submit the form
        console.log("submitted!");
        this.submit();
    });
});

function addStepRow() {
    // Create a new textarea element
    var newTextarea = document.createElement('textarea');
    newTextarea.className = 'form-control step-textarea';
    newTextarea.rows = '2';

    // Append the new textarea to the steps container
    var stepsContainer = document.getElementById('steps-container');
    stepsContainer.appendChild(newTextarea);

    var allRows = document.querySelectorAll('.step-textarea');
    var stepsData = [];

    allRows.forEach(function (textarea) {
        stepsData.push(textarea.value.trim());
    });
    console.log('Steps Data:', stepsData);
    
}