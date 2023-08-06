
try {
  new Function("import('/hacsfiles/frontend/main-17b14c19.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-17b14c19.js';
  document.body.appendChild(el);
}
  