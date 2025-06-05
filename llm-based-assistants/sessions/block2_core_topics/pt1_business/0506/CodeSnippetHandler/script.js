const submitButton = document.getElementById('submitCode');
const clearButton = document.getElementById('clearForm');
const codeInput = document.getElementById('codeInput');
const resultMessage = document.getElementById('resultMessage');

submitButton.addEventListener('click', () => {
    resultMessage.textContent = 'Processing...';
    setTimeout(() => {
        const isSuccess = Math.random() < 0.5;
        resultMessage.textContent = isSuccess ? 'Success' : 'Something went wrong';
    }, 3000);
});

clearButton.addEventListener('click', () => {
    codeInput.value = '';
    resultMessage.textContent = '';
});