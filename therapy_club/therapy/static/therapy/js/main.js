document.addEventListener('DOMContentLoaded', function() {

  // const swiper = new Swiper('.swiper', {
  //   // Optional parameters
  //   direction: 'horizontal',
  //   loop: true,
  
  //   // If we need pagination
  //   pagination: {
  //     el: '.swiper-pagination',
  //   },
  //   effect:'cube',
  //   speed:500,
    
  //   grabCursor:true,
  //   // Navigation arrows
  //   navigation: {
  //     nextEl: '.swiper-button-next',
  //     prevEl: '.swiper-button-prev',
  //   },
  
  //   // And if we need scrollbar
  
  // });
  
  redButton = document.querySelector('.btn-5');
  miniButton = document.querySelector('.mini-btn');
  setTimeout(() => {
    
    miniButton.classList.add('active');
    redButton.classList.add('active');
    redButton.classList.add('slide-from-right');
    miniButton.classList.add('slide-from-right');
   

  }, 500);
  
  
  document.querySelector('.burger').addEventListener('click', function(){
    this.classList.toggle('burger-active');
   document.querySelector('.nav-menu').classList.toggle('open'); 
  })

 modalButton = document.querySelector('#js-open-modal')
 miniModalButton = document.querySelector('#mini-js-open-modal')
 modalContent = document.querySelector('.modal-content')
 overlay = document.querySelector('.overlay')
 closeCrist = document.querySelector('.js-modal-close')

 
 miniModalButton.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.add('active-modal');
  modalContent.classList.add('active-modal');
 });
  
 modalButton.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.add('active-modal');
  modalContent.classList.add('active-modal');
 });

  // закрытие модального окна при клике по крестику
 closeCrist.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.remove('active-modal');
  modalContent.classList.remove('active-modal');
 });

 closeCrist.addEventListener('touchend', (e) =>{ 
  e.preventDefault();
  overlay.classList.remove('active-modal');
  modalContent.classList.remove('active-modal');
 });

 // закрытие модального окна при клике по подложке 
 overlay.addEventListener('click', function() {
  document.querySelector('.modal-content.active-modal').classList.remove('active-modal');
  this.classList.remove('active-modal');
});

 overlay.addEventListener('touchend', function() {
  document.querySelector('.modal-content.active-modal').classList.remove('active-modal');
  this.classList.remove('active-modal');
});

// закрытие бургер-меню при переходе по якорю
 dropdown = document.querySelectorAll('.dropdown-menu');
 nav = document.querySelector('.nav-menu');
 burger = document.querySelector('.burger');

 dropdown.forEach(function(item){
  item.addEventListener('click', function(){
    nav.classList.remove('open');
    burger.classList.remove('burger-active');

  item.addEventListener('touchend', function() {
    nav.classList.remove('open');
    burger.classList.remove('burger-active');

    });

  });

 });

});
// модальное окно страницы категории
document.addEventListener('DOMContentLoaded', function() {
  const photoIcons = document.querySelectorAll('.mini-gallery-card');
  const overlay = document.querySelector('.overlay');
  const modalGallery = document.querySelector('.modal-gallery-content');
  const bigPhotos = document.querySelectorAll('.gallery-slide');
  const leftBtn = document.querySelector('.left-gallery-btn');
  const rightBtn = document.querySelector('.right-gallery-btn');
  const closeGalleryCrist = document.querySelector('.js-gallery-modal-close');

  photoIcons.forEach((item, index) =>{
    item.addEventListener('click', () =>{
      photoIndex = index;
      openModalGallery();
      appendBigPhoto();
    })
  })

const openModalGallery = ()=>{
  overlay.classList.add('active-modal');
  modalGallery.classList.add('active-modal-gallery');
}

const appendBigPhoto = () =>{
  bigPhotos.forEach((item) =>{
    item.style.display = 'none'
  })
  bigPhotos[photoIndex].style.display = 'block'
}

leftBtn.addEventListener('click', ()=> {
  if (photoIndex == 0){
    photoIndex = bigPhotos.length - 1;
    appendBigPhoto();
  }else if (photoIndex != 0){
    photoIndex--;
    appendBigPhoto();
  }else{
    return
  }
  });

rightBtn.addEventListener('click', ()=> {
  if (photoIndex == bigPhotos.length - 1){
    photoIndex = 0;
    appendBigPhoto();
  }else if (photoIndex != bigPhotos.length - 1){
    photoIndex++;
    appendBigPhoto();
  }else{
    return
  }
  });


  
    // закрытие модального окна при клике по крестику
  closeGalleryCrist.addEventListener('click', function() { 
  overlay.classList.remove('active-modal');
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
 });
  closeGalleryCrist.addEventListener('touchend', function() { 
  overlay.classList.remove('active-modal');
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
 });
 // закрытие модального окна при клике по подложке 
 overlay.addEventListener('click', function() {
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
  this.classList.remove('active-modal');
});
 overlay.addEventListener('touchend', function() {
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
  this.classList.remove('active-modal');
});





});

/* модальное окно для новости */
document.addEventListener('DOMContentLoaded', function() {
  if (document.querySelector('.post-modal__cross')){
      post_overlay = document.querySelector('#post-overlay-modal'),
      closeButton = document.querySelector('.post-modal__cross');
      modalElem = document.querySelector('.post-modal');
      checkElem = sessionStorage.getItem("cookie-message");
      if (checkElem == undefined) {
          setTimeout(function(){
              modalElem.classList.add('active');
              post_overlay.classList.add('active');
          },500)
  
        }
      closeButton.addEventListener('click', function(e) {
          var parentModal = this.closest('.post-modal');
           sessionStorage.setItem("cookie-message", true);
           parentModal.classList.remove('active');
           post_overlay.classList.remove('active');
        });
  
         /* закрытие по ESC */
    document.body.addEventListener('keyup', function (e) {
      var key = e.keyCode;
      if (key == 27) {
          sessionStorage.setItem("cookie-message", true);
          document.querySelector('.post-modal.active').classList.remove('active');
          document.querySelector('.post-overlay.active').classList.remove('active');
      };
    }, false);
      /* скрытие окна при клике на подложку */
      post_overlay.addEventListener('click', function() {
          sessionStorage.setItem("cookie-message", true);
          document.querySelector('.post-modal.active').classList.remove('active');
          this.classList.remove('active');
        });
  }
  
  
  });