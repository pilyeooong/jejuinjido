// // window.onload = function () {
//   // const logBox = document.querySelector('.congestion-log');
//   // const scrollMessage = document.querySelector('.scroll-guide');

//   // function hoverEvent() {
//   //   scrollMessage.style.display = 'block';
//   //   setTimeout(() => {
//   //     scrollMessage.style.display = 'none';
//   //   }, 1500);
//   //   removeEventListener('mouseover', hoverEvent);
//   // }

//   // logBox.addEventListener('onload', hoverEvent);
// // };

// window.onload = function () {
//   const info = document.querySelector('.color-info');

//   console.log(info);
//   info.addEventListener('click', function () {
//     console.log('123');
//   })

//   const sticker = document.querySelector('.sticker');
//   console.log(sticker);
//   sticker.addEventListener('click', function () {
//     alert('ccc');
//   })
// }

const categoryMenu = document.querySelector('.category-menu');
const categoryList = document.querySelector('.category-list');
const body = document.querySelector('body');

function onOverMenu() {
  categoryList.style.display =
    categoryList.style.display === 'none' ? 'block' : 'none';
}
categoryMenu.addEventListener('click', function () {
  categoryList.style.display =
    categoryList.style.display === 'none' ? 'block' : 'none';
});

categoryMenu.addEventListener('mouseover', onOverMenu);
categoryList.addEventListener('mouseover', function () {
  categoryList.style.display = 'block';
});
categoryList.addEventListener('mouseout', function () {
  categoryList.style.display = 'none';
});
