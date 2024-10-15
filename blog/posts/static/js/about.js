// Function to display a greeting when the page loads
window.onload = function() {
    let message = document.createElement('p');
    message.innerText = "Learn more about our journey!";
    message.style.textAlign = "center";
    message.style.color = "whitesmoke";
    document.body.prepend(message);
};


// Smooth scrolling for internal links only
document.querySelectorAll('nav a').forEach(anchor => {
    // Check if the href starts with a '#', indicating an internal link
    if (anchor.getAttribute('href').startsWith('#')) {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    }
});
