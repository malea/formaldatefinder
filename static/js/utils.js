function Rsvp(event_id){

/* Send FacebookID 'fid' and EventID 'eid' from the client
to the server using the formaldatefinder API */

FB.getLoginStatus(function(response) {
  if (response.status === 'connected') {
    var uid = response.authResponse.userID;
      $.post("/api/", 
      {'fid': uid, 'eid': event_id}, 
      function(data, status){
        console.log("POST successful.  " + event_id + "/" + uid);
      });
  } else {
  alert("Please log in first!");
  }
 });
 
 };


