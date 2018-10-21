var ajax_sendKey = function(fnSuccess, fnError) {
		$.ajax({
			type: "post",
			url: site + "confirm_key",
			dataType: "json",
			cache:false,
			data: {
				dungeon: $("#dungeon").find("option:selected").text(),
                level:$("#level").val(),
				username:$.cookie('username'),
			},
			success: function(data) {
				if (fnSuccess != undefined && typeof(fnSuccess) == "function") {
					fnSuccess();
				}
			},
			error:function(){
				if (fnError != undefined && typeof(fnError) == "function") {
					fnError();
				}
			}
		});
	};
var ajax_query_key = function(fnSuccess, fnError) {
		$.ajax({
			type: "post",
			url: site + "query_key",
			dataType: "json",
			cache:false,
			data: {
			},
			success: function(data) {
				if (fnSuccess != undefined && typeof(fnSuccess) == "function") {
					fnSuccess(data);
				}
			},
			error:function(){
				if (fnError != undefined && typeof(fnError) == "function") {
					fnError();
				}
			}
		});
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
        ]
	});

	var updateTable = function(data){
		oNodeTable.clear();
		oNodeTable.rows.add(data).draw();
	}
	var checkCookie = function(username,password,data){
		if(data.indexOf('ok') != -1){
			console.log("sinin success");
		}else{
			$(location).attr('href', site + "signin");
		}
		//$(document.body).html(data);
	};
	ajax_singin($.cookie('username'),$.cookie('password'),checkCookie);

	var query_key = function(){
	    ajax_query_key(updateTable);
    }
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