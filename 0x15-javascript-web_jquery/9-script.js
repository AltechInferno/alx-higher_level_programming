$('document').ready(function() {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(value) {
        $('DIV#hello').text(value.hello);
    });
});
