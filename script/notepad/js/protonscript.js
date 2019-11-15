function disclaimer() {
    return confirm('');
}

function updateDelay(delay) {
    $('#rangevalue').html('Delay: '+delay);
}

function pidList(){
  
  var jqxhr = $.post( "/vidpid",{
    'pid_type': 'pids',
    'vendor': $('#vid').val()
    
  })
  .done(function(data) {
    if (data["valid"]) {

      // Remove the existing option
      $("#pid").find("option").remove();

      // Create the new option entries
      $.each(data['pids'], function (key, value) {
          $('#pid').append('<option value="'+ value[0] +'">'+ value[1] +'</option>');
      });
      
    } else {
      var error_msg = '<div class="alert alert-danger" role="alert">' + data['message'] +'</div>'
      
      $('#payloadFiles').html(error_msg);
    }
  })
  .fail(function(data) {
      var error_msg = '<div class="alert alert-danger" role="alert">POST Error</div>'
      $('#payloadFiles').html(error_msg);
  })
  .always(function() {
    console.log( "finished" );
  });
}


function generateVid(){
  
  var jqxhr = $.post( "/vidpid",{
    'pid_type': 'file',
    'vid': $('#vid').val(),
    'pid': $('#pid').val()
    
  })
  .done(function(data) {
    if (data["valid"]) {

      var button1 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64vid'] + '" download="vidpid.bin" role="button">Download vidpid.bin</a>'
      $('#payloadFiles').html('');
      $('#payloadFiles').append(button1);
      
    } else {
      var error_msg = '<div class="alert alert-danger" role="alert">'+ data['message'] +'</div>'
      
      $('#payloadFiles').html(error_msg);
    }
  })
  .fail(function(data) {
      var error_msg = '<div class="alert alert-danger" role="alert">POST Error</div>'
      $('#payloadFiles').html(error_msg);
  })
  .always(function() {
    console.log( "finished" );
  });
}

function decoderSubmit() {
  
  var formData = new FormData();
  formData.append('file', $('#decodeInputFile')[0].files[0]);
  formData.append('duck_type', 'decoder');
  formData.append('languageSelect', $('#languageSelect').val())
  
  $.ajax({
         url: "/decode",
   type: "POST",
   data:  formData,
   contentType: false,
         cache: false,
   processData:false,
   beforeSend : function()
   {
    // Clear the payload card
    $('#payloadFiles').html('');
   },
   success: function(data)
      {
    if(data['valid'])
    {
      // decoder worked
      var button1 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64ducktext'] + '" download="duckycode.txt" role="button">Download duckycode.txt</a>'
      var button2 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="#" onclick="sendToEncoder(\''+data['b64ducktext'] + '\')" role="button">Edit in Encoder</a>'

      $('#payloadFiles').html('');
      $('#payloadFiles').append(button1, button2);
    }
    else
    {
     // Decoder failed show the error message
      var error_msg = '<div class="alert alert-danger" role="alert">'+ data['message']  +'</div>'
      $('#payloadFiles').html(error_msg);
    }
      },
     error: function(e) 
      {
        // The POST failed
        console.log(e.StausText)
      var error_msg = '<div class="alert alert-danger" role="alert">Server POST Error</div>'
      $('#payloadFiles').html(error_msg);
      }          
    }); 
 
  }

function download_inject() {
  var formData = new FormData();
  var name = $('#text-input')[0];
  alert(name)
  formData.append('file',  $('#text-input').val()); //document.querySelector('.ace_text-input')
  alert(formData.getAll('file'));
}


function encoderSubmit() {
  
  disclaimer();
  
  var jqxhr = $.post( "/encode",{
    'duck_type': $('#duck_type').val(),
    'languageSelect': $('#languageSelect').val(),
    'ducky_text': editor.getValue()
    
  })
  .done(function(data) {
    if (data["valid"]) {
      // Create the two download buttons. 
      
      var button1 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64inject'] + '" download="inject.bin" role="button">Download Inject.bin</a>'
      var button2 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64ducktext'] + '" download="duckycode.txt" role="button">Download duckycode.txt</a>'

      $('#payloadFiles').html('');
      $('#payloadFiles').append(button1, button2);
      
      
    } else {
      var error_msg = '<div class="alert alert-danger" role="alert"> Error on line '+ data['line_count'] +' : '+ data['message'] +'</div>'
      
      $('#payloadFiles').html(error_msg);
    }
  })
  .fail(function(data) {
      var error_msg = '<div class="alert alert-danger" role="alert">POST Error</div>'
      $('#payloadFiles').html(error_msg);
  })
  .always(function() {
    console.log( "finished" );
  });
  
}

$(document).ready(function () {
// When we tick a checkbox on the payload generator we need to add the variables to the user vars card.
$("input[type='checkbox']").change(function() {
    if(this.checked) {
        // Add User input fields
        addInput(this.getAttribute('name'), this.getAttribute('data-fields'), this.getAttribute('data-syntax'));
    } else {
        // remove the element from the dom.
        var div = document.getElementById(this.getAttribute('name'));
        div.remove();
    }
});

});


function addInput(itemName, itemFields, itemSyntax){

    var div_panel = '';
    var sectionDisplayName = itemName;
    var sectionFormName = itemName;//.replace(/\s+/g, '-').toLowerCase();


    var fieldNames = itemFields.split(',');
    var syntaxNames = itemSyntax.split(',');
    if (fieldNames.length > 0 && fieldNames[0] != ''){
      
    div_panel += '<div class="card mb-2" id="'+ itemName +'">\
                  <div class="card-header">'+itemName+'</div>\
                  <div class="card-body">'
      
    }

    for (var i = 0; i < fieldNames.length; i++) {

        var inputDisplayName = fieldNames[i];
        var inputPlaceholder = syntaxNames[i];

        var inputFormName = sectionFormName + '__' + fieldNames[i];//.replace(/\s+/g, '-').toLowerCase();

        if (inputDisplayName.length > 0) {
            div_panel += '<div class="form-group"><input type="text" class="form-control form-control-sm" name="'+ inputFormName +'" placeholder="'+ inputPlaceholder +'"></div>';

        }

    }
    div_panel += '<input type="hidden" name="section_' + sectionFormName +'" value="'+ sectionFormName +'">';
    div_panel += "</div></div>";

    $("#userVariables").append(div_panel);
    //document.getElementById('form_variables').innerHTML += (div_panel)

}


function payloadGenerator() {
      disclaimer();
  console.log("Generate Payload");
  // Need to collect all the variables.
  var postData = {
    'delay': $('#rangeinput').val(),
    'osname': $('#osname').val(),
    'language': $('#languageSelect').val(),
    'target_os': $('#target_os').val()
  };
  var userVars = $('#userVariables :input')
  userVars.each(function(entry){
    entry_elem = $(this);
    entry_name = entry_elem.attr('name');
    entry_val = entry_elem.val();
    postData[entry_name] = entry_val;
    
  });
  
  console.log(postData);

  var jqxhr = $.post( "/payload/", postData)
  .done(function(data) {
    if (data["valid"]) {

      // Create the two download buttons. 
      
      var button1 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64inject'] + '" download="inject.bin" role="button">Download Inject.bin</a>'
      var button2 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="data:application/octet;base64,' + data['b64ducktext'] + '" download="duckycode.txt" role="button">Download duckycode.txt</a>'
      var button3 = '<a class="btn btn-sm btn-primary mx-auto d-block mt-2" href="#" onclick="sendToEncoder(\''+data['b64ducktext'] + '\')" role="button">Edit in Encoder</a>'
      
      $('#payloadFiles').html('');
      $('#payloadFiles').append(button1, button2, button3);
      
      
    } else {
      var error_msg = '<div class="alert alert-danger" role="alert"> '+ data['message'] +'</div>'
      $('#payloadFiles').html(error_msg);
    }
  })
  .fail(function(data) {
      var error_msg = '<div class="alert alert-danger" role="alert">POST Error</div>'
      $('#payloadFiles').html(error_msg);
  })
  .always(function() {
    console.log( "finished" );
  });
  
  

}

function getUserScript(uid) {
  // get the script content
  var jqxhr = $.get( "/userscript/"+uid, function() {
    console.log( "sent" );
  })
    .done(function(data) {
      if (data["valid"]) {
          // Pass the script content to Encoder
          sendToEncoder(data['b64ducktext'])
      } else {
      var error_msg = '<div class="alert alert-danger" role="alert"> '+ data['message'] +'</div>'
      $('#payloadFiles').html(error_msg);
      }
    })
    .fail(function(data) {
      var error_msg = '<div class="alert alert-danger" role="alert">POST Error</div>'
      $('#payloadFiles').html(error_msg);
    });

}

function sendToEncoder(ducky_text) {
  
  // If we are in HTML5 then lets send to localstorage change location and let the encoder page recover it
  if (typeof(Storage) !== "undefined") {
    localStorage.setItem("duckytext", ducky_text)
    window.location.href = '/encode';
} else {
      var error_msg = '<div class="alert alert-danger" role="alert">Your browser does not support this feature. Try Chrome.</div>'
      $('#payloadFiles').html(error_msg);
}
  
}


// This randomly changes the title every 2 seconds!
var tid = setInterval(mycode, 2000);
function mycode() {
  var myArray = ['Look at me', 'Over Here', 'ProtonScript', 'Comfortable Editor'];
  var rand = myArray[Math.floor(Math.random() * myArray.length)];
  $(document).attr("title", rand);
}
function abortTimer() { // to be called when you want to stop the timer
  clearInterval(tid);
}
