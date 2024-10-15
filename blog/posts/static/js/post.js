// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {

    // Function to handle hover effect on post titles
    const addHoverEffect = () => {
        const postTitles = document.querySelectorAll('h1');
        postTitles.forEach(title => {
            title.addEventListener('mouseenter', () => {
                title.style.transform = 'scale(1.05)'; // Slightly enlarge the title
                title.style.transition = 'transform 0.2s ease'; // Add transition
            });
            title.addEventListener('mouseleave', () => {
                title.style.transform = 'scale(1)'; // Reset size
            });
        });
    };

    // Function to fade in content on load
    const fadeInContent = () => {
        const contentElements = document.querySelectorAll('h1, p');
        contentElements.forEach((element, index) => {
            element.style.opacity = '0'; // Start with invisible content
            element.style.transition = 'opacity 0.5s ease-in-out'; // Add transition
            setTimeout(() => {
                element.style.opacity = '1'; // Fade in
            }, index * 200); // Stagger the fade in effect
        });
    };

    // Initialize functions
    addHoverEffect();
    fadeInContent();
});
