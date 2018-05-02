
$(document).ready(function() {
    var url = document.location.host;
    var socket = io.connect(url);

    socket.on("connect", function() {
        console.log("I have connected")
    });

    socket.on("json", function(msg){
        console.log("json received", msg)
        msg_list = document.createElement("ul");
        msg.main.forEach( function(message) {
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

/*
function getJSON(url) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open("get", url, true);
    xhr.responseType = "json";
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
    getJSON("/api_v1/channels").then(function(data) {
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
}*/
