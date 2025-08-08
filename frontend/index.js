async function handleSubmit(event) {
    event.preventDefault();

    const inputElement = document.querySelector('input');
    const taskName = inputElement.value;

    inputElement.value = '';
    const response = await fetch('http://localhost:4000/create-task', {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            'task_name': taskName
        })
    })

    const data = await response.json();
    console.log(data);
}

document.querySelector('form').addEventListener('submit', handleSubmit);