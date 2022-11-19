
var general_name = ["apple", "banana", "orange"];
var num=1
function link_autocomplete_data($id) {
  for (var i in general_name) {
    console.log(general_name[i])
    $('<option value="' + num + '">' + general_name[i] + "</option>").insertAfter($('Rent_form_g_name').find("option:last"))
    num++;
  };
}
link_autocomplete_data('Rent_form_g_name')
  $('#Rent_form_g_name').selectpicker();

