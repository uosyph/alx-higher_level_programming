#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('div#red_header').addClass('red');
  });
});
