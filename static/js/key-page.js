$(function () {
    var keyTable = $('#key_table').DataTable({
        // columns: [{
        //     "data": "level"
        // }, {
        //     "data": "dungeon"
        // }, {
        //     "data": "user"
        // },  ],
        columns: [
            {title: "副本", "class": "center"},
            {title: "等级", "class": "center"},
            {title: "用户昵称", "class": "center"},
            {title: "职业", "class": "center"},
        ],
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
    });

    /**
     * 返回表格行数组
     * @param data
     * @returns
     */
    var handleTableRows = function (data) {
        var rows = data.map(function (row) {
            return new KeyRow(row).getRow();
        });
        return rows;
    };

    /**
     * 回调，渲染表格数据
     * @param data
     */
    var updateTable = function (data) {
        var rows = handleTableRows(data);
        keyTable.clear();
        keyTable.rows.add(rows).draw();
    };

    /**
     * 回调，校验cookie用户密码
     * 逻辑移到后端
     * @param data
     */
    // var checkCookie = function (data) {
    //     if (data.stat == "ok") {
    //         console.log("sinin success");
    //     } else {
    //         redirectToSignin();
    //     }
    //     //$(document.body).html(data);
    // };

    /**
     * 重定向到登录页面
     */
    var redirectToSignin = function () {
        $(location).attr('href', site + "signin");
    }

    /**
     * 校验页面cookie，失败则重定向到登录页面
     * 逻辑移到后端
     */
    // ajax_singin($.cookie('username'), $.cookie('password'), checkCookie, redirectToSignin);

    /**
     * 回调，更新表格
     */
    var query_key = function () {
        $(".dataTables_filter input").addClass("form-control search-input");
        ajax_query_key(updateTable);
    };

    //添加key后，回调查询key方法
    $("#confirm_key").on("click", function () {
        ajax_confirm_key(function (data) {
            if(data.stat == "ok")
                query_key();
        });
    });

    //注销
    $("#logout").on("click", function (event) {
        event.preventDefault();
        ajax_logout(redirectToSignin);
        // $.cookie('username', null);
        // $.cookie('password', null);
    });

    //页面载入后执行
    query_key();
})