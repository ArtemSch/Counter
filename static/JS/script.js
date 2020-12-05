$('.cube-red').hover( ()=>{
    var request = $.ajax({
        url: "/add",
        method: "GET",
        data: { cub : 2, val:1},
        dataType: "json"
        })

request.done(( msg )=> {
    $('.cube-red').text(msg.val)
    console.log('res red',msg.val)
    })

request.fail(( jqXHR, textStatus )=> {
    console.log(jqXHR,textStatus)
    })

})

$('.cube-green').hover( ()=>{

    var request = $.ajax({
        url: "/add",
        method: "GET",
        data: { cub : 1, val:1},
        dataType: "json"
        })

request.done(( msg )=> {
    $('.cube-green').text(msg.val)
    console.log('res green',msg.val)
    })

request.fail(( jqXHR, textStatus )=> {
    console.log(jqXHR,textStatus)
    })

})