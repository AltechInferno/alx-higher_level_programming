$(document).ready(function() {
    $('#btn_translate').on('click', translateHello);
    $('#language_code').on('keypress', function(e) {
        if (e.which === 13) {
            translateHello();
        }
    });

    function translateHello() {
        var languageCode = $('#language_code').val();
        
        $.get('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
            var translation = data.hello;
            $('#hello').text(translation);
        });
    }
});

