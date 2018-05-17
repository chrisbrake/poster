
var url = document.location.host;
var socket = io.connect(url);
var current_room = "main"

socket.on("connect", function() {
    socket.emit("join", {room: current_room});
    console.log("I have connected")
});

socket.on("chat", function(msg){
    console.log("chat received", msg)
    msg_list = document.createElement("ul");
    msg.forEach( function(message) {
        var msg_box = document.createElement("li");
        msg_box.setAttribute("class", "list-group-item col-sm-12");
        var t = document.createTextNode(message.data);
        msg_box.appendChild(t);
        msg_list.appendChild(msg_box);
    } );
    var chatbox = document.getElementById("chatbox");
    chatbox.innerHTML = "";
    chatbox.setAttribute("class", "list-group");
    chatbox.appendChild(msg_list);
});

function sendChat() {
    var message = document.getElementById("to_send").value;
    document.getElementById("to_send").value = "";
    socket.emit("chat", {room: current_room, msg: message});
};

function changeRooms(to_room) {
    var to_room = document.getElementById("room_picker").value;
    document.getElementById("room_picker").value = "";
    console.log("leaving " + current_room)
    socket.emit("leave", {room: current_room});
    current_room = to_room
    console.log("joining " + current_room)
    socket.emit("join", {room: current_room});
};