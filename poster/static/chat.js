
var url = document.location.host;
var socket = io.connect(url);

socket.on("connect", function() {
    console.log("I have connected")
});

socket.on("chat", function(msg){
    console.log("chat received", msg)
    msg_list = document.createElement("ul");
    msg.forEach( function(message) {
        var msg_box = document.createElement("li");
        msg_box.setAttribute("class", "list-group-item col-sm-12");
        var t = document.createTextNode(message);
        msg_box.appendChild(t);
        msg_list.appendChild(msg_box);
    } );
    var chatbox = document.getElementById("chatbox");
    chatbox.innerHTML = "";
    chatbox.setAttribute("class", "list-group");
    chatbox.appendChild(msg_list);
});

function sendChat(channel) {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    socket.emit("chat", {msg: message});
};