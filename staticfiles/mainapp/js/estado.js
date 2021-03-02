$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-estado .modal-content").html("");
        $("#modal-estado").modal("show");
      },
      success: function (data) {
        $("#modal-estado .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#estado-table tbody").html(data.html_estado_list);
          $("#modal-estado").modal("hide");
        }
        else {
          $("#modal-estado .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-estado").click(loadForm);
  $("#modal-estado").on("submit", ".js-estado-create-form", saveForm);


});
