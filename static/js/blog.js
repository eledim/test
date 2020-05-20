// 博客主页面，文章列表
// var html = $(".article")[0].outerHTML
html = '<li class="article">\n' +
    '                    <a href="#"></a>\n' +
    '                    <div class="time"></div>\n' +
    '                </li>'
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



