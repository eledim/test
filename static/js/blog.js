var html = $(".article")[0].outerHTML
ajax_get_blog_title(function (data) {
    data = data.response
    for(var a in data){
        var $html = $(html)
        $html.find("a").text(data[a].title)
        var time = getTime(data[a].create_time)
        $html.find(".time").text(time)
        $html.find("a").attr('href','/article/'+data[a].id)
        $(".articlelist").append($html)
    }
})
function getTime(data) {
    var time = (data + "")
    if (time == 'null' || time == "")
        return ''
    time = time.slice(0, 4) + '/' + time.slice(4, 6) + '/' + time.slice(6, 8) + ' '
        + time.slice(8, 10) + ':' + time.slice(10, 12) + ':' + time.slice(12, 14)
    return time
}


