function like(like){
    var likecount = document.getElementById(like)
    console.log(like.innerText)
    like.innerText++
    console.log (like.innerText)
}

function toggle(element){element.remove();
}