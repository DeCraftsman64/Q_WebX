
(function ($) {
    "use strict";


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');
    const alert1 = 'alert-validate';
    const alert2 = 'alert-validate3'

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i], alert1);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        if ($(this).parent().data("state") === "True") {
            showValidate(this, alert2);
        }
        $(this).focus(function(){
           hideValidate(this,alert1);
           hideValidate(this, alert2)
        });

    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input , alert_type) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass(alert_type);
    }

    function hideValidate(input, alert_type) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass(alert_type);
    }
    
    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    $('.btn-show-pass').on('click', function(){
        if(showPass == 0) {
            $(this).next('input').attr('type','text');
            $(this).find('i').removeClass('fa-eye');
            $(this).find('i').addClass('fa-eye-slash');
            showPass = 1;
        }
        else {
            $(this).next('input').attr('type','password');
            $(this).find('i').removeClass('fa-eye-slash');
            $(this).find('i').addClass('fa-eye');
            showPass = 0;
        }
        
    });
    

})(jQuery);