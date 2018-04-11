function getJSON(url) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open('get', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        console.log('Recieved ' + xhr.response)
        resolve(xhr.response);
      } else {
        reject(status);
      }
    };
    xhr.send();
  });
};

function sendChat() {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    var xhr = new XMLHttpRequest();
    var url = "/channels/main";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    console.log('Sending Message ' + message)
    xhr.send(message);
}

function makeChannel() {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    var xhr = new XMLHttpRequest();
    var url = "/channels/" + message;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    console.log('Making Channel ' + message)
    xhr.send(message);
}

function getChannels() {
    getJSON('/channels').then(function(data) {
        var channel_selector = document.getElementById("channel_selector");
        channel_selector.innerHTML = "";
        data.forEach( function(channel) {
            var btn = document.createElement("BUTTON");
            btn.setAttribute("class", "btn");
            var t = document.createTextNode(channel);
            btn.appendChild(t);
            channel_selector.appendChild(btn);
        } );
    });
}
