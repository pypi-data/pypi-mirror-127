
try {
  new Function("import('/hacsfiles/frontend/main-f8fe83ef.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-f8fe83ef.js';
  document.body.appendChild(el);
}
  