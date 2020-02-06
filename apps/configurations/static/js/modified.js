$('#Modal_stockist').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var recipient = button.data('pki'); // Extract info from data-* attributes
  console.log(recipient);
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this);
  modal.find('.modal-body #stock').val(recipient)
});

$('#Modal_element_delete').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var recipient = button.data('pk'); // Extract info from data-* attributes
    console.log(recipient);
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('.modal-footer #delete').val(recipient);
  });
  
  var token = '{{csrf_token}}';
    $('#Modal_list').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var urlToAjax = button.data('urlstockists');
        console.log(urlToAjax);
        var recipient = button.data('pk'); // Extract info from data-* attributes
        console.log(recipient);                
            $.ajax({
                headers: { "X-CSRFToken": token },
                url: urlToAjax,
                type: 'POST',
                data: {'id':recipient},
                success: function(data){
                    console.log(data)
                    var htmldata=""
                    if(data.length==0){
                        htmldata += '<div class="h5 mb-0 font-weight-bold text-gray-800"> There are no assigned stockists </div>'
                    }else{
                        for(var i = 0; i<data.length; i++){
                            htmldata += '<div class="card border-left-primary shadow h-100 py-2">\
                                            <div class="card-body">\
                                                <div class="row no-gutters align-items-center">\
                                                    <div class="col mr-2">\
                                                        <div class="h5 mb-0 font-weight-bold text-gray-800">Name: '+data[i].fields.name+'</div>\
                                                        <div class="h5 mb-0 font-weight-bold text-gray-800">Position: '+data[i].fields.position+ '</div>\
														<div class="form-group">\
														<label> Grant input'+
														(data[i].fields.grant_input==true ? 
															'<input type="checkbox" checked class="newToggle" data-toggle="toggle" data-on="On" data-off="Off" data-onstyle="warning">':
															'<input type="checkbox" class="newToggle" data-toggle="toggle" data-on="On" data-off="Off" data-onstyle="warning">'
															)
														+'</label>\
                                                            <label> Grant output'+
															(data[i].fields.grant_output==true ? 
																'<input type="checkbox" checked class="newToggle" data-toggle="toggle" data-on="On" data-off="Off" data-onstyle="warning">':
																'<input type="checkbox" class="newToggle" data-toggle="toggle" data-on="On" data-off="Off" data-onstyle="warning">'
																)
															+'</label>\
                                                        </div>\
                                                    </div>\
                                                    <div class="col-auto">\
                                                        <i class="fas fa-user fa-2x text-gray-300"></i>\
                                                    </div>\
                                                </div>\
                                            </div>\
                                        </div> <br>'
                        }     
                    }
                    $('#stck').html(htmldata);             
					$('.newToggle').bootstrapToggle();
                }
            });
        var modal = $(this);
        modal.find('.modal-body #stock').val(recipient)
    });