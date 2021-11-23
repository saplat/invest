var socket = new WebSocket('ws://localhoste:8000/ws/graph/');

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData)

    document.querySelector('#app').innerText = djangoData.value;
}