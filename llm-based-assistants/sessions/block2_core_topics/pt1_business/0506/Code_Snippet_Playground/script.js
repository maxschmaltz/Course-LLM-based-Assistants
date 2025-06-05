document.addEventListener('DOMContentLoaded', function() {
    const submitBtn = document.getElementById('submitBtn');
    const clearBtn = document.getElementById('clearBtn');
    const message = document.getElementById('message');
    const textarea = document.querySelector('textarea');

    submitBtn.addEventListener('click', function() {
        message.textContent = 'Processing...';
        setTimeout(() => {
            const isSuccess = Math.random() < 0.5;
            message.textContent = isSuccess ? 'Success' : 'Something went wrong';
        }, 3000);
    });

    clearBtn.addEventListener('click', function() {
        textarea.value = '';
        message.textContent = '';
    });
});