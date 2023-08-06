
try {
  new Function("import('/hacsfiles/frontend/main-581bee61.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-581bee61.js';
  document.body.appendChild(el);
}
  