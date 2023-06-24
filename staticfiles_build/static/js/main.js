var bars = document.querySelectorAll('.bars');

bars.forEach(function(bar) {
  bar.addEventListener('click', function() {
    var list = document.querySelectorAll('.bars-active');
    list.forEach(function(element) {
        if(element!=bar)
            element.classList.remove('bars-active');
    });
    this.classList.toggle('bars-active');
    document.querySelector('.lookup').classList.add('lookup-active');
    if (document.querySelectorAll('.bars-active').length == 0) {
        document.querySelector('.lookup').classList.remove('lookup-active');
    }
    console.log('clicked');
  });
});

// function removeSlider() {
//     var list=
// }
