$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    $.each(data.results, function (i, item) {
      const newItem = $('<li></li>').text(item.title);
      $('UL#list_movies').append(newItem);
    });
  }
);
