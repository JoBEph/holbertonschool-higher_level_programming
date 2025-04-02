const list_movie = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
data.results.forEach(movie => {
    const movie_li = document.createElement('li');
    movie_li.textContent = movie.title;
    list_movie.appendChild(movie_li);
    });
})
    .catch(error => {
        console.error('Error:', error);
        if(list_movie){
            const error_li = document.createElement('li');
            error_li.textContent = 'Error loading movies';
            list_movie.appendChild(error_li);
        }
});
