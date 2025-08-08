function handleSubmit(event) {
    event.preventDefault();

    const inputElement = document.querySelector('input');
    const taskName = inputElement.value;

    // backend integration
    console.log(`submited task ${taskName}`);
}

document.querySelector('form').addEventListener('submit', handleSubmit);