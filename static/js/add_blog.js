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
            alert("添加成功")
        }));
   })

  // boom(p1,((fun)=>(data)=>(data?fun(data):null))((data)=>(""+data)))

