// 查看文章页面
var $content_text = $(".content_text")
var $title = $(".article_title")
var $article_time = $('.article_time')
params ={
    id:window.location.pathname
}

ajax_get_blog_content(params,function (data) {
    data = [data.response]
    for(var a in data){
        $content_text.append(data[a].content)
        //$content_text.text(data[a].content)
        $title.text(data[a].title)
        $article_time.text(getTime(data[a].create_time))
        $(".edit_article a").attr('href','/edit_blog/'+data[a].id)
        if (data[a].is_edit == 1)
            $(".edit_article").show();
    }
})
