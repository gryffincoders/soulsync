document.addEventListener("DOMContentLoaded", function() {
    // Selecting the menu icon
    let menuicn = document.querySelector(".menuicn");
    // Selecting the navigation container
    let nav = document.querySelector(".navcontainer");
    
    // Ensuring elements are present before adding event listeners or manipulating them
    if (menuicn && nav) {
        menuicn.addEventListener("click", () => {
            // Toggle the 'navclose' class on click to show/hide the nav container
            nav.classList.toggle("navclose");
        });
    } else {
        console.error("Menu icon or navigation container not found!");
    }

    // Attempting to retrieve the user's input and display it
    let userInputElement = document.getElementById("user");
    let p = document.getElementById("name");
    
    if (userInputElement && p) {
        // Update paragraph content only after ensuring both elements exist
        userInputElement.addEventListener("change", () => {
            p.innerHTML = userInputElement.value; // Display the user's input in paragraph 'p'
        });
    } else {
        console.error("User input element or paragraph element not found!");
    }
});


function selectMood(event, mood) {
    // Clear previous selections
    document.querySelectorAll('.mood').forEach(emoji => {
        emoji.classList.remove('selected');
    });

    // Highlight the selected emoji
    event.target.classList.add('selected');

    // Update the webpage based on the selected mood
    const moodText = document.querySelector('.welcome h3');
    switch (mood) {
        case 'Very Sad':
            moodText.textContent = 'We notice you’re feeling very sad. It’s okay to feel this way. Here’s something gentle for you to read or do...';
            break;
        case 'Sad':
            moodText.textContent = 'Feeling a bit down? Let’s find a way to brighten your day together.';
            break;
        case 'Neutral':
            moodText.textContent = 'Feeling neutral is perfectly fine. Perhaps there’s something small you could enjoy today?';
            break;
        case 'Happy':
            moodText.textContent = 'We’re glad you’re feeling happy! Keep the positivity going!';
            break;
        case 'Very Happy':
            moodText.textContent = 'It’s great to see you so joyful! Spread that great energy!';
            break;
    }
}

