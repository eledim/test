var ajax_sendKey = function(fnSuccess, fnError) {
	var data =  {
		dungeon: $("#dungeon").find("option:selected").text(),
		level:$("#level").val(),
		username:$.cookie('username'),
        character:$("#character").find("option:selected").text(),
	};
	ajax(data,"confirm_key", fnSuccess, fnError);
};

var ajax_query_key = function(fnSuccess, fnError) {
	ajax(null,"query_key",fnSuccess,fnError);
};

$(function () {
	var oNodeTable = $('#key_table').DataTable({
        // columns: [{
        //     "data": "level"
        // }, {
        //     "data": "dungeon"
        // }, {
        //     "data": "user"
        // },  ],
		columns: [
            { title: "副本","class": "center" },
            { title: "等级" ,"class": "center" },
            { title: "用户昵称" ,"class": "center" },
            { title: "职业" ,"class": "center" },
        ],
		dom:'<"top"lf>rt<"bottom"ip><"clear">',
	});
    var handleTableRows =function(data){
        var rows = data.map(function (row) {
            return new KeyRow(row).getRow();
        });
        return rows;
    };

    /**
     * 回调，渲染表格数据
     * @param data
     */
	var updateTable = function(data){
	    var rows = handleTableRows(data);
		oNodeTable.clear();
		oNodeTable.rows.add(rows).draw();
	};
    /**
     * 回调，校验cookie用户密码
     * @param data
     */
	var checkCookie = function(data){
		if(data.stat == "ok"){
			console.log("sinin success");
		}else{
			reLocation();
		}
		//$(document.body).html(data);
	};
    /**
     * 重定位
     */
	var reLocation = function(){
	    $(location).attr('href', site + "signin");
    }
	ajax_singin($.cookie('username'),$.cookie('password'),checkCookie,reLocation);
    /**
     * 回调，更新表格
     */
	var query_key = function(){
	    $(".dataTables_filter input").addClass("form-control search-input");
	    ajax_query_key(updateTable);
    };

	query_key();

	$("#confirm_key").on("click",function () {
		ajax_sendKey(query_key);
	});

	$("#logout").on("click",function () {
		event.preventDefault();
		reLocation();
		$.cookie('username',null);
		$.cookie('password',null);
	});


})