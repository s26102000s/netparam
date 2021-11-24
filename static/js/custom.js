/*==================================================================================
    Custom JS (Any custom js code you want to apply should be defined here).
====================================================================================*/






$(window).scroll(startCounter);

function startCounter(){
    if ($(window).scrollTop() > 500){
        $(window).off("scroll", startCounter);
        $('.counter').each(function () {
            $(this).prop('Counter',0).animate({
                Counter: $(this).text()
            }, {
                duration: 3000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
        
    }
}






