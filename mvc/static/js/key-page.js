var ajax_sendKey = function(fnSuccess, fnError) {
	var data =  {
		dungeon: $("#dungeon").find("option:selected").text(),
		level:$("#level").val(),
		username:$.cookie('username'),
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
        ],
		dom:'<"top"lf>rt<"bottom"ip><"clear">',
	});

	var updateTable = function(data){
		oNodeTable.clear();
		oNodeTable.rows.add(data).draw();
	};

	var checkCookie = function(data){
		if(data.stat == "ok"){
			console.log("sinin success");
		}else{
			reLocation();
		}
		//$(document.body).html(data);
	};
	var reLocation = function(){
	    $(location).attr('href', site + "signin");
    }
	ajax_singin($.cookie('username'),$.cookie('password'),checkCookie,reLocation);

	var query_key = function(){
	    ajax_query_key(updateTable);
    };

	query_key();

	$("#confirm_key").on("click",function () {
		ajax_sendKey(query_key);
	});

	$("#logout").on("click",function () {
		event.preventDefault();
		$(location).attr('href', site + "signin");
		$.cookie('username',null);
		$.cookie('password',null);
	});


})