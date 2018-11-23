
// var  site = 'http://eledim.xyz/';
var  site = 'http://127.0.0.1:5000/'
//var  site = 'http://192.168.43.135/'
var ajax = function(params, url,fnSuccess, fnError) {
	$.ajax({
		type: "post",
		url: site + url,
		dataType: "json",
		cache:false,
		data: params,
		success: function(data) {
			if (fnSuccess != undefined && typeof(fnSuccess) == "function") {
				fnSuccess(data,params);
			}
		},
		error:function(data){
			if (fnError != undefined && typeof(fnError) == "function") {
				fnError(data,params);
			}
		}
	});
};