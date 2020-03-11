var $content_text = $(".content_text")
var $title = $(".title")
params ={
    id:window.location.pathname
}
ajax_get_blog_content(params,function (data) {
    data = [data.response]
    for(var a in data){
        $content_text.append(data[a].content)
        //$content_text.text(data[a].content)
        $title.text(data[a].title)
    }
})
