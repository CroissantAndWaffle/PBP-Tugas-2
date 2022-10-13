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

$('#add_task').submit(function(e) {
  $.ajax({
    data: $('#add_task').serialize(),
    type: "POST",
    url: "add",
    
    success: function(response) {
      $('#add').modal('toggle');
      title = $('#title_add').val()
      description = $('#desc_add').val()
      date = new Date().toJSON();

      add_data = {
        title : title,
        description : description,
        date : date,
      }

      $.post('add/', add_data)

      $('#display').append('<div class="col-13 col-md-6 col-lg-4">\
      <div class="card">\
      <div class="card-body">\
      <h5 class="card-title">'+title+'</h5>\
      <h6 class="card-subtitle mb-2 text-muted">'+date+'</h6>\
      <p class="card-text">'+description+'</p>\
      </div></div></div>');
    
    },
  })
  e.preventDefault();
});
