function Rsvp(event_id){

FB.getLoginStatus(function(response) {
  if (response.status === 'connected') {
    var uid = response.authResponse.userID;
      $.post("/api/", 
      {'fid': uid, 'eid': event_id}, 
      function(data, status){
        console.log("POST successful.  " + event_id + "/" + uid);
      });
  } 
 });
 
 };


