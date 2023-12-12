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
}