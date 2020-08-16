window.onload = function () {
  const logBox = document.querySelector('.congestion-log');
  const scrollMessage = document.querySelector('.scroll-guide');

  function hoverEvent() {
    scrollMessage.style.display = 'block';
    setTimeout(() => {
      scrollMessage.style.display = 'none';
    }, 1500);
    removeEventListener('mouseover', hoverEvent);
  }

  logBox.addEventListener('onload', hoverEvent);
};
