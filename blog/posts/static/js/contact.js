// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    
    // Function to handle hover effects on phone numbers and emails
    const addHoverEffect = () => {
        const contactItems = document.querySelectorAll('.contact-item');

        contactItems.forEach(item => {
            item.addEventListener('mouseenter', () => {
                item.style.color = '#3498db'; // Change color on hover
                item.style.cursor = 'pointer'; // Change cursor to pointer
                item.style.textDecoration = 'underline'; // Underline text
            });

            item.addEventListener('mouseleave', () => {
                item.style.color = ''; // Reset color
                item.style.textDecoration = 'none'; // Remove underline
            });
        });
    };

    // Function to add click functionality to email and phone links
    const addClickableLinks = () => {
        const email = document.querySelector('#email');
        const phone = document.querySelector('#phone');

        if (email) {
            email.addEventListener('click', () => {
                window.location.href = `mailto:${email.innerText}`; // Open email client
            });
        }

        if (phone) {
            phone.addEventListener('click', () => {
                window.location.href = `tel:${phone.innerText}`; // Initiate phone call
            });
        }
    };

    // Initialize functions
    addHoverEffect();
    addClickableLinks();
});
