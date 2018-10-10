
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
                levle:$("#level").val(),
			},
			success: function(data) {
				fnSetTotalNodes(data);
				if (fnSuccess != undefined && typeof(fnSuccess) == "function") {
					fnSuccess();
				}
			},
			error:function(){
				console.info("Pool:fnAjaxQueryTotalNodes error.");
				if (fnError != undefined && typeof(fnError) == "function") {
					fnError();
				}
			}
		});
	};
$("#confirm_key").on("click",function () {
   sendKey();
});