$('document').ready(function(){
  var stickyNavTop = $('#navbar').offset().top;
  var stickyNav = function(){
    var scrollTop = $(window).scrollTop();
    if (scrollTop > stickyNavTop){
      $('#navbar').addClass('sticky'); 
      $('#body').addClass('push');
    }else {
      $('#navbar').removeClass('sticky');
      $('#body').removeClass('push');
    }
  };

  //Call the sticky navbar function
stickyNav();
$(window).scroll(function(){
  stickyNav();
});

});
