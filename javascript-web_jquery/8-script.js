$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (json) {
  const list = json.results;
  for (let i = 0; i < list.length; i++) {
    $('UL#list_movies').append('<li>' + list[i].title + '</li>');
  }
});