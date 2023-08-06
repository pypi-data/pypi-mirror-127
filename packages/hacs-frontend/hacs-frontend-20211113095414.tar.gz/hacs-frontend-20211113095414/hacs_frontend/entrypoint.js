
try {
  new Function("import('/hacsfiles/frontend/main-8aba92c7.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-8aba92c7.js';
  document.body.appendChild(el);
}
  