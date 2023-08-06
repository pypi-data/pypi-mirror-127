
try {
  new Function("import('/hacsfiles/frontend/main-01106cc7.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-01106cc7.js';
  document.body.appendChild(el);
}
  