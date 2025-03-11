document.addEventListener('DOMContentLoaded', function() {
    // Loading screen
    const loadingScreen = document.querySelector('.loading-screen');
    const progressBar = document.querySelector('.progress-bar');
    const loadingText = document.querySelector('.loading-text');

    let progress = 0;
    const interval = setInterval(() => {
        progress += 1;
        progressBar.style.width = `${progress}%`;
        loadingText.innerText = `Загрузка... ${progress}%`;

        if (progress >= 100) {
            clearInterval(interval);
            setTimeout(() => {
                loadingScreen.style.display = 'none';
                document.body.style.overflow = 'auto'; // Restore scrollbars
            }, 500);
        }
    }, 30); // Adjust the interval to control the loading speed

    // Function to open a popup window
    function openPopupWindow(content) {
        const popupWindow = document.createElement('div');
        popupWindow.classList.add('popup-window');
        popupWindow.innerHTML = `
            <h2>${content.title}</h2>
            ${content.body}
            <button class="close-button">Закрыть</button>
        `;
        document.body.appendChild(popupWindow);

        const closeButton = popupWindow.querySelector('.close-button');
        closeButton.addEventListener('click', () => {
            popupWindow.remove();
        });
    }

    // Event listeners for buttons
    document.querySelectorAll('.nav-button, .main-button, .option-button').forEach(button => {
        button.addEventListener('click', function() {
            const action = this.dataset.action;

            switch (action) {
                case 'iq_test':
                    openPopupWindow({
                        title: 'IQ и возбужденность',
                        body: `
                            <label>Введите количество вашего IQ сегодня:</label>
                            <input type="number" id="iq_value"><br>
                            <label>Введите уровень вашей возбужденности сегодня в %:</label>
                            <input type="number" id="excitement_level"><br>
                            <button onclick="calculateIQ()">Рассчитать</button>
                        `
                    });
                    break;
                case 'AUX':
                    openPopupWindow({
                        title: 'Тест Подолецкой',
                        body: `
                            <label>Введите ваш желанный IQ для инициализации теста Подолецкой:</label>
                            <input type="number" id="desired_iq"><br>
                            <button onclick="startQuiz()">Начать</button>
                        `
                    });
                    break;
                case 'show_random_iq':
                    // Placeholder for show_random_iq functionality
                    alert('Функциональность "Узнать свой настоящий IQ сегодня"');
                    break;
                case 'write_to_podoletskaya':
                    // Placeholder for write_to_podoletskaya functionality
                    alert('Функциональность "Написать Подолецкой"');
                    break;
                case 'open_chat_with_podoletskaya':
                    // Placeholder for open_chat_with_podoletskaya functionality
                    alert('Функциональность "Чат с Подолецкой"');
                    break;
                case 'mini_game':
                    // Placeholder for mini_game functionality
                    alert('Функциональность "Мини-игра: Найди Подолецкую"');
                    break;
                case 'open_fandom':
                    window.open('https://www.fandom.com', '_blank');
                    break;
                case 'toggle_music':
                    // Placeholder for toggle_music functionality
                    alert('Функциональность "Включить/Выключить музыку"');
                    break;
                default:
                    alert('Действие не определено');
            }
        });
    });

    // Basic functions (replace with your actual logic)
    window.calculateIQ = function() {
        const iqValue = document.getElementById('iq_value').value;
        const excitementLevel = document.getElementById('excitement_level').value;
        alert(`Расчет IQ: IQ = ${iqValue}, Возбужденность = ${excitementLevel}`);
        // Add your calculation logic here
    };

    window.startQuiz = function() {
        const desiredIQ = document.getElementById('desired_iq').value;
        alert(`Начать викторину с IQ = ${desiredIQ}`);
        // Add your quiz start logic here
    };
});
