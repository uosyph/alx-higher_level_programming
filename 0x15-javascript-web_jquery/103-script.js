const $ = window.$;
function getHello () {
  $.ajax({
    type: 'GET',
    data: {
      lang: $('INPUT#language_code').val()
    },
    url: 'https://fourtonfish.com/hellosalut/',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    getHello();
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      getHello();
    }
  });
});
