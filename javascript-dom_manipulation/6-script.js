const character_element = document.querySelector('#character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json())
.then(data => {
    character_element.textContent = data.name;
})
.catch(error => {
    console.error('Error:', error);
    character_element.textContent = 'Error loading character';
  });
