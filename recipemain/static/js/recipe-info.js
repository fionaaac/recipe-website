let star = document.querySelectorAll('input');
let showValue = document.querySelector('#rating-value');

for (let i = 0; i < star.length; i++) {
	star[i].addEventListener('click', function() {
		i = this.value;

		showValue.innerHTML = i + " out of 5";
        console.log("clicked", i);
        sendRatingToServer(i);
	});
}

function sendRatingToServer(rating) {
    const currentUrl = window.location.href;
    const recipeId = currentUrl.split('/').pop();
    const rating = { rating: rating };

    // var hiddenRating = document.createElement('input');
    //     hiddenRating.type = 'hidden';
    //     hiddenRating.name = 'rating';
    //     hiddenIngredientsInput.value = JSON.stringify(rating);
    //     this.appendChild(hiddenIngredientsInput);
    //     this.
}