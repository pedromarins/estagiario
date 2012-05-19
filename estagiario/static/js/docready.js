

// var get_params = function(){
//     var _url_params = {};
//     var e,
//         a = /\+/g,  // Regex for replacing addition symbol with a space
//         r = /([^&=]+)=?([^&]*)/g,
//         d = function (s) { return decodeURIComponent(s.replace(a, " ")); },
//         q = window.location.search.substring(1);

//     while (e = r.exec(q))
//        _url_params[d(e[1])] = d(e[2]);
//    return _url_params;
// };

var redirect_to_params = function(params){
    window.location.href = '?' + jQuery.param(params);
};


var start_filter = function(container){
    var params = get_params();
    
    $(container).each(function(){
        $(this).click(function(event){
            event.preventDefault();
            var val = $(this).attr('data-val');
            var key = $(this).attr('data-param');
            
            if (!val){
                //delete params[key];    
                //redirect_to_params(params);
                alert('asd');
                var $url = new UrlManager(1);
                $url.del_param(key);
                return $url.redirect();
            }            
            

            if (params[key]){                
                // change filter value
                if (params[key] != val){
                    params[key] = val;    
                    redirect_to_params(params);
                } else {
                    //alert('adicionar ou limpar?');
                    return;
                }
            
            } else {
                if (val){
                    params[key] = val;
                    redirect_to_params(params);
                    
                } else {
                    return;
                }
                
            }
    })
    

    });
};







$(document).ready(function() {

    start_filter('#tag-filter a');
    $('#id-state-select').change(function() {
        //alert($(this).attr('value'));
        //window.location.href = '/' + $(this).attr('value') + '/';

        //var params = get_params();
        //params['uf'] = $(this).attr('value');
        //redirect_to_params(params);
        var $url = new UrlManager();
        return $url.redirect({'uf': $(this).attr('value')});
    

    });
    
    start_filter('#hours-filter a');
    start_filter('#city-filter a');
    start_filter('#size-filter a');
    
    $("a.field-link").click(function(){
        //alert($(this).attr("href"));
        return
    });

    // path_redirect({'uf': 'rj'});
    // path_redirect({'uf': 'rj', 'field': 'direito'});
    // path_redirect({'field': 'direito'});



// Example querystring:

// ?i=main&mode=front&sid=de8d49b78a85a322c4155015fdce22c4&enc=+Hello%20&empty

// Result:

// urlParams = {
//     enc: " Hello ",
//     i: "main",
//     mode: "front",
//     sid: "de8d49b78a85a322c4155015fdce22c4",
//     empty: ""
// }

//alert(urlParams["mode"]);
// -> "front"

// //alert("empty" in urlParams);
// // -> true

// var myParams = {name: "Amit Jain",days:['Mon','Tue','Sat'] };
// 2
// jQuery.param(myParams);
// 3
 
// 4
// Output: "name=Amit+Jain&days%5B%5D=Mon&days%5B%5D=Tue&days%5B%5D=Sat"
// 1
// var myParams = {name: "Diana",address:{



//alert($.param(urlParams));
});