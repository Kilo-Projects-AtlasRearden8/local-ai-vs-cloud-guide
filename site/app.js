// Running AI Locally vs. Cloud — site interactivity
// Asdale Dynamics, LLC

(function () {
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.mobile-menu');

  if (!toggle || !menu) return;

  toggle.addEventListener('click', function () {
    var open = menu.classList.contains('open');
    menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
  });

  // Close menu when a link is clicked
  var links = menu.querySelectorAll('a');
  links.forEach(function (link) {
    link.addEventListener('click', function () {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
})();
