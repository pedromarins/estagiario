/**
 * Save/remove bookmarks to/from the bookmark menu item and the database
 *
 * @param string url        The current page url path (request.get_full_path)
 * @param string title      The current page title
 * @param string prompt_msg The message to ask for prompting
 * @return void
 */


/*********************/
/*      STRINGS      */
/*********************/


/**
* Check if <item> is in the AssociativeArray <list>
*/
var str_in_list = function(item, list){
    for (i in lst){
        if (lst[i] == text){ return true; }
    };
    return false;
};






/* remove key from obj */
var remove_key = function(key, obj){
    new_obj = new Object();
    for (k in obj) {
        if (k != key){
            new_obj[k] = obj[k];
        }        
    }
    return new_obj;
}



/*********************/
/*        URLS       */
/*********************/


/**
*  HashMap with GET params from window.location  
*  foo.com?arg1=a&arg2=b => {'arg1':'a', 'arg2':'b'}
*/
var get_params = function(){
    var _url_params = new Object();
    var e,
        a = /\+/g,  // Regex for replacing addition symbol with a space
        r = /([^&=]+)=?([^&]*)/g,
        d = function (s) { return decodeURIComponent(s.replace(a, " ")); },
        q = window.location.search.substring(1);
    while (e = r.exec(q))
       _url_params[d(e[1])] = d(e[2]);
   return _url_params;
};



/*
    path_redirect({'uf': 'rj'});
    path_redirect({'uf': 'rj', 'field': 'direito'});
    path_redirect({'field': 'direito'});

var a = '/estagios/ ';
var b = '/estagios/rj/';

var FIELDS = ['estagios', 'administracao', 'direito', 'engenharia', 'economia', 'informatica', 'design', 'publicidade', 'outros']


alert("RJ".length==2);
alert("RJA".length==2);
//get_url_param(1);
//get_url_param(2);
//get_url_param(3);
*/


var get_path = function(){
    var url = window.location.protocol + '//' + window.location.hostname;
    if (window.location.port!=80){
        url += ':'+window.location.port;
    }
    return url + '/'
}

var UrlManager = function(){
    this.params = get_params();
    
    this.get_url_param = function(i){
        var array = window.location.pathname.split('/');
        return array[i];
    } 

    /* add or replace a GET param */
    this.set_param = function(k, v){
        this.params[k] = v;
    };

    /* removes GET param */
    this.del_param = function(k){
        this.params = remove_key(k, this.params);
    };

    this.redirect = function(data){
        if (!data) {
            var data = {};
        };


        var field = this.get_url_param(1);
        if (data['field']){
            field = data['field'];
        } else {
            //field = 'estagios';
            //alert('no field');
        };

        
        if (data['uf']){
            var uf = data['uf'];
            this.del_param('cidade');
        } else {
            var uf = this.get_url_param(2);
        };

        var url = get_path()
        if (field){
            url += field + '/';
        };

        if (uf){
            url += uf + '/';
        };

        url += '?';
        location.replace(url + jQuery.param(this.params));

        //alert(this.params['tags']);
        //alert(window.location.href);
        //     alert(jQuery.param(this.params));

        //     var url = window.location.protocol + '//' + window.location.hostname; //+ window.location.pathname;
        //     alert(url);
        //     //window.location.href = '?' + jQuery.param(this.params);
        //     alert('redirect');
        //     //window.location.href = '/';
        // alert('top');
        //     //window.location.replace('/');
        //     //window.location = '/';
        //window.location.search = '';
        //window.location.href = '/estagios/';
        
        //this.get_url_param(i)

        //location.replace("http://localhost:8000/");  
    };


};





//     var state_redirect(uf){
        
//     }

//     var a = '/estagios/ ';
//     var b = '/estagios/rj/';
//     var c = '/engenharia/';
//     var d = '/engenharia/rj/';
//     

//     //alert(str_in_list('contato', FIELDS));
    

