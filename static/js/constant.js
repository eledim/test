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
