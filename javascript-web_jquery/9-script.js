$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (json) {
  $('DIV#hello').text(json.hello);
});
