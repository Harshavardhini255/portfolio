(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  document.documentElement.classList.add("js");

  var progressBar = $("#progressBar");
  var queued = false;

  function onScroll() {
    if (!progressBar) return;
    var y = window.pageYOffset || document.documentElement.scrollTop;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    progressBar.style.width = (h > 0 ? (y / h) * 100 : 0) + "%";
  }

  window.addEventListener("scroll", function () {
    if (queued) return;
    queued = true;
    window.requestAnimationFrame(function () { onScroll(); queued = false; });
  }, { passive: true });
  onScroll();

  var revealables = $$(".phero__title, .phero__cat, .chips, .blk, .res, .pn");
  if (reduced || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      var delay = 0;
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        setTimeout(function () { el.classList.add("is-in"); }, delay);
        delay += 60;
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  var year = $("#year");
  if (year) year.textContent = new Date().getFullYear();
})();
