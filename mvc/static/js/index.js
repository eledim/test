
new Vue({
    el: '#level',
    delimiters:['[[', ']]'],
    data: {
        items: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    },
    methods:{

    }
})
// var  site = 'http://eledim.xyz/';
var  site = 'http://127.0.0.1:5000/'
var sendKey = function(fnSuccess,fnError) {
		$.ajax({
			type: "post",
			url: site + "confirm_key",
			dataType: "json",
			cache:false,
			data: {
				dungeon: $("#dungeon").find("option:selected").text(),
                level:$("#level").val(),
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
var query_key = function(fnSuccess,fnError) {
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
	query_key(updateTable);
	$("#confirm_key").on("click",function () {
	   sendKey();
	   query_key(updateTable);
	});
})