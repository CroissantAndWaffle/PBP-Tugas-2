$(document).ready(function() {
  $.get("json", function(data) {
    $.each(data, function (key, value) {
      $('#display').append('<div class="col-13 col-md-6 col-lg-4">\
        <div class="card">\
        <div class="card-body">\
        <h5 class="card-title">'+value.fields.title+'</h5>\
        <h6 class="card-subtitle mb-2 text-muted">'+value.fields.date+'</h6>\
        <p class="card-text">'+value.fields.description+'</p>\
        </div></div></div>');
      })            
  });
});