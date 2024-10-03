function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.display = (menu.style.display === "none" || menu.style.display === "") ? "block" : "none";
}

//кнопка лайка, пока что не знаю нужен ли? но оно работает!
// document.addEventListener('DOMContentLoaded', function(){
//     const likeButtons = document.querySelectorAll('.like-icon');
//     likeButtons.forEach(function(likeBtn){
//     let isliked = false;

//     likeBtn.addEventListener('click', function() {
//         isliked = !isliked;

//         if (isliked){
//             likeBtn.src = './images/menu-page-img/Q-liked.svg';
//         }   else    {
//             likeBtn.src = './images/menu-page-img/Q-like.svg';
//         }
//         });
//     });
// });
