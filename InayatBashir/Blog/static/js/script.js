var travelheder=this.document.getElementById("travelheder");
var travelsection=this.document.querySelector(".travelsection");
window.addEventListener('scroll',function(e){
	
	if(this.window.pageYOffset>45){
		travelheder.classList.add("navbar");
		travelheder.nextElementSibling.classList.add('margin_class');
	}else{
		travelheder.classList.remove("navbar");
		travelheder.nextElementSibling.classList.remove('margin_class')
	}
})		

TweenMax.to(".wrapper", 1, {
				top: "-110%",
				ease: Expo.easeInOut,
				delay: 2
			});
			
	var tl = new TimelineMax();
			
	tl.from(".loader", 1, {
				scaleY: "0%",
				y: 80,
				ease: Expo.easeInOut,
				delay: 1,
				transformOrigin:"50% 100%"
	});
			
	tl.to(".loader", 1, {
				height: "20vh",
				scaleY: "0%",
				ease: Expo.easeInOut,
				transformOrigin:"0% -100%"
	});			
			
TweenMax.staggerFrom(
	".nav__links > li ",
				1,
				{
					y: "60",
					opacity: 0,
					ease: Power2.easeOut,
					delay: 3,
				},
				0.2
);
			
TweenMax.staggerFrom(
	".social ",
				1,
				{
					y: "60",
					opacity: 0,
					ease: Power2.easeOut,
					delay: 3.5,
				},
				0.1
	);
TweenMax.staggerFrom(
		".heading_author span",
				1,
				{
					y: "60",
					opacity: 0,
					ease: Power2.easeOut,
					delay: 4,
				},
				0.2
);
TweenMax.staggerFrom(
		".composition img",
				1,
				{
					x: "60",
					opacity: 0,
					ease: Power2.easeOut,
					delay: 5,
				},
				0.2
);

			
const body = document.body,
scrollWrap = document.getElementsByClassName("smooth-scroll-wrapper")[0],
height = scrollWrap.getBoundingClientRect().height - 1,
speed = 0.04;

var offset = 0;

body.style.height = Math.floor(height) + "px";

function smoothScroll() {
offset += (window.pageYOffset - offset) * speed;

			// var scroll = "translateY(-" + offset + "px) translateZ(0)";
scrollWrap.style.transform = scroll;

callScroll = requestAnimationFrame(smoothScroll);
}

smoothScroll();

$(function () {
	var elements = $(".text, .imgg , .continuee").toArray();
	$(window).scroll(function () {
	elements.forEach(function (item) {
	if ($(this).scrollTop() >= $(item).offset().top - 500) {
				$(item).addClass("reveal");
						}
		else{
						$(item).removeClass("reveal");
					}
				});
			});
			elements.forEach(function (item) {
				if ($(this).scrollTop() >= $(item).offset().top - 400) {
					$(item).addClass("reveal");
				}else{
					$(item).removeClass("reveal");
				}
			});
		});



		