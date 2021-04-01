/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
Use {} instead of new Object()
Use "" instead of new String()
Use 0 instead of new Number()
Use false instead of new Boolean()
Use [] instead of new Array()
Use /()/ instead of new RegExp()
Use function (){} instead of new Function()

var x1 = {};           // new object
var x2 = "";           // new primitive string
var x3 = 0;            // new primitive number
var x4 = false;        // new primitive boolean
var x5 = [];           // new array object
var x6 = /()/;         // new regexp object
var x7 = function(){}; // new function object

var x = 5 + 7;       // x.valueOf() is 12,  typeof x is a number
var x = 5 + "7";     // x.valueOf() is 57,  typeof x is a string
var x = "5" + 7;     // x.valueOf() is 57,  typeof x is a string
var x = 5 - 7;       // x.valueOf() is -2,  typeof x is a number
var x = 5 - "7";     // x.valueOf() is -2,  typeof x is a number
var x = "5" - 7;     // x.valueOf() is -2,  typeof x is a number
var x = 5 - "x";     // x.valueOf() is NaN, typeof x is a number
*/

'use strict';

function select(element){
	let links = document.querySelectorAll(element);
	return links;
}

var a = select('a');

console.log(a);
/*
let anchorlinks = document.querySelectorAll('a[href^="#"]');

for (let item of anchorlinks) { // relitere 
    item.addEventListener('click', (e)=> {
        let hashval = item.getAttribute('href');
        let target = document.querySelector(hashval);
        target.scrollIntoView({
            behavior: 'smooth'
        });
        history.pushState(null, null, hashval);
        e.preventDefault();
    });
}
*/

$('.counter').each(function() {
  var $this = $(this),
      countTo = $this.attr('data-count');
  
  $({ countNum: $this.text()}).animate({
    countNum: countTo
  },{

    duration: 2000,
    easing:'linear',
    step: function() {
      $this.text(Math.floor(this.countNum));
    },
    complete: function() {
      $this.text(this.countNum);
      //alert('finished');
    }

	});  
});

$(document).ready(function() {
    
    /* Every time the window is scrolled ... */
    $(window).scroll( function(){    
        /* Check the location of each desired element */
        $('.hideme').each( function(){
            //var bottom_of_object = $(this).offset().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            var top_of_object = $(this).offset().top;
            //var top_of_window = $(window).scrollTop();
						//console.log(top_of_object);
						//console.log(bottom_of_window);
            /* If the object is completely visible in the window, fade it it */
            if( top_of_object < bottom_of_window ){                
              $(this).animate({'opacity':'1'},600);                    
            }            
        });
    });    
});