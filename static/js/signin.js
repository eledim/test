//添加cookie并跳转主页
var setCookieAndRedirectToHome = function (ajax_data, params) {
    if (ajax_data.stat == "ok") {
        //逻辑移到后端
        // if (params.username != $.cookie('username')) {
        //     $.cookie('username', params.username, {expires: 30});
        //     $.cookie('password', params.password, {expires: 30});
        // }
        $('form').fadeOut(500);
        $('.wrapper').addClass('form-success');
        $(location).attr('href', site + "blog");/*?username=" + params.username);*/
        console.log("signin success");
    } else {
        //$(location).attr('href', site + "signin");
        $("#signin_info").show().text("Password wrong.")
        $("#signin_info").fadeOut(5000);
        console.log("signin failed");
    }
    //$(document.body).html(data);
};
// 登录
$('#login-button').click(function (event) {
    event.preventDefault();
    var username = $("input[name=username]").val()
    var password = $("input[name=password]").val()
    if (username != "" && password != "")
        ajax_singin(username, password, setCookieAndRedirectToHome);
});

