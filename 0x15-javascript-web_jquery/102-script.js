$(document).ready(function() {
    $('#btn_translate').on('click', function() {
      var languageCode = $('#language_code').val();

        $.get('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
            var translation = data.hello;

            $('#hello').text(translation);
        });
    });
});

