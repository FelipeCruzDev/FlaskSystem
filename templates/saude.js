const bars = document.querySelectorAll('.bar');

bars.forEach(bar => {
  const value = bar.getAttribute('data-value');
  bar.style.setProperty('--value', `${value}%`);
});
