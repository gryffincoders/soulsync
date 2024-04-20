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
