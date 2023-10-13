if (Modernizr.addTest('svgasimg', document.implementation.hasFeature('http://www.w3.org/TR/SVG11/feature#Image', '1.1'))) {
  a = $('[class*="-png"]');
  a.each(function(i, obj) {
    var iterator = obj.classList.entries();
    for(var value of iterator) {
      if(/-png/.test(value)) {
        cl = value[1];
        $(obj).removeClass(cl);
        ej = cl.replace(/-png$/,"");
        $(obj).addClass(ej)
      }
    }
  });
  a = $('[class*="illo-container"]');
  a.each(function(i, obj) {
    var iterator = obj.classList.entries();
    for(var value of iterator) {
      if(/illo-container/.test(value)) {
        cl = value[1];
        $(obj).removeClass(cl);
        svg = $(obj).find('img').attr('src');
        svgSrc = svg.replace(/png/g,"svg").replace(/@3x/,"");
        $(obj).find('img').attr("src",svgSrc)
      }
    }
  });
  a = $('[class*="img-svg"]');
  a.each(function(i, obj) {
    pngSrc = $(obj).attr('src');
    svgSrc = pngSrc.replace(/png/g,"svg");
    $(obj).attr("src",svgSrc);
  });
}
