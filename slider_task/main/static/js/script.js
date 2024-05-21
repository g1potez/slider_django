$(document).ready(function() {
      
      $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav, .slider-zoom',
        speed: 100,
      });
      
      $('.slider-nav').slick({
        slidesToShow: 5,
        centerMode: true,
        focusOnSelect: true,
        asNavFor: '.slider-for, .slider-zoom',
        responsive: [
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 3,
            }
          },
          {
            breakpoint: 401,
            settings: {
              slidesToShow: 1,
            }
          }
        ]
      });

    $('.slider-for .slider-wrapper img').on('click', function() {
        $('.content__imageZoom').css('display', 'flex');
        let getSrc = $('.slider-for .slick-active img').attr('src');
        $('.imageZoom__image img').attr('src', getSrc);
    })
    $('.imageZoom__closeBtn').on('click', function() {
        $('.content__imageZoom').css('display', 'none')
    })

    // changeForm
    $('#changeToRegister').on('click', function() {
      $('.account__signin').css('display', 'none');
      $('.account__signup').css('display', 'block');
    })
    $('#changeToAuth').on('click', function() {
      $('.account__signup').css('display', 'none');
      $('.account__signin').css('display', 'block');
    })

    //usernameInfo
    $('.usernameInfo .usernameInfo__username').on('click', function() {
      $('.usernameInfo .usernameInfo__menu').toggle('active')
    })
})