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
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type","application/json");
    xhr.send(JSON.stringify(data));
}

function sendChat(channel) {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    postJSON("/channels/main", {message:message});
}

function getChat() {
    getJSON('/channels/main').then(function(data) {
        msg_list = document.createElement("ul");
        data.forEach( function(message) {
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
}

function makeChannel(channel) {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    postJSON("/channels/" + message, {channel:channel});
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

window.setInterval("getChat()", 500);