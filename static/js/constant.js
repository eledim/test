// var  site = 'http://eledim.xyz/';
// var site = 'http://127.0.0.1:5000/'
// var site = 'http://101.37.116.142:191/'
var site = window.location.protocol + "//" + window.location.host + '/';
//var  site = 'http://192.168.43.135/'
var ajax = function (params, url, fnSuccess, fnError) {
    $.ajax({
        type: "post",
        url: site + url,
        contentType: "application/json",
        dataType: "json",
        cache: false,
        data: JSON.stringify(params),
        success: function (data) {
            if (fnSuccess != undefined && typeof (fnSuccess) == "function") {
                fnSuccess(data, params);
            }
        },
        error: function (data) {
            if (fnError != undefined && typeof (fnError) == "function") {
                fnError(data, params);
            }
        }
    });
};

var ajax_singin = function (username, password, fnSuccess, fnError) {
    var params = {
        username: username,
        password: password,
    };
    ajax(params, "do_signin", fnSuccess, fnError);
};

var ajax_confirm_key = function (fnSuccess, fnError) {
    var data = {
        dungeon: $("#dungeon").find("option:selected").text(),
        level: $("#level").val(),
        username: $.cookie('username'),
        character: $("#character").find("option:selected").text(),
    };
    ajax(data, "confirm_key", fnSuccess, fnError);
};

var ajax_logout = function (fnSuccess) {
    ajax(null, "logout", fnSuccess);
};

var ajax_query_key = function (fnSuccess, fnError) {
    ajax(null, "query_key", fnSuccess, fnError);
};


var ajax_get_blog_title = function (fnSuccess, fnError) {
    ajax(null, "get_blog_title", fnSuccess, fnError);
};

var ajax_get_blog_content = function (params,fnSuccess, fnError) {
    ajax(params, "get_blog_content", fnSuccess, fnError);
};

function doSuccess(func) {
    return function(data){
        if(data.stat == "ok") {
             func(data)
        }
    }
}
// 年月日，时分秒
function getFullTime() {
    let date = new Date(),//时间戳为10位需*1000，时间戳为13位的话不需乘1000
        Y = date.getFullYear() + '',
        M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1),
        D = (date.getDate() < 10 ? '0'+(date.getDate()) : date.getDate()),
        h = (date.getHours() < 10 ? '0'+(date.getHours()) : date.getHours()),
        m = (date.getMinutes() < 10 ? '0'+(date.getMinutes()) : date.getMinutes()),
        s = (date.getSeconds() < 10 ? '0'+(date.getSeconds()) : date.getSeconds());
    return Y + M + D + h + m + s
}

// 获取当前时间戳
function getLocalTime() {
    return new Date().getTime();
}

// 时间戳
function time2TimeStap (timer) {
    return new Date(timer).getTime();
}