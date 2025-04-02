const hello_element = document.querySelector('#hello')
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(response => response.json())
.then(data => {
    hello_element.textContent = data.hello;
})
.catch(error => {
    console.error('Error:', error);
});
