// 添加文章，修改文章页面

params = {
    id: window.location.pathname
}
ajax_get_blog_content(params,function (data) {
    data = [data.response]
    for(var a in data){
        editor.txt.html(data[a].content)
        $("#title").val(data[a].title)

    }
})


   $("#add_blog").on("click",function () {
       var txt = $("textarea").val()
       var title = $("#title").val()
       txt = editor.txt.html()
       // txt = editor.txt.text()
       // editor.txt.clear()
       // editor.txt.append('<p>追加的内容</p>')
       var params = {
           title:title,
           content:txt,
           create_time:parseInt(getFullTime())
       }
        ajax(params, "do_add_blog",doSuccess(function (data) {
            alert("添加成功:"+data.response)
            $(location).attr('href', site + 'article/'+data.response);
        }));
   })


   $("#edit_blog").on("click",function () {
       var txt =  editor.txt.html()
       var title = $("#title").val()
       var params = {
           title: title,
           content: txt,
           modify_time: parseInt(getFullTime()),
           id: window.location.pathname
       }
        ajax(params, "do_edit_blog",doSuccess(function (data) {
            alert("修改成功:"+data.response)
            $(location).attr('href', site + 'article/'+data.response);
        }));
   })


   $("#delete_blog").on("click",function () {
       var params = {
           id:window.location.pathname,
           state:1
       }
        ajax(params, "do_edit_blog",doSuccess(function (data) {
            alert("回收成功:"+data.response)
            $(location).attr('href', site + 'blog' );
        }));
   })
  // boom(p1,((fun)=>(data)=>(data?fun(data):null))((data)=>(""+data)))

