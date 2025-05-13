document.addEventListener('DOMContentLoaded', () => {
    const textField = document.getElementById('textField');
    const showKeyboardBtn = document.getElementById('showKeyboardBtn');
    const searchBtn = document.getElementById('searchBtn');
    const keyboard = document.getElementById('keyboard');
    const closeKeyboardBtn = document.getElementById('closeKeyboardBtn');
    const keyboardHeader = document.querySelector('.keyboard-header');
    const taskContainer = document.getElementById('keyboard-pos')

    let isDragging = false;
    let offsetX, offsetY;

    showKeyboardBtn.addEventListener('click', () => {
        const containerRect = taskContainer.getBoundingClientRect(); // Get the position of the form container

        // Get the center of the viewport
        const viewportWidth = window.innerWidth;

        // Center the keyboard horizontally
        const keyboardWidth = keyboard.offsetWidth;
        const centerX = (viewportWidth - keyboardWidth) / 2;

        // Position the keyboard below the form container
        keyboard.style.left = `${centerX}px`; // Center horizontally
        keyboard.style.top = `${containerRect.bottom + 10}px`;
        keyboard.classList.remove('hidden');
    });

    closeKeyboardBtn.addEventListener('click', () =>{
        keyboard.classList.add('hidden');
    });

//    searchBtn.addEventListener('click', () => {
//        alert('Search button clicked!');
//    });

    document.querySelectorAll('.key').forEach(key => {
        key.addEventListener('click', () => {
            const value = key.getAttribute('data-value');
            if(value === 'backspace'){
                textField.value = textField.value.slice(0, -1);
            }else if (value === 'enter'){
                textField.value += '\n';
            }else{
                textField.value += value
            }
        });
    });
    keyboardHeader.addEventListener('mousedown', (e) => {
        isDragging = true;
        offsetX = e.clientX - keyboard.offsetLeft;
        offsetY = e.clientY - keyboard.offsetTop;
    });

    document.addEventListener('mousemove', (e) => {
        if(isDragging){
            keyboard.style.left = `${e.clientX - offsetX}px`;
            keyboard.style.top = `${e.clientY - offsetY}px`;
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const navbarItem = document.getElementById('scrollToCard');

    navbarItem.addEventListener('click', (e) => {
        e.preventDefault();  // Prevent the default link behavior

        // Get the first element with class 'card'
        const card = document.querySelector('.about');

        if (card) {
            // Scroll to the element with class 'card'
            card.scrollIntoView({
                behavior: 'smooth',  // Smooth scrolling
                block: 'start'       // Align to the top of the viewport
            });
        }
    });
});
