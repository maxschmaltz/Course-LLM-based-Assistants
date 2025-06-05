document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.createElement('button');
    themeToggle.textContent = 'Toggle Theme';
    themeToggle.style.position = 'fixed';
    themeToggle.style.bottom = '10px';
    themeToggle.style.right = '10px';
    document.body.appendChild(themeToggle);

    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-theme');
    });

    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('#main-nav a');

    window.addEventListener('scroll', function() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 60) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });

    const chatButton = document.createElement('button');
    chatButton.textContent = 'Open Chat';
    chatButton.style.position = 'fixed';
    chatButton.style.bottom = '50px';
    chatButton.style.right = '10px';
    document.body.appendChild(chatButton);

    chatButton.addEventListener('click', function() {
        alert('Chat feature coming soon!');
    });
});
