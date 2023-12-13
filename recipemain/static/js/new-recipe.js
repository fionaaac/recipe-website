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
        // event.preventDefault();

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


        var hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'ingredientsData';
        hiddenInput.value = JSON.stringify(ingredientsData);
        console.log(hiddenInput.value);
        this.appendChild(hiddenInput);

        this.submit();
    });
});