!function(e,t){for(var r in t)e[r]=t[r]}(window,webpackJsonp([81],{"./openedx/features/course_experience/static/course_experience/js/CourseOutline.js":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e){function n(e){if(Array.isArray(e)){for(var t=0,r=Array(e.length);t<e.length;t++)r[t]=e[t];return r}return Array.from(e)}function a(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}r.d(t,"CourseOutline",function(){return i});var o=r("./node_modules/edx-ui-toolkit/src/js/utils/constants.js"),i=(r.n(o),function t(){function r(t){var r=e(t).children(".fa-chevron-right"),n=e(document.getElementById(t.getAttribute("aria-controls")));n.slideDown(),n.removeClass("is-hidden"),r.addClass("fa-rotate-90"),t.setAttribute("aria-expanded","true")}function i(t){var r=e(t).children(".fa-chevron-right"),n=e(document.getElementById(t.getAttribute("aria-controls")));n.slideUp(),n.addClass("is-hidden"),r.removeClass("fa-rotate-90"),t.setAttribute("aria-expanded","false")}a(this,t);var c=[].concat(n(document.querySelectorAll(".outline-item.focusable")));c.forEach(function(e){return e.addEventListener("keydown",function(e){var t=c.indexOf(e.target);switch(e.key){case o.keys.down:e.preventDefault(),c[Math.min(t+1,c.length-1)].focus();break;case o.keys.up:e.preventDefault(),c[Math.max(t-1,0)].focus()}})}),[].concat(n(document.querySelectorAll('a:not([href^="#"])'))).forEach(function(e){return e.addEventListener("click",function(e){Logger.log("edx.ui.lms.link_clicked",{current_url:window.location.href,target_url:e.currentTarget.href})})}),[].concat(n(document.querySelectorAll(".accordion"))).forEach(function(e){Array.prototype.slice.call(e.querySelectorAll(".accordion-trigger")).forEach(function(e){return e.addEventListener("click",function(e){var t=e.currentTarget;if(t.classList.contains("accordion-trigger")){var n="true"===t.getAttribute("aria-expanded");n?n&&i(t):r(t),e.stopImmediatePropagation()}})})});var l=document.querySelector("#expand-collapse-outline-all-button"),u=document.querySelector("#expand-collapse-outline-all-span");l.addEventListener("click",function(e){var t="true"===l.getAttribute("aria-expanded"),n=void 0;t?(l.setAttribute("aria-expanded","false"),n=i,u.classList.add("expand-collapse-outline-all-extra-padding"),u.innerText="Expand All"):(l.setAttribute("aria-expanded","true"),n=r,u.classList.remove("expand-collapse-outline-all-extra-padding"),u.innerText="Collapse All"),Array.prototype.slice.call(document.querySelectorAll(".accordion-trigger")).forEach(function(e){n(e)}),e.stopImmediatePropagation()})})}.call(t,r(0))},0:function(e,t){!function(){e.exports=window.jQuery}()}},["./openedx/features/course_experience/static/course_experience/js/CourseOutline.js"]));