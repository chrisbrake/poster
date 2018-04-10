var getJSON = function(url) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open('get', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        resolve(xhr.response);
      } else {
        reject(status);
      }
    };
    xhr.send();
  });
};

function sendChat() {
    var message = document.getElementById("message_to_send").value;
    document.getElementById("message_to_send").value = "";
    var xhr = new XMLHttpRequest();
    var url = "/channels/main";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send(message);
}

function getChannels() {
    getJSON('/channels').then(function(data) {
        alert('Your Json result is:  ' + data.result[0]); //you can comment this, i used it to debug
        document.getElementById('chatbox').innerText = data.result[0]; //display the result in an HTML element
    }, function(status) { //error detection....
        alert('Something went wrong.');
    });
}