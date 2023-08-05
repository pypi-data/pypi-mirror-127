
try {
  new Function("import('/hacsfiles/frontend/main-52900fef.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-52900fef.js';
  document.body.appendChild(el);
}
  