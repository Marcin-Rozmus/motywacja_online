const card = document.getElementById('motivationCard');
const motivationText = document.querySelector('.motivation-text');
const textCounter = document.getElementById('textCounter');
const motivationIcon = document.getElementById('motivationIcon');
const authorText = document.createElement('p');
authorText.className = 'author-text';
document.querySelector('.card-back').appendChild(authorText);
let isFlipped = false;

const themeToggle = document.getElementById('theme-toggle');

async function getRandomText() {
    try {
        const endpoint = card.classList.contains('demotivation-mode') ? '/get-demotivation' : '/get-motivation';
        const response = await fetch(endpoint);
        const data = await response.json();
        textCounter.textContent = `${data.index}/${data.total}`;
        motivationIcon.className = `motivation-icon ${data.icon}`;
        authorText.textContent = data.author ? `~ ${data.author}` : '';
        return data.text;
    } catch (error) {
        console.error('Błąd podczas pobierania tekstu:', error);
        return "Przepraszamy, wystąpił błąd. Spróbuj ponownie.";
    }
}

card.addEventListener('click', async () => {
    if (!isFlipped) {
        const text = await getRandomText();
        motivationText.textContent = text;
        card.classList.add('flipped');
        isFlipped = true;
    } else {
        card.classList.remove('flipped');
        isFlipped = false;
    }
});

themeToggle.addEventListener('change', function() {
    if (this.checked) {
        card.classList.add('demotivation-mode');
        motivationIcon.classList.remove('fa-lightbulb');
        motivationIcon.classList.add('fa-cloud');
        document.body.classList.add('dark-theme');
        document.title = 'Mom dość';
    } else {
        card.classList.remove('demotivation-mode');
        motivationIcon.classList.remove('fa-cloud');
        motivationIcon.classList.add('fa-lightbulb');
        document.body.classList.remove('dark-theme');
        document.title = 'Jesteś zwycięzcą';
    }
}); 