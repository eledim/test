var setCookieAndReLoc = function(username,password,ajax_data){
	if(ajax_data.indexOf('ok') != -1){
		if(username != $.cookie('username')){
			$.cookie('username',username, { expires: 30 });
			$.cookie('password', password, { expires: 30 });
		}
		$('form').fadeOut(500);
		$('.wrapper').addClass('form-success');
		$(location).attr('href', site + "key_page?username="+username);
		console.log("signin success");
	}else{
		//$(location).attr('href', site + "signin");
		$("#signin_info").show().text("Password wrong.")
		$("#signin_info").fadeOut(5000);
		console.log("signin failed");
	}
	//$(document.body).html(data);
};
$('#login-button').click(function (event) {
	event.preventDefault();
	ajax_singin($("input[name=username]").val(),$("input[name=password]").val(),setCookieAndReLoc);
});
var ajax_singin = function(username,password,fnSuccess, fnError) {
		$.ajax({
			type: "post",
			url: site + "signin",
			dataType: "html",
			cache:false,
			data: {
				username:username,
				password:password,
			},
			success: function(data) {
				if (fnSuccess != undefined && typeof(fnSuccess) == "function") {
					fnSuccess(username,password,data);
				}
			},
			error:function(){
				if (fnError != undefined && typeof(fnError) == "function") {
					fnError();
				}
			}
		});
	};