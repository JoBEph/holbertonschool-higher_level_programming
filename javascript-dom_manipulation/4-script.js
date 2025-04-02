const add_item = document.querySelector('#add_item');
const my_list = document.querySelector('.my_list');
add_item.addEventListener('click', function() {
    const new_li = document.createElement('li');
    new_li.textContent = 'Item';
    my_list.appendChild(new_li);
});
