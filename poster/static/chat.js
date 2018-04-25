// TODO: Move to WebSockets
// https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
// https://robots.thoughtbot.com/json-event-based-convention-websockets

$(document).ready(function() {
    var socket = io.connect("wss://" + document.location.host + document.location.pathname + "api_v1");

    socket.on('connect', function() {
        socket.send("I have connected")
    });

    socket.on('message', function(msg){
        console.log('message recieved')
        console.log(msg)
        msg_list = document.createElement("ul");
        evt.json.data.forEach( function(message) {
            var msg_box = document.createElement("li");
            msg_box.setAttribute("class", "list-group-item");
            var t = document.createTextNode(message);
            msg_box.appendChild(t);
            msg_list.appendChild(msg_box);
        } );
        var chatbox = document.getElementById("chatbox");
        chatbox.innerHTML = "";
        chatbox.setAttribute("class", "list-group");
        chatbox.appendChild(msg_list);
    });
});


function getJSON(url) {
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

function postJSON(url, data) {
    socket.send( JSON.stringify(data) );
}

function sendChat(channel) {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    postJSON("/api/v1/channels/main", {message:message});
}



function makeChannel(channel) {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    postJSON("/api/v1/channels/" + message, {channel:channel});
}

function getChannels() {
    getJSON('/api_v1/channels').then(function(data) {
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