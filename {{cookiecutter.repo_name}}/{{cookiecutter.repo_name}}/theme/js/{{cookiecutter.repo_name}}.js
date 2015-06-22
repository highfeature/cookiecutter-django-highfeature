/** Init **/
jQuery(window).ready(function () {
    toTop();
    topNav();
});

/** 00 To Top **/
function toTop() {
    $(window).scroll(function() {
        if ($(this).scrollTop()) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    });
    $("#toTop").click(function() {
        $("html, body").animate({scrollTop: 0}, 1000);
    });
}

/** 01 Top Nav **/
function topNav() {
	jQuery(window).scroll(function() {
		topMain(); // on scroll
	});	topMain(); // on load


	window.topNavSmall = false;
	function topMain() {
		var _scrollTop 	= jQuery(document).scrollTop();

		if(_scrollTop > 0) {
            $('.navbar-fixed-top').stop().animate({height:'50px', padding:'0'},300);
//			jQuery('#header_shadow').stop().animate({ 'top':'30px'},400);/* just a little visible */
			window.topNavSmall = true;
		}

		if(window.topNavSmall === true && _scrollTop < 3) {
            $('.navbar-fixed-top').stop().animate({padding:'20px 0', height:'92px'},300);
//			jQuery('#header_shadow').stop().animate({ 'top':'92px'},400);
			window.topNavSmall = false;
		}
	}
}

