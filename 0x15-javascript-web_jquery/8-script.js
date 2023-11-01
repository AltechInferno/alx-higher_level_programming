$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $res = data.results
  $.each(res, function(i, j) {
    $('DIV#character').append(`<li>${j.title}</li>`);
  })
});
