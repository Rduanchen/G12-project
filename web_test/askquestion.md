# Title: How can I clone a form and add autocomplete automatically?(with Jquery)

Hi:
let me describe what does the codes are doing.It is a simple form of html. here is two box. when user type a name(the name must exist in the list that I claw from other website) in the second box. The firstbox would show the id of the name. when someone click the "clone" button the programe would clone the form and change it's id.

here is my question:
1. How can set autocomplete automatically when I clone a form.
2. How can I  autocomplete the first box(id of the name,id="Rent_form_g_ID") while user type the name in the second box(id="Rent_form_g_name").

The following code only run **when i didn't clone anything.**

This is my code:  
```html
<body>
  <form>
     <div class="row" id="general_form">
              <div class="col-2">
              <label for="Rent_form_g_ID" class="form-label">id of name</label>
              <input type="text" class="form-control"id="Rent_form_g_ID"  value="" disabled readonly>
              </div>
              <div class="col-2">
              <label for="Rent_form_g_name" class="form-label">name</label>
              <input type="text" class="form-control" placeholder="enter the name" id="Rent_form_g_name">
              </div>
              <div class="col-2">
                  <button type="button" class="btn btn-primary btn-block" onclick="delete_data(this.id)">delete</button>
              </div>
              <br>
          </div>
  </form>
  <div class="row">
      <hr>
      <button type="button" class="btn btn-primary btn-block" onclick="append_a_data()">新增一筆資料</button>
  </div>
<body>
<script>
  var general_data={};
  var general_name=[];
  var general_key=[];

  //get general data via api        
  //analyze the data which i get
  var url='https://ap3.ragic.com/haisann/forms2/1?api=true';
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, false ); // false for synchronous request
  xmlHttp.send( null );
  general_data=JSON.parse(xmlHttp.responseText);
  console.log(general_data);
  for(var i in general_data){
      general_key.push(general_data[i]["財產編號"]);
      general_name.push(general_data[i]["財產名稱"]);
  };
  console.log("get general data ssucess fully");


  function link_autocomplete_data($id){
      //連結財產資料
      $('#'+$id).autocomplete({
           source: general_name
      });
  }


  var cloneCount = 1;//clone 
  //clone sub form and change id
  function append_a_data(){
      var $html=$('#general_form').clone().attr('id', 'general_form'+ cloneCount).insertAfter($('[id^=general_form]:last'));
      $('#general_form'+ cloneCount).find('#Rent_form_g_ID').attr('id','Rent_form_g_ID'+cloneCount);
      $('#general_form'+ cloneCount).find('#Rent_form_g_name').attr('id','#Rent_form_g_name'+cloneCount);
      link_autocomplete_data('Rent_form_g_name'+cloneCount);
      cloneCount++;
      
  };

  function delete_data($id){
      $('#'+$id).parent().parent().remove();
  };


  $(document).ready(function(){
      link_autocomplete_data("Rent_form_g_name");

      // also I don't know how to write this programe better
      $('#Rent_form_g_name').click(function() {
          $(this).change(function(){
              var g_name=$('#Rent_form_g_name').val();
              for(i in general_data){
                  if(general_data[i]["財產名稱"]==g_name){
                      $('#Rent_form_g_ID').val(general_data[i]["財產編號"])
                      $('#Rent_form_g_stock').val(general_data[i]["財產數量"])
                  };
          };
          });
      });
      
  })
</script>
```



