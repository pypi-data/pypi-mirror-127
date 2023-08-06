(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("react"));
	else if(typeof define === 'function' && define.amd)
		define(["react"], factory);
	else if(typeof exports === 'object')
		exports["dazzler_extra"] = factory(require("react"));
	else
		root["dazzler_extra"] = factory(root["React"]);
})(self, function(__WEBPACK_EXTERNAL_MODULE_react__) {
return (self["webpackChunkdazzler_name_"] = self["webpackChunkdazzler_name_"] || []).push([["extra"],{

/***/ "./src/extra/scss/index.scss":
/*!***********************************!*\
  !*** ./src/extra/scss/index.scss ***!
  \***********************************/
/***/ (() => {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "./node_modules/react-colorful/dist/index.module.js":
/*!**********************************************************!*\
  !*** ./node_modules/react-colorful/dist/index.module.js ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "HexColorInput": () => (/* binding */ Me),
/* harmony export */   "HexColorPicker": () => (/* binding */ G),
/* harmony export */   "HslColorPicker": () => (/* binding */ re),
/* harmony export */   "HslStringColorPicker": () => (/* binding */ oe),
/* harmony export */   "HslaColorPicker": () => (/* binding */ V),
/* harmony export */   "HslaStringColorPicker": () => (/* binding */ Z),
/* harmony export */   "HsvColorPicker": () => (/* binding */ ie),
/* harmony export */   "HsvStringColorPicker": () => (/* binding */ fe),
/* harmony export */   "HsvaColorPicker": () => (/* binding */ ae),
/* harmony export */   "HsvaStringColorPicker": () => (/* binding */ ue),
/* harmony export */   "RgbColorPicker": () => (/* binding */ pe),
/* harmony export */   "RgbStringColorPicker": () => (/* binding */ _e),
/* harmony export */   "RgbaColorPicker": () => (/* binding */ de),
/* harmony export */   "RgbaStringColorPicker": () => (/* binding */ me),
/* harmony export */   "setNonce": () => (/* binding */ X)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
function l(){return(l=Object.assign||function(e){for(var r=1;r<arguments.length;r++){var t=arguments[r];for(var o in t)Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o])}return e}).apply(this,arguments)}function u(e,r){if(null==e)return{};var t,o,n={},a=Object.keys(e);for(o=0;o<a.length;o++)r.indexOf(t=a[o])>=0||(n[t]=e[t]);return n}var c="undefined"!=typeof window?react__WEBPACK_IMPORTED_MODULE_0__.useLayoutEffect:react__WEBPACK_IMPORTED_MODULE_0__.useEffect;function i(e){var r=(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(e);return (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){r.current=e}),(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){return r.current&&r.current(e)},[])}var s,f=function(e,r,t){return void 0===r&&(r=0),void 0===t&&(t=1),e>t?t:e<r?r:e},v=function(e){return"touches"in e},d=function(e,r){var t=e.getBoundingClientRect(),o=v(r)?r.touches[0]:r;return{left:f((o.pageX-(t.left+window.pageXOffset))/t.width),top:f((o.pageY-(t.top+window.pageYOffset))/t.height)}},h=function(e){!v(e)&&e.preventDefault()},m=react__WEBPACK_IMPORTED_MODULE_0___default().memo(function(r){var t=r.onMove,s=r.onKey,f=u(r,["onMove","onKey"]),m=(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(null),g=(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(!1),p=(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(!1),b=p[0],_=p[1],C=i(t),x=i(s),E=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){h(e),(v(e)?e.touches.length>0:e.buttons>0)&&m.current?C(d(m.current,e)):_(!1)},[C]),H=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){var r,t=e.nativeEvent,o=m.current;h(t),r=t,g.current&&!v(r)||(g.current||(g.current=v(r)),0)||!o||(o.focus(),C(d(o,t)),_(!0))},[C]),M=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){var r=e.which||e.keyCode;r<37||r>40||(e.preventDefault(),x({left:39===r?.05:37===r?-.05:0,top:40===r?.05:38===r?-.05:0}))},[x]),N=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(){return _(!1)},[]),w=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){var r=e?window.addEventListener:window.removeEventListener;r(g.current?"touchmove":"mousemove",E),r(g.current?"touchend":"mouseup",N)},[E,N]);return c(function(){return w(b),function(){b&&w(!1)}},[b,w]),react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",l({},f,{className:"react-colorful__interactive",ref:m,onTouchStart:H,onMouseDown:H,onKeyDown:M,tabIndex:0,role:"slider"}))}),g=function(e){return e.filter(Boolean).join(" ")},p=function(r){var t=r.color,o=r.left,n=r.top,a=void 0===n?.5:n,l=g(["react-colorful__pointer",r.className]);return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:l,style:{top:100*a+"%",left:100*o+"%"}},react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:"react-colorful__pointer-fill",style:{backgroundColor:t}}))},b=function(e,r,t){return void 0===r&&(r=0),void 0===t&&(t=Math.pow(10,r)),Math.round(t*e)/t},_={grad:.9,turn:360,rad:360/(2*Math.PI)},C=function(e){return"#"===e[0]&&(e=e.substr(1)),e.length<6?{r:parseInt(e[0]+e[0],16),g:parseInt(e[1]+e[1],16),b:parseInt(e[2]+e[2],16),a:1}:{r:parseInt(e.substr(0,2),16),g:parseInt(e.substr(2,2),16),b:parseInt(e.substr(4,2),16),a:1}},x=function(e,r){return void 0===r&&(r="deg"),Number(e)*(_[r]||1)},E=function(e){var r=/hsla?\(?\s*(-?\d*\.?\d+)(deg|rad|grad|turn)?[,\s]+(-?\d*\.?\d+)%?[,\s]+(-?\d*\.?\d+)%?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?M({h:x(r[1],r[2]),s:Number(r[3]),l:Number(r[4]),a:void 0===r[5]?1:Number(r[5])/(r[6]?100:1)}):{h:0,s:0,v:0,a:1}},H=E,M=function(e){var r=e.s,t=e.l;return{h:e.h,s:(r*=(t<50?t:100-t)/100)>0?2*r/(t+r)*100:0,v:t+r,a:e.a}},N=function(e){var r=e.s,t=e.v,o=e.a,n=(200-r)*t/100;return{h:b(e.h),s:b(n>0&&n<200?r*t/100/(n<=100?n:200-n)*100:0),l:b(n/2),a:b(o,2)}},w=function(e){var r=N(e);return"hsl("+r.h+", "+r.s+"%, "+r.l+"%)"},y=function(e){var r=N(e);return"hsla("+r.h+", "+r.s+"%, "+r.l+"%, "+r.a+")"},q=function(e){var r=e.h,t=e.s,o=e.v,n=e.a;r=r/360*6,t/=100,o/=100;var a=Math.floor(r),l=o*(1-t),u=o*(1-(r-a)*t),c=o*(1-(1-r+a)*t),i=a%6;return{r:b(255*[o,u,l,l,c,o][i]),g:b(255*[c,o,o,u,l,l][i]),b:b(255*[l,l,c,o,o,u][i]),a:b(n,2)}},k=function(e){var r=/hsva?\(?\s*(-?\d*\.?\d+)(deg|rad|grad|turn)?[,\s]+(-?\d*\.?\d+)%?[,\s]+(-?\d*\.?\d+)%?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?K({h:x(r[1],r[2]),s:Number(r[3]),v:Number(r[4]),a:void 0===r[5]?1:Number(r[5])/(r[6]?100:1)}):{h:0,s:0,v:0,a:1}},O=k,I=function(e){var r=/rgba?\(?\s*(-?\d*\.?\d+)(%)?[,\s]+(-?\d*\.?\d+)(%)?[,\s]+(-?\d*\.?\d+)(%)?,?\s*[/\s]*(-?\d*\.?\d+)?(%)?\s*\)?/i.exec(e);return r?B({r:Number(r[1])/(r[2]?100/255:1),g:Number(r[3])/(r[4]?100/255:1),b:Number(r[5])/(r[6]?100/255:1),a:void 0===r[7]?1:Number(r[7])/(r[8]?100:1)}):{h:0,s:0,v:0,a:1}},j=I,z=function(e){var r=e.toString(16);return r.length<2?"0"+r:r},B=function(e){var r=e.r,t=e.g,o=e.b,n=e.a,a=Math.max(r,t,o),l=a-Math.min(r,t,o),u=l?a===r?(t-o)/l:a===t?2+(o-r)/l:4+(r-t)/l:0;return{h:b(60*(u<0?u+6:u)),s:b(a?l/a*100:0),v:b(a/255*100),a:n}},K=function(e){return{h:b(e.h),s:b(e.s),v:b(e.v),a:b(e.a,2)}},A=react__WEBPACK_IMPORTED_MODULE_0___default().memo(function(r){var t=r.hue,o=r.onChange,n=g(["react-colorful__hue",r.className]);return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:n},react__WEBPACK_IMPORTED_MODULE_0___default().createElement(m,{onMove:function(e){o({h:360*e.left})},onKey:function(e){o({h:f(t+360*e.left,0,360)})},"aria-label":"Hue","aria-valuetext":b(t)},react__WEBPACK_IMPORTED_MODULE_0___default().createElement(p,{className:"react-colorful__hue-pointer",left:t/360,color:w({h:t,s:100,v:100,a:1})})))}),L=react__WEBPACK_IMPORTED_MODULE_0___default().memo(function(r){var t=r.hsva,o=r.onChange,n={backgroundColor:w({h:t.h,s:100,v:100,a:1})};return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:"react-colorful__saturation",style:n},react__WEBPACK_IMPORTED_MODULE_0___default().createElement(m,{onMove:function(e){o({s:100*e.left,v:100-100*e.top})},onKey:function(e){o({s:f(t.s+100*e.left,0,100),v:f(t.v-100*e.top,0,100)})},"aria-label":"Color","aria-valuetext":"Saturation "+b(t.s)+"%, Brightness "+b(t.v)+"%"},react__WEBPACK_IMPORTED_MODULE_0___default().createElement(p,{className:"react-colorful__saturation-pointer",top:1-t.v/100,left:t.s/100,color:w(t)})))}),D=function(e,r){if(e===r)return!0;for(var t in e)if(e[t]!==r[t])return!1;return!0},F=function(e,r){return e.replace(/\s/g,"")===r.replace(/\s/g,"")};function S(e,r,l){var u=i(l),c=(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(function(){return e.toHsva(r)}),s=c[0],f=c[1],v=(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)({color:r,hsva:s});(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){if(!e.equal(r,v.current.color)){var t=e.toHsva(r);v.current={hsva:t,color:r},f(t)}},[r,e]),(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){var r;D(s,v.current.hsva)||e.equal(r=e.fromHsva(s),v.current.color)||(v.current={hsva:s,color:r},u(r))},[s,e,u]);var d=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){f(function(r){return Object.assign({},r,e)})},[]);return[s,d]}var P,T=function(){return s||( true?__webpack_require__.nc:0)},X=function(e){s=e},Y=function(){c(function(){if("undefined"!=typeof document&&!P){(P=document.createElement("style")).innerHTML='.react-colorful{position:relative;display:flex;flex-direction:column;width:200px;height:200px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default}.react-colorful__saturation{position:relative;flex-grow:1;border-color:transparent;border-bottom:12px solid #000;border-radius:8px 8px 0 0;background-image:linear-gradient(0deg,#000,transparent),linear-gradient(90deg,#fff,hsla(0,0%,100%,0))}.react-colorful__alpha-gradient,.react-colorful__pointer-fill{content:"";position:absolute;left:0;top:0;right:0;bottom:0;pointer-events:none;border-radius:inherit}.react-colorful__alpha-gradient,.react-colorful__saturation{box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}.react-colorful__alpha,.react-colorful__hue{position:relative;height:24px}.react-colorful__hue{background:linear-gradient(90deg,red 0,#ff0 17%,#0f0 33%,#0ff 50%,#00f 67%,#f0f 83%,red)}.react-colorful__last-control{border-radius:0 0 8px 8px}.react-colorful__interactive{position:absolute;left:0;top:0;right:0;bottom:0;border-radius:inherit;outline:none;touch-action:none}.react-colorful__pointer{position:absolute;z-index:1;box-sizing:border-box;width:28px;height:28px;transform:translate(-50%,-50%);background-color:#fff;border:2px solid #fff;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,.2)}.react-colorful__interactive:focus .react-colorful__pointer{transform:translate(-50%,-50%) scale(1.1)}.react-colorful__alpha,.react-colorful__alpha-pointer{background-color:#fff;background-image:url(\'data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill-opacity=".05"><path d="M8 0h8v8H8zM0 8h8v8H0z"/></svg>\')}.react-colorful__saturation-pointer{z-index:3}.react-colorful__hue-pointer{z-index:2}';var e=T();e&&P.setAttribute("nonce",e),document.head.appendChild(P)}},[])},$=function(r){var t=r.className,o=r.colorModel,n=r.color,a=void 0===n?o.defaultColor:n,c=r.onChange,i=u(r,["className","colorModel","color","onChange"]);Y();var s=S(o,a,c),f=s[0],v=s[1],d=g(["react-colorful",t]);return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",l({},i,{className:d}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(L,{hsva:f,onChange:v}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(A,{hue:f.h,onChange:v,className:"react-colorful__last-control"}))},R={defaultColor:"000",toHsva:function(e){return B(C(e))},fromHsva:function(e){return t=(r=q(e)).g,o=r.b,"#"+z(r.r)+z(t)+z(o);var r,t,o},equal:function(e,r){return e.toLowerCase()===r.toLowerCase()||D(C(e),C(r))}},G=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:R}))},J=function(r){var t=r.className,o=r.hsva,n=r.onChange,a={backgroundImage:"linear-gradient(90deg, "+y(Object.assign({},o,{a:0}))+", "+y(Object.assign({},o,{a:1}))+")"},l=g(["react-colorful__alpha",t]);return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:l},react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",{className:"react-colorful__alpha-gradient",style:a}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(m,{onMove:function(e){n({a:e.left})},onKey:function(e){n({a:f(o.a+e.left)})},"aria-label":"Alpha","aria-valuetext":b(100*o.a)+"%"},react__WEBPACK_IMPORTED_MODULE_0___default().createElement(p,{className:"react-colorful__alpha-pointer",left:o.a,color:y(o)})))},Q=function(r){var t=r.className,o=r.colorModel,n=r.color,a=void 0===n?o.defaultColor:n,c=r.onChange,i=u(r,["className","colorModel","color","onChange"]);Y();var s=S(o,a,c),f=s[0],v=s[1],d=g(["react-colorful",t]);return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div",l({},i,{className:d}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(L,{hsva:f,onChange:v}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(A,{hue:f.h,onChange:v}),react__WEBPACK_IMPORTED_MODULE_0___default().createElement(J,{hsva:f,onChange:v,className:"react-colorful__last-control"}))},U={defaultColor:{h:0,s:0,l:0,a:1},toHsva:M,fromHsva:N,equal:D},V=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:U}))},W={defaultColor:"hsla(0, 0%, 0%, 1)",toHsva:E,fromHsva:y,equal:F},Z=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:W}))},ee={defaultColor:{h:0,s:0,l:0},toHsva:function(e){return M({h:e.h,s:e.s,l:e.l,a:1})},fromHsva:function(e){return{h:(r=N(e)).h,s:r.s,l:r.l};var r},equal:D},re=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:ee}))},te={defaultColor:"hsl(0, 0%, 0%)",toHsva:H,fromHsva:w,equal:F},oe=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:te}))},ne={defaultColor:{h:0,s:0,v:0,a:1},toHsva:function(e){return e},fromHsva:K,equal:D},ae=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:ne}))},le={defaultColor:"hsva(0, 0%, 0%, 1)",toHsva:k,fromHsva:function(e){var r=K(e);return"hsva("+r.h+", "+r.s+"%, "+r.v+"%, "+r.a+")"},equal:F},ue=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:le}))},ce={defaultColor:{h:0,s:0,v:0},toHsva:function(e){return{h:e.h,s:e.s,v:e.v,a:1}},fromHsva:function(e){var r=K(e);return{h:r.h,s:r.s,v:r.v}},equal:D},ie=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:ce}))},se={defaultColor:"hsv(0, 0%, 0%)",toHsva:O,fromHsva:function(e){var r=K(e);return"hsv("+r.h+", "+r.s+"%, "+r.v+"%)"},equal:F},fe=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:se}))},ve={defaultColor:{r:0,g:0,b:0,a:1},toHsva:B,fromHsva:q,equal:D},de=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:ve}))},he={defaultColor:"rgba(0, 0, 0, 1)",toHsva:I,fromHsva:function(e){var r=q(e);return"rgba("+r.r+", "+r.g+", "+r.b+", "+r.a+")"},equal:F},me=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Q,l({},r,{colorModel:he}))},ge={defaultColor:{r:0,g:0,b:0},toHsva:function(e){return B({r:e.r,g:e.g,b:e.b,a:1})},fromHsva:function(e){return{r:(r=q(e)).r,g:r.g,b:r.b};var r},equal:D},pe=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:ge}))},be={defaultColor:"rgb(0, 0, 0)",toHsva:j,fromHsva:function(e){var r=q(e);return"rgb("+r.r+", "+r.g+", "+r.b+")"},equal:F},_e=function(r){return react__WEBPACK_IMPORTED_MODULE_0___default().createElement($,l({},r,{colorModel:be}))},Ce=/^#?[0-9A-F]{3}$/i,xe=/^#?[0-9A-F]{6}$/i,Ee=function(e){return xe.test(e)||Ce.test(e)},He=function(e){return e.replace(/([^0-9A-F]+)/gi,"").substr(0,6)},Me=function(r){var n=r.color,c=void 0===n?"":n,s=r.onChange,f=r.onBlur,v=r.prefixed,d=u(r,["color","onChange","onBlur","prefixed"]),h=(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(function(){return He(c)}),m=h[0],g=h[1],p=i(s),b=i(f),_=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){var r=He(e.target.value);g(r),Ee(r)&&p("#"+r)},[p]),C=(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(function(e){Ee(e.target.value)||g(He(c)),b(e)},[c,b]);return (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){g(He(c))},[c]),react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input",l({},d,{value:(v?"#":"")+m,spellCheck:"false",onChange:_,onBlur:C}))};
//# sourceMappingURL=index.module.js.map


/***/ }),

/***/ "./src/extra/js/components/ColorPicker.tsx":
/*!*************************************************!*\
  !*** ./src/extra/js/components/ColorPicker.tsx ***!
  \*************************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var react_colorful_1 = __webpack_require__(/*! react-colorful */ "./node_modules/react-colorful/dist/index.module.js");
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
/**
 * A color picker powered by react-colorful
 *
 * A toggle button is included or can be disabled with ``toggleable=False``
 * and then it be activated by binding, tie or initial value.
 *
 * Common style aspects goes on the container of the picker, hidden by default.
 *
 * :CSS:
 *
 *      - ``dazzler-extra-color-picker`` - Top level container
 *      - ``dazzler-color-picker-toggle`` - Toggle button
 *      - ``dazzler-color-picker`` - Picker container.
 *
 * .. literalinclude:: ../../tests/components/pages/color_picker.py
 */
var ColorPicker = function (props) {
    var identity = props.identity, class_name = props.class_name, style = props.style, type = props.type, toggleable = props.toggleable, toggle_button = props.toggle_button, toggle_on_choose = props.toggle_on_choose, toggle_on_choose_delay = props.toggle_on_choose_delay, toggle_button_color = props.toggle_button_color, toggle_direction = props.toggle_direction, active = props.active, value = props.value, updateAspects = props.updateAspects, as_string = props.as_string, rest = __rest(props, ["identity", "class_name", "style", "type", "toggleable", "toggle_button", "toggle_on_choose", "toggle_on_choose_delay", "toggle_button_color", "toggle_direction", "active", "value", "updateAspects", "as_string"]);
    var css = react_1.useMemo(function () {
        return commons_1.getPresetsClassNames(rest, 'dazzler-color-picker', "toggle-direction-" + toggle_direction);
    }, [rest, active]);
    var className = react_1.useMemo(function () {
        var c = [class_name];
        if (active) {
            c.push('active');
        }
        return c.join(' ');
    }, [class_name, active]);
    var styling = react_1.useMemo(function () { return commons_1.getCommonStyles(rest, style); }, [rest, style]);
    var autoClose = react_1.useCallback(commons_1.throttle(function () { return updateAspects({ active: false }); }, toggle_on_choose_delay, true), []);
    var picker = react_1.useMemo(function () {
        var onChange = function (newColor) {
            var payload = { value: newColor };
            if (toggle_on_choose) {
                autoClose();
            }
            updateAspects(payload);
        };
        switch (type) {
            case 'rgb':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.RgbStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.RgbColorPicker, { onChange: onChange, color: value }));
            case 'rgba':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.RgbaStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.RgbaColorPicker, { onChange: onChange, color: value }));
            case 'hsl':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.HslStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.HslColorPicker, { onChange: onChange, color: value }));
            case 'hsla':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.HslaStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.HslaColorPicker, { onChange: onChange, color: value }));
            case 'hsv':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.HsvStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.HsvColorPicker, { onChange: onChange, color: value }));
            case 'hsva':
                if (as_string) {
                    return (react_1["default"].createElement(react_colorful_1.HsvaStringColorPicker, { onChange: onChange, color: value }));
                }
                return (react_1["default"].createElement(react_colorful_1.HsvaColorPicker, { onChange: onChange, color: value }));
            case 'hex':
            default:
                return (react_1["default"].createElement(react_colorful_1.HexColorPicker, { onChange: onChange, color: value }));
        }
    }, [
        type,
        value,
        updateAspects,
        toggle_on_choose,
        toggle_on_choose_delay,
        as_string,
    ]);
    var toggleButton = react_1.useMemo(function () {
        if (toggle_button_color) {
            return (react_1["default"].createElement("div", { className: "toggle-button-color", 
                // @ts-ignore
                style: { backgroundColor: value } }));
        }
        return toggle_button;
    }, [toggle_button, toggle_button_color, value]);
    var onToggle = react_1.useCallback(function () {
        updateAspects({ active: !active });
    }, [active, updateAspects]);
    return (react_1["default"].createElement("div", { id: identity, className: className },
        toggleable && (react_1["default"].createElement("div", { className: "dazzler-color-picker-toggle", onClick: onToggle }, toggleButton)),
        react_1["default"].createElement("div", { className: css, style: styling }, picker)));
};
ColorPicker.defaultProps = {
    type: 'hex',
    toggle_button: '🎨',
    toggleable: true,
    toggle_on_choose: true,
    toggle_on_choose_delay: 2500,
    toggle_direction: 'top-left',
};
exports.default = ColorPicker;


/***/ }),

/***/ "./src/extra/js/components/Drawer.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Drawer.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var Caret = function (_a) {
    var side = _a.side, opened = _a.opened;
    switch (side) {
        case 'top':
            return opened ? react_1["default"].createElement("span", null, "\u25B2") : react_1["default"].createElement("span", null, "\u25BC");
        case 'right':
            return opened ? react_1["default"].createElement("span", null, "\u25B8") : react_1["default"].createElement("span", null, "\u25C2");
        case 'left':
            return opened ? react_1["default"].createElement("span", null, "\u25C2") : react_1["default"].createElement("span", null, "\u25B8");
        case 'bottom':
            return opened ? react_1["default"].createElement("span", null, "\u25BC") : react_1["default"].createElement("span", null, "\u25B2");
        default:
            return null;
    }
};
/**
 * Draw content from the sides of the screen.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-drawer``
 *     - ``drawer-content``
 *     - ``drawer-control``
 *     - ``vertical``
 *     - ``horizontal``
 *     - ``right``
 *     - ``bottom``
 */
var Drawer = function (props) {
    var class_name = props.class_name, identity = props.identity, style = props.style, children = props.children, opened = props.opened, side = props.side, updateAspects = props.updateAspects;
    var css = [side];
    if (side === 'top' || side === 'bottom') {
        css.push('horizontal');
    }
    else {
        css.push('vertical');
    }
    return (react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, [class_name])), id: identity, style: style },
        opened && (react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, ['drawer-content'])) }, children)),
        react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, ['drawer-control'])), onClick: function () { return updateAspects({ opened: !opened }); } },
            react_1["default"].createElement(Caret, { opened: opened, side: side }))));
};
Drawer.defaultProps = {
    side: 'top',
};
exports.default = Drawer;


/***/ }),

/***/ "./src/extra/js/components/Notice.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Notice.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * Browser notifications with permissions handling.
 */
var Notice = /** @class */ (function (_super) {
    __extends(Notice, _super);
    function Notice(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            lastMessage: props.body,
            notification: null,
        };
        _this.onPermission = _this.onPermission.bind(_this);
        return _this;
    }
    Notice.prototype.componentDidMount = function () {
        var updateAspects = this.props.updateAspects;
        if (!('Notification' in window) && updateAspects) {
            updateAspects({ permission: 'unsupported' });
        }
        else if (Notification.permission === 'default') {
            Notification.requestPermission().then(this.onPermission);
        }
        else {
            this.onPermission(window.Notification.permission);
        }
    };
    Notice.prototype.componentDidUpdate = function (prevProps) {
        if (!prevProps.displayed && this.props.displayed) {
            this.sendNotification(this.props.permission);
        }
    };
    Notice.prototype.sendNotification = function (permission) {
        var _this = this;
        var _a = this.props, updateAspects = _a.updateAspects, body = _a.body, title = _a.title, icon = _a.icon, require_interaction = _a.require_interaction, lang = _a.lang, badge = _a.badge, tag = _a.tag, image = _a.image, vibrate = _a.vibrate;
        if (permission === 'granted') {
            var options = {
                requireInteraction: require_interaction,
                body: body,
                icon: icon,
                lang: lang,
                badge: badge,
                tag: tag,
                image: image,
                vibrate: vibrate,
            };
            var notification = new Notification(title, options);
            notification.onclick = function () {
                if (updateAspects) {
                    updateAspects(ramda_1.merge({ displayed: false }, commons_1.timestampProp('clicks', _this.props.clicks + 1)));
                }
            };
            notification.onclose = function () {
                if (updateAspects) {
                    updateAspects(ramda_1.merge({ displayed: false }, commons_1.timestampProp('closes', _this.props.closes + 1)));
                }
            };
        }
    };
    Notice.prototype.onPermission = function (permission) {
        var _a = this.props, displayed = _a.displayed, updateAspects = _a.updateAspects;
        if (updateAspects) {
            updateAspects({ permission: permission });
        }
        if (displayed) {
            this.sendNotification(permission);
        }
    };
    Notice.prototype.render = function () {
        return null;
    };
    return Notice;
}(react_1["default"].Component));
exports.default = Notice;


/***/ }),

/***/ "./src/extra/js/components/PageMap.tsx":
/*!*********************************************!*\
  !*** ./src/extra/js/components/PageMap.tsx ***!
  \*********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
/**
 * List of links to other page in the app.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-page-map``
 */
var PageMap = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity;
    var _a = react_1.useState(null), pageMap = _a[0], setPageMap = _a[1];
    react_1.useEffect(function () {
        // @ts-ignore
        fetch(window.dazzler_base_url + "/dazzler/page-map").then(function (rep) {
            return rep.json().then(setPageMap);
        });
    }, []);
    return (react_1["default"].createElement("ul", { className: class_name, style: style, id: identity }, pageMap &&
        pageMap.map(function (page) { return (react_1["default"].createElement("li", { key: page.name },
            react_1["default"].createElement("a", { href: page.url }, page.title))); })));
};
PageMap.defaultProps = {};
exports.default = PageMap;


/***/ }),

/***/ "./src/extra/js/components/Pager.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/Pager.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var startOffset = function (page, itemPerPage) {
    return (page - 1) * (page > 1 ? itemPerPage : 0);
};
var endOffset = function (start, itemPerPage, page, total, leftOver) {
    return page !== total
        ? start + itemPerPage
        : leftOver !== 0
            ? start + leftOver
            : start + itemPerPage;
};
var showList = function (page, total, n) {
    if (total > n) {
        var middle = Math.floor(n / 2);
        var first = page >= total - middle
            ? total - n + 1
            : page > middle
                ? page - middle
                : 1;
        var last = page < total - middle ? first + n : total + 1;
        return ramda_1.range(first, last);
    }
    return ramda_1.range(1, total + 1);
};
var Page = react_1.memo(function (_a) {
    var style = _a.style, class_name = _a.class_name, on_change = _a.on_change, text = _a.text, page = _a.page, current = _a.current;
    return (react_1["default"].createElement("span", { style: style, className: "" + class_name + (current ? ' current-page' : ''), onClick: function () { return !current && on_change(page); } }, text || page));
});
/**
 * Paging for dazzler apps.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-pager``
 *     - ``page``
 */
var Pager = /** @class */ (function (_super) {
    __extends(Pager, _super);
    function Pager(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            current_page: null,
            start_offset: null,
            end_offset: null,
            pages: [],
            total_pages: Math.ceil(props.total_items / props.items_per_page),
        };
        _this.onChangePage = _this.onChangePage.bind(_this);
        return _this;
    }
    Pager.prototype.UNSAFE_componentWillMount = function () {
        this.onChangePage(this.props.current_page);
    };
    Pager.prototype.onChangePage = function (page) {
        var _a = this.props, items_per_page = _a.items_per_page, total_items = _a.total_items, updateAspects = _a.updateAspects, pages_displayed = _a.pages_displayed;
        var total_pages = this.state.total_pages;
        var start_offset = startOffset(page, items_per_page);
        var leftOver = total_items % items_per_page;
        var end_offset = endOffset(start_offset, items_per_page, page, total_pages, leftOver);
        var payload = {
            current_page: page,
            start_offset: start_offset,
            end_offset: end_offset,
            pages: showList(page, total_pages, pages_displayed),
        };
        this.setState(payload);
        if (updateAspects) {
            if (this.state.total_pages !== this.props.total_pages) {
                payload.total_pages = this.state.total_pages;
            }
            updateAspects(payload);
        }
    };
    Pager.prototype.UNSAFE_componentWillReceiveProps = function (props) {
        if (props.current_page !== this.state.current_page) {
            this.onChangePage(props.current_page);
        }
        if (props.total_items !== this.props.total_items) {
            var total_pages = Math.ceil(props.total_items / props.items_per_page);
            this.setState({
                total_pages: total_pages,
                pages: showList(props.current_page, total_pages, props.pages_displayed),
            });
        }
    };
    Pager.prototype.render = function () {
        var _this = this;
        var _a = this.state, current_page = _a.current_page, pages = _a.pages, total_pages = _a.total_pages;
        var _b = this.props, class_name = _b.class_name, identity = _b.identity, page_style = _b.page_style, page_class_name = _b.page_class_name, pages_displayed = _b.pages_displayed, next_label = _b.next_label, previous_label = _b.previous_label;
        var css = ['page'];
        if (page_class_name) {
            css.push(page_class_name);
        }
        var pageCss = ramda_1.join(' ', css);
        return (react_1["default"].createElement("div", { className: class_name, id: identity },
            current_page > 1 && (react_1["default"].createElement(Page, { page: current_page - 1, text: previous_label, style: page_style, class_name: pageCss, on_change: this.onChangePage })),
            current_page + 1 >= pages_displayed &&
                total_pages > pages_displayed && (react_1["default"].createElement(react_1["default"].Fragment, null,
                react_1["default"].createElement(Page, { page: 1, text: '1', style: page_style, class_name: pageCss, on_change: this.onChangePage }),
                react_1["default"].createElement(Page, { page: -1, text: '...', on_change: function () { return null; }, class_name: pageCss + " more-pages" }))),
            pages.map(function (e) { return (react_1["default"].createElement(Page, { page: e, key: "page-" + e, style: page_style, class_name: pageCss, on_change: _this.onChangePage, current: e === current_page })); }),
            total_pages - current_page >= Math.ceil(pages_displayed / 2) &&
                total_pages > pages_displayed && (react_1["default"].createElement(react_1["default"].Fragment, null,
                react_1["default"].createElement(Page, { page: -1, text: '...', class_name: pageCss + " more-pages", on_change: function () { return null; } }),
                react_1["default"].createElement(Page, { page: total_pages, style: page_style, class_name: pageCss, on_change: this.onChangePage }))),
            current_page < total_pages && (react_1["default"].createElement(Page, { page: current_page + 1, text: next_label, style: page_style, class_name: pageCss, on_change: this.onChangePage }))));
    };
    Pager.defaultProps = {
        current_page: 1,
        items_per_page: 10,
        pages_displayed: 10,
        next_label: 'next',
        previous_label: 'previous',
    };
    return Pager;
}(react_1["default"].Component));
exports.default = Pager;


/***/ }),

/***/ "./src/extra/js/components/PopUp.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/PopUp.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
function getMouseX(e, popup) {
    return (e.clientX -
        e.target.getBoundingClientRect().left -
        popup.getBoundingClientRect().width / 2);
}
/**
 * Wraps a component/text to render a popup when hovering
 * over the children or clicking on it.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-pop-up``
 *     - ``popup-content``
 *     - ``visible``
 */
var PopUp = /** @class */ (function (_super) {
    __extends(PopUp, _super);
    function PopUp(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            pos: null,
        };
        return _this;
    }
    PopUp.prototype.render = function () {
        var _this = this;
        var _a = this.props, class_name = _a.class_name, style = _a.style, identity = _a.identity, children = _a.children, content = _a.content, mode = _a.mode, updateAspects = _a.updateAspects, active = _a.active, content_style = _a.content_style, children_style = _a.children_style;
        return (react_1["default"].createElement("div", { className: class_name, style: style, id: identity },
            react_1["default"].createElement("div", { className: 'popup-content' + (active ? ' visible' : ''), style: __assign(__assign({}, (content_style || {})), { left: this.state.pos || 0 }), ref: function (r) { return (_this.popupRef = r); } }, content),
            react_1["default"].createElement("div", { className: "popup-children", onMouseEnter: function (e) {
                    if (mode === 'hover') {
                        _this.setState({ pos: getMouseX(e, _this.popupRef) }, function () { return updateAspects({ active: true }); });
                    }
                }, onMouseLeave: function () {
                    return mode === 'hover' && updateAspects({ active: false });
                }, onClick: function (e) {
                    if (mode === 'click') {
                        _this.setState({ pos: getMouseX(e, _this.popupRef) }, function () { return updateAspects({ active: !active }); });
                    }
                }, style: children_style }, children)));
    };
    PopUp.defaultProps = {
        mode: 'hover',
        active: false,
    };
    return PopUp;
}(react_1["default"].Component));
exports.default = PopUp;


/***/ }),

/***/ "./src/extra/js/components/Spinner.tsx":
/*!*********************************************!*\
  !*** ./src/extra/js/components/Spinner.tsx ***!
  \*********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
/**
 * Simple html/css spinner.
 */
var Spinner = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity;
    return react_1["default"].createElement("div", { id: identity, className: class_name, style: style });
};
exports.default = Spinner;


/***/ }),

/***/ "./src/extra/js/components/Sticky.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Sticky.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * A shorthand component for a sticky div.
 */
var Sticky = function (props) {
    var class_name = props.class_name, identity = props.identity, style = props.style, children = props.children, top = props.top, left = props.left, right = props.right, bottom = props.bottom;
    var styles = ramda_1.mergeAll([style, { top: top, left: left, right: right, bottom: bottom }]);
    return (react_1["default"].createElement("div", { className: class_name, id: identity, style: styles }, children));
};
exports.default = Sticky;


/***/ }),

/***/ "./src/extra/js/components/Toast.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/Toast.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * Display a message over the ui that will disappears after a delay.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-toast``
 *     - ``opened``
 *     - ``toast-inner``
 *     - ``top``
 *     - ``top-left``
 *     - ``top-right``
 *     - ``bottom``
 *     - ``bottom-left``
 *     - ``bottom-right``
 *     - ``right``
 */
var Toast = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity, message = props.message, position = props.position, opened = props.opened, delay = props.delay, updateAspects = props.updateAspects;
    var _a = react_1.useState(false), displayed = _a[0], setDisplayed = _a[1];
    var css = react_1.useMemo(function () {
        var c = [class_name, position];
        if (opened) {
            c.push('opened');
        }
        return ramda_1.join(' ', c);
    }, [class_name, opened, position]);
    react_1.useEffect(function () {
        if (opened && !displayed) {
            setTimeout(function () {
                updateAspects({ opened: false });
                setDisplayed(false);
            }, delay);
            setDisplayed(true);
        }
    }, [opened, displayed, delay]);
    return (react_1["default"].createElement("div", { className: css, style: style, id: identity }, message));
};
Toast.defaultProps = {
    delay: 3000,
    position: 'top',
    opened: true,
};
exports.default = Toast;


/***/ }),

/***/ "./src/extra/js/components/TreeView.tsx":
/*!**********************************************!*\
  !*** ./src/extra/js/components/TreeView.tsx ***!
  \**********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var TreeViewElement = function (_a) {
    var label = _a.label, onClick = _a.onClick, identifier = _a.identifier, items = _a.items, level = _a.level, selected = _a.selected, expanded_items = _a.expanded_items, nest_icon_expanded = _a.nest_icon_expanded, nest_icon_collapsed = _a.nest_icon_collapsed;
    var isSelected = react_1.useMemo(function () { return selected && ramda_1.includes(identifier, selected); }, [selected, identifier]);
    var isExpanded = react_1.useMemo(function () { return ramda_1.includes(identifier, expanded_items); }, [expanded_items, expanded_items]);
    var css = ['tree-item-label', "level-" + level];
    if (isSelected) {
        css.push('selected');
    }
    return (react_1["default"].createElement("div", { className: "tree-item level-" + level, style: { marginLeft: level + "rem" } },
        react_1["default"].createElement("div", { className: ramda_1.join(' ', css), onClick: function (e) { return onClick(e, identifier, Boolean(items)); } },
            items && (react_1["default"].createElement("span", { className: "tree-caret" }, isExpanded ? nest_icon_expanded : nest_icon_collapsed)),
            label || identifier),
        items && isExpanded && (react_1["default"].createElement("div", { className: "tree-sub-items" }, items.map(function (item) {
            return renderItem({
                parent: identifier,
                onClick: onClick,
                item: item,
                level: level + 1,
                selected: selected,
                nest_icon_expanded: nest_icon_expanded,
                nest_icon_collapsed: nest_icon_collapsed,
                expanded_items: expanded_items,
            });
        })))));
};
var renderItem = function (_a) {
    var parent = _a.parent, item = _a.item, level = _a.level, rest = __rest(_a, ["parent", "item", "level"]);
    if (ramda_1.is(String, item)) {
        return (react_1["default"].createElement(TreeViewElement, __assign({ label: item, identifier: parent ? ramda_1.join('.', [parent, item]) : item, level: level || 0, key: item }, rest)));
    }
    return (react_1["default"].createElement(TreeViewElement, __assign({}, item, { level: level || 0, key: item.identifier, identifier: parent ? ramda_1.join('.', [parent, item.identifier]) : item.identifier }, rest)));
};
/**
 * A tree of nested items.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-tree-view``
 *     - ``tree-item``
 *     - ``tree-item-label``
 *     - ``tree-sub-items``
 *     - ``tree-caret``
 *     - ``selected``
 *     - ``level-{n}``
 *
 * :example:
 *
 * .. literalinclude:: ../../tests/components/pages/treeview.py
 */
var TreeView = function (_a) {
    var class_name = _a.class_name, style = _a.style, identity = _a.identity, updateAspects = _a.updateAspects, items = _a.items, selected = _a.selected, expanded_items = _a.expanded_items, nest_icon_expanded = _a.nest_icon_expanded, nest_icon_collapsed = _a.nest_icon_collapsed;
    var onClick = function (e, identifier, expand) {
        e.stopPropagation();
        var payload = {};
        if (selected && ramda_1.includes(identifier, selected)) {
            var last = ramda_1.split('.', identifier);
            last = ramda_1.slice(0, last.length - 1, last);
            if (last.length === 0) {
                payload.selected = null;
            }
            else if (last.length === 1) {
                payload.selected = last[0];
            }
            else {
                payload.selected = ramda_1.join('.', last);
            }
        }
        else {
            payload.selected = identifier;
        }
        if (expand) {
            if (ramda_1.includes(identifier, expanded_items)) {
                payload.expanded_items = ramda_1.without([identifier], expanded_items);
            }
            else {
                payload.expanded_items = ramda_1.concat(expanded_items, [identifier]);
            }
        }
        updateAspects(payload);
    };
    return (react_1["default"].createElement("div", { className: class_name, style: style, id: identity }, items.map(function (item) {
        return renderItem({
            item: item,
            onClick: onClick,
            selected: selected,
            nest_icon_expanded: nest_icon_expanded,
            nest_icon_collapsed: nest_icon_collapsed,
            expanded_items: expanded_items,
        });
    })));
};
TreeView.defaultProps = {
    nest_icon_collapsed: '⏵',
    nest_icon_expanded: '⏷',
    expanded_items: [],
};
exports.default = TreeView;


/***/ }),

/***/ "./src/extra/js/index.ts":
/*!*******************************!*\
  !*** ./src/extra/js/index.ts ***!
  \*******************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
exports.ColorPicker = exports.PageMap = exports.Toast = exports.TreeView = exports.PopUp = exports.Drawer = exports.Sticky = exports.Spinner = exports.Pager = exports.Notice = void 0;
__webpack_require__(/*! ../scss/index.scss */ "./src/extra/scss/index.scss");
var Notice_1 = __importDefault(__webpack_require__(/*! ./components/Notice */ "./src/extra/js/components/Notice.tsx"));
exports.Notice = Notice_1["default"];
var Pager_1 = __importDefault(__webpack_require__(/*! ./components/Pager */ "./src/extra/js/components/Pager.tsx"));
exports.Pager = Pager_1["default"];
var Spinner_1 = __importDefault(__webpack_require__(/*! ./components/Spinner */ "./src/extra/js/components/Spinner.tsx"));
exports.Spinner = Spinner_1["default"];
var Sticky_1 = __importDefault(__webpack_require__(/*! ./components/Sticky */ "./src/extra/js/components/Sticky.tsx"));
exports.Sticky = Sticky_1["default"];
var Drawer_1 = __importDefault(__webpack_require__(/*! ./components/Drawer */ "./src/extra/js/components/Drawer.tsx"));
exports.Drawer = Drawer_1["default"];
var PopUp_1 = __importDefault(__webpack_require__(/*! ./components/PopUp */ "./src/extra/js/components/PopUp.tsx"));
exports.PopUp = PopUp_1["default"];
var TreeView_1 = __importDefault(__webpack_require__(/*! ./components/TreeView */ "./src/extra/js/components/TreeView.tsx"));
exports.TreeView = TreeView_1["default"];
var Toast_1 = __importDefault(__webpack_require__(/*! ./components/Toast */ "./src/extra/js/components/Toast.tsx"));
exports.Toast = Toast_1["default"];
var PageMap_1 = __importDefault(__webpack_require__(/*! ./components/PageMap */ "./src/extra/js/components/PageMap.tsx"));
exports.PageMap = PageMap_1["default"];
var ColorPicker_1 = __importDefault(__webpack_require__(/*! ./components/ColorPicker */ "./src/extra/js/components/ColorPicker.tsx"));
exports.ColorPicker = ColorPicker_1["default"];


/***/ }),

/***/ "react":
/*!****************************************************************************************************!*\
  !*** external {"commonjs":"react","commonjs2":"react","amd":"react","umd":"react","root":"React"} ***!
  \****************************************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = __WEBPACK_EXTERNAL_MODULE_react__;

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./src/extra/js/index.ts"));
/******/ return __webpack_exports__;
/******/ }
]);
});
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGF6emxlcl9leHRyYV9jNmQyNzI3MmM0ZmMyMDgwNjY2YS5qcyIsIm1hcHBpbmdzIjoiQUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0QsTzs7Ozs7Ozs7QUNWQTs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ0FxRyxhQUFhLG9DQUFvQyxZQUFZLG1CQUFtQixLQUFLLG1CQUFtQixzRUFBc0UsU0FBUyx3QkFBd0IsZ0JBQWdCLG9CQUFvQixZQUFZLGtCQUFrQixRQUFRLFdBQVcsc0NBQXNDLFNBQVMsaUNBQWlDLGtEQUFDLENBQUMsNENBQUMsQ0FBQyxjQUFjLE1BQU0sNkNBQUMsSUFBSSxPQUFPLGdEQUFDLFlBQVksWUFBWSxFQUFFLGtEQUFDLGFBQWEsK0JBQStCLEtBQUssd0JBQXdCLHlEQUF5RCxlQUFlLG9CQUFvQixpQkFBaUIsc0RBQXNELE9BQU8sNEdBQTRHLGVBQWUsMEJBQTBCLEdBQUcsaURBQU0sYUFBYSxxREFBcUQsNkNBQUMsU0FBUyw2Q0FBQyxPQUFPLCtDQUFDLG1DQUFtQyxrREFBQyxhQUFhLDhFQUE4RSxRQUFRLGtEQUFDLGFBQWEsa0NBQWtDLDRGQUE0RixRQUFRLGtEQUFDLGFBQWEseUJBQXlCLG1DQUFtQywyREFBMkQsR0FBRyxRQUFRLGtEQUFDLFlBQVksYUFBYSxPQUFPLGtEQUFDLGFBQWEsMkRBQTJELDJFQUEyRSxRQUFRLG9CQUFvQix1QkFBdUIsVUFBVSxRQUFRLDBEQUFlLFdBQVcsSUFBSSxnSEFBZ0gsR0FBRyxnQkFBZ0IsbUNBQW1DLGVBQWUsOEZBQThGLE9BQU8sMERBQWUsUUFBUSxtQkFBbUIsOEJBQThCLENBQUMsMERBQWUsUUFBUSxnREFBZ0QsbUJBQW1CLEdBQUcsbUJBQW1CLDBFQUEwRSxJQUFJLHFDQUFxQyxlQUFlLDhDQUE4QywrRUFBK0UsRUFBRSw0RkFBNEYsaUJBQWlCLGlEQUFpRCxlQUFlLDJJQUEySSxZQUFZLHlGQUF5RixHQUFHLGlCQUFp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RSxVQUFVLEVBQUUsS0FBSyxFQUFFLEtBQUssRUFBRSxFQUFFLEVBQUUsUUFBUSxJQUNqRCxLQUFLLENBQUMsR0FBRyxDQUFDLFVBQUMsSUFBSTtRQUNaLGlCQUFVLENBQUM7WUFDUCxJQUFJO1lBQ0osT0FBTztZQUNQLFFBQVE7WUFDUixrQkFBa0I7WUFDbEIsbUJBQW1CO1lBQ25CLGNBQWM7U0FDakIsQ0FBQztJQVBGLENBT0UsQ0FDTCxDQUNDLENBQ1QsQ0FBQztBQUNOLENBQUMsQ0FBQztBQUVGLFFBQVEsQ0FBQyxZQUFZLEdBQUc7SUFDcEIsbUJBQW1CLEVBQUUsR0FBRztJQUN4QixrQkFBa0IsRUFBRSxHQUFHO0lBQ3ZCLGNBQWMsRUFBRSxFQUFFO0NBQ3JCLENBQUM7QUFFRixrQkFBZSxRQUFRLENBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ3RLeEIsNkVBQTRCO0FBRTVCLHVIQUF5QztBQVlyQyxpQkFaRyxtQkFBTSxDQVlIO0FBWFYsb0hBQXVDO0FBWW5DLGdCQVpHLGtCQUFLLENBWUg7QUFYVCwwSEFBMkM7QUFZdkMsa0JBWkcsb0JBQU8sQ0FZSDtBQVhYLHVIQUF5QztBQVlyQyxpQkFaRyxtQkFBTSxDQVlIO0FBWFYsdUhBQXlDO0FBWXJDLGlCQVpHLG1CQUFNLENBWUg7QUFYVixvSEFBdUM7QUFZbkMsZ0JBWkcsa0JBQUssQ0FZSDtBQVhULDZIQUE2QztBQVl6QyxtQkFaRyxxQkFBUSxDQVlIO0FBWFosb0hBQXVDO0FBWW5DLGdCQVpHLGtCQUFLLENBWUg7QUFYVCwwSEFBMkM7QUFZdkMsa0JBWkcsb0JBQU8sQ0FZSDtBQVhYLHNJQUFtRDtBQVkvQyxzQkFaRyx3QkFBVyxDQVlIOzs7Ozs7Ozs7Ozs7QUN2QmYiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vL3dlYnBhY2svdW5pdmVyc2FsTW9kdWxlRGVmaW5pdGlvbj8iLCJ3ZWJwYWNrOi8vLy4vc3JjL2V4dHJhL3Njc3MvaW5kZXguc2Nzcy8uL3NyYy9leHRyYS9zY3NzL2luZGV4LnNjc3M/Iiwid2VicGFjazovLy8uL25vZGVfbW9kdWxlcy9yZWFjdC1jb2xvcmZ1bC9kaXN0L2luZGV4Lm1vZHVsZS5qcy8uL25vZGVfbW9kdWxlcy9yZWFjdC1jb2xvcmZ1bC9kaXN0L2luZGV4Lm1vZHVsZS5qcz8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL0NvbG9yUGlja2VyLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL0RyYXdlci50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9Ob3RpY2UudHN4PyIsIndlYnBhY2s6Ly8vLy4vc3JjL2V4dHJhL2pzL2NvbXBvbmVudHMvUGFnZU1hcC50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9QYWdlci50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9Qb3BVcC50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9TcGlubmVyLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1N0aWNreS50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9Ub2FzdC50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9UcmVlVmlldy50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvaW5kZXgudHM/Iiwid2VicGFjazovLy8vZXh0ZXJuYWwge1wiY29tbW9uanNcIjpcInJlYWN0XCIsXCJjb21tb25qczJcIjpcInJlYWN0XCIsXCJhbWRcIjpcInJlYWN0XCIsXCJ1bWRcIjpcInJlYWN0XCIsXCJyb290XCI6XCJSZWFjdFwifT8iXSwic291cmNlc0NvbnRlbnQiOlsiKGZ1bmN0aW9uIHdlYnBhY2tVbml2ZXJzYWxNb2R1bGVEZWZpbml0aW9uKHJvb3QsIGZhY3RvcnkpIHtcblx0aWYodHlwZW9mIGV4cG9ydHMgPT09ICdvYmplY3QnICYmIHR5cGVvZiBtb2R1bGUgPT09ICdvYmplY3QnKVxuXHRcdG1vZHVsZS5leHBvcnRzID0gZmFjdG9yeShyZXF1aXJlKFwicmVhY3RcIikpO1xuXHRlbHNlIGlmKHR5cGVvZiBkZWZpbmUgPT09ICdmdW5jdGlvbicgJiYgZGVmaW5lLmFtZClcblx0XHRkZWZpbmUoW1wicmVhY3RcIl0sIGZhY3RvcnkpO1xuXHRlbHNlIGlmKHR5cGVvZiBleHBvcnRzID09PSAnb2JqZWN0Jylcblx0XHRleHBvcnRzW1wiZGF6emxlcl9leHRyYVwiXSA9IGZhY3RvcnkocmVxdWlyZShcInJlYWN0XCIpKTtcblx0ZWxzZVxuXHRcdHJvb3RbXCJkYXp6bGVyX2V4dHJhXCJdID0gZmFjdG9yeShyb290W1wiUmVhY3RcIl0pO1xufSkoc2VsZiwgZnVuY3Rpb24oX19XRUJQQUNLX0VYVEVSTkFMX01PRFVMRV9yZWFjdF9fKSB7XG5yZXR1cm4gIiwiLy8gZXh0cmFjdGVkIGJ5IG1pbmktY3NzLWV4dHJhY3QtcGx1Z2luIiwiaW1wb3J0IGUse3VzZUxheW91dEVmZmVjdCBhcyByLHVzZUVmZmVjdCBhcyB0LHVzZUNhbGxiYWNrIGFzIG8sdXNlUmVmIGFzIG4sdXNlU3RhdGUgYXMgYX1mcm9tXCJyZWFjdFwiO2Z1bmN0aW9uIGwoKXtyZXR1cm4obD1PYmplY3QuYXNzaWdufHxmdW5jdGlvbihlKXtmb3IodmFyIHI9MTtyPGFyZ3VtZW50cy5sZW5ndGg7cisrKXt2YXIgdD1hcmd1bWVudHNbcl07Zm9yKHZhciBvIGluIHQpT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKHQsbykmJihlW29dPXRbb10pfXJldHVybiBlfSkuYXBwbHkodGhpcyxhcmd1bWVudHMpfWZ1bmN0aW9uIHUoZSxyKXtpZihudWxsPT1lKXJldHVybnt9O3ZhciB0LG8sbj17fSxhPU9iamVjdC5rZXlzKGUpO2ZvcihvPTA7bzxhLmxlbmd0aDtvKyspci5pbmRleE9mKHQ9YVtvXSk+PTB8fChuW3RdPWVbdF0pO3JldHVybiBufXZhciBjPVwidW5kZWZpbmVkXCIhPXR5cGVvZiB3aW5kb3c/cjp0O2Z1bmN0aW9uIGkoZSl7dmFyIHI9bihlKTtyZXR1cm4gdChmdW5jdGlvbigpe3IuY3VycmVudD1lfSksbyhmdW5jdGlvbihlKXtyZXR1cm4gci5jdXJyZW50JiZyLmN1cnJlbnQoZSl9LFtdKX12YXIgcyxmPWZ1bmN0aW9uKGUscix0KXtyZXR1cm4gdm9pZCAwPT09ciYmKHI9MCksdm9pZCAwPT09dCYmKHQ9MSksZT50P3Q6ZTxyP3I6ZX0sdj1mdW5jdGlvbihlKXtyZXR1cm5cInRvdWNoZXNcImluIGV9LGQ9ZnVuY3Rpb24oZSxyKXt2YXIgdD1lLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLG89dihyKT9yLnRvdWNoZXNbMF06cjtyZXR1cm57bGVmdDpmKChvLnBhZ2VYLSh0LmxlZnQrd2luZG93LnBhZ2VYT2Zmc2V0KSkvdC53aWR0aCksdG9wOmYoKG8ucGFnZVktKHQudG9wK3dpbmRvdy5wYWdlWU9mZnNldCkpL3QuaGVpZ2h0KX19LGg9ZnVuY3Rpb24oZSl7IXYoZSkmJmUucHJldmVudERlZmF1bHQoKX0sbT1lLm1lbW8oZnVuY3Rpb24ocil7dmFyIHQ9ci5vbk1vdmUscz1yLm9uS2V5LGY9dShyLFtcIm9uTW92ZVwiLFwib25LZXlcIl0pLG09bihudWxsKSxnPW4oITEpLHA9YSghMSksYj1wWzBdLF89cFsxXSxDPWkodCkseD1pKHMpLEU9byhmdW5jdGlvbihlKXtoKGUpLCh2KGUpP2UudG91Y2hlcy5sZW5ndGg+MDplLmJ1dHRvbnM+MCkmJm0uY3VycmVudD9DKGQobS5jdXJyZW50LGUpKTpfKCExKX0sW0NdKSxIPW8oZnVuY3Rpb24oZSl7dmFyIHIsdD1lLm5hdGl2ZUV2ZW50LG89bS5jdXJyZW50O2godCkscj10LGcuY3VycmVudCYmIXYocil8fChnLmN1cnJlbnR8fChnLmN1cnJlbnQ9dihyKSksMCl8fCFvfHwoby5mb2N1cygpLEMoZChvLHQpKSxfKCEwKSl9LFtDXSksTT1vKGZ1bmN0aW9uKGUpe3ZhciByPWUud2hpY2h8fGUua2V5Q29kZTtyPDM3fHxyPjQwfHwoZS5wcmV2ZW50RGVmYXVsdCgpLHgoe2xlZnQ6Mzk9PT1yPy4wNTozNz09PXI/LS4wNTowLHRvcDo0MD09PXI/LjA1OjM4PT09cj8tLjA1OjB9KSl9LFt4XSksTj1vKGZ1bmN0aW9uKCl7cmV0dXJuIF8oITEpfSxbXSksdz1vKGZ1bmN0aW9uKGUpe3ZhciByPWU/d2luZG93LmFkZEV2ZW50TGlzdGVuZXI6d2luZG93LnJlbW92ZUV2ZW50TGlzdGVuZXI7cihnLmN1cnJlbnQ/XCJ0b3VjaG1vdmVcIjpcIm1vdXNlbW92ZVwiLEUpLHIoZy5jdXJyZW50P1widG91Y2hlbmRcIjpcIm1vdXNldXBcIixOKX0sW0UsTl0pO3JldHVybiBjKGZ1bmN0aW9uKCl7cmV0dXJuIHcoYiksZnVuY3Rpb24oKXtiJiZ3KCExKX19LFtiLHddKSxlLmNyZWF0ZUVsZW1lbnQoXCJkaXZcIixsKHt9LGYse2NsYXNzTmFtZTpcInJlYWN0LWNvbG9yZnVsX19pbnRlcmFjdGl2ZVwiLHJlZjptLG9uVG91Y2hTdGFydDpILG9uTW91c2VEb3duOkgsb25LZXlEb3duOk0sdGFiSW5kZXg6MCxyb2xlOlwic2xpZGVyXCJ9KSl9KSxnPWZ1bmN0aW9uKGUpe3JldHVybiBlLmZpbHRlcihCb29sZWFuKS5qb2luKFwiIFwiKX0scD1mdW5jdGlvbihyKXt2YXIgdD1yLmNvbG9yLG89ci5sZWZ0LG49ci50b3AsYT12b2lkIDA9PT1uPy41Om4sbD1nKFtcInJlYWN0LWNvbG9yZnVsX19wb2ludGVyXCIsci5jbGFzc05hbWVdKTtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KFwiZGl2XCIse2NsYXNzTmFtZTpsLHN0eWxlOnt0b3A6MTAwKmErXCIlXCIsbGVmdDoxMDAqbytcIiVcIn19LGUuY3JlYXRlRWxlbWVudChcImRpdlwiLHtjbGFzc05hbWU6XCJyZWFjdC1jb2xvcmZ1bF9fcG9pbnRlci1maWxsXCIsc3R5bGU6e2JhY2tncm91bmRDb2xvcjp0fX0pKX0sYj1mdW5jdGlvbihlLHIsdCl7cmV0dXJuIHZvaWQgMD09PXImJihyPTApLHZvaWQgMD09PXQmJih0PU1hdGgucG93KDEwLHIpKSxNYXRoLnJvdW5kKHQqZSkvdH0sXz17Z3JhZDouOSx0dXJuOjM2MCxyYWQ6MzYwLygyKk1hdGguUEkpfSxDPWZ1bmN0aW9uKGUpe3JldHVyblwiI1wiPT09ZVswXSYmKGU9ZS5zdWJzdHIoMSkpLGUubGVuZ3RoPDY/e3I6cGFyc2VJbnQoZVswXStlWzBdLDE2KSxnOnBhcnNlSW50KGVbMV0rZVsxXSwxNiksYjpwYXJzZUludChlWzJdK2VbMl0sMTYpLGE6MX06e3I6cGFyc2VJbnQoZS5zdWJzdHIoMCwyKSwxNiksZzpwYXJzZUludChlLnN1YnN0cigyLDIpLDE2KSxiOnBhcnNlSW50KGUuc3Vic3RyKDQsMiksMTYpLGE6MX19LHg9ZnVuY3Rpb24oZSxyKXtyZXR1cm4gdm9pZCAwPT09ciYmKHI9XCJkZWdcIiksTnVtYmVyKGUpKihfW3JdfHwxKX0sRT1mdW5jdGlvbihlKXt2YXIgcj0vaHNsYT9cXCg/XFxzKigtP1xcZCpcXC4/XFxkKykoZGVnfHJhZHxncmFkfHR1cm4pP1ssXFxzXSsoLT9cXGQqXFwuP1xcZCspJT9bLFxcc10rKC0/XFxkKlxcLj9cXGQrKSU/LD9cXHMqWy9cXHNdKigtP1xcZCpcXC4/XFxkKyk/KCUpP1xccypcXCk/L2kuZXhlYyhlKTtyZXR1cm4gcj9NKHtoOngoclsxXSxyWzJdKSxzOk51bWJlcihyWzNdKSxsOk51bWJlcihyWzRdKSxhOnZvaWQgMD09PXJbNV0/MTpOdW1iZXIocls1XSkvKHJbNl0/MTAwOjEpfSk6e2g6MCxzOjAsdjowLGE6MX19LEg9RSxNPWZ1bmN0aW9uKGUpe3ZhciByPWUucyx0PWUubDtyZXR1cm57aDplLmgsczoocio9KHQ8NTA/dDoxMDAtdCkvMTAwKT4wPzIqci8odCtyKSoxMDA6MCx2OnQrcixhOmUuYX19LE49ZnVuY3Rpb24oZSl7dmFyIHI9ZS5zLHQ9ZS52LG89ZS5hLG49KDIwMC1yKSp0LzEwMDtyZXR1cm57aDpiKGUuaCksczpiKG4+MCYmbjwyMDA/cip0LzEwMC8objw9MTAwP246MjAwLW4pKjEwMDowKSxsOmIobi8yKSxhOmIobywyKX19LHc9ZnVuY3Rpb24oZSl7dmFyIHI9TihlKTtyZXR1cm5cImhzbChcIityLmgrXCIsIFwiK3IucytcIiUsIFwiK3IubCtcIiUpXCJ9LHk9ZnVuY3Rpb24oZSl7dmFyIHI9TihlKTtyZXR1cm5cImhzbGEoXCIrci5oK1wiLCBcIityLnMrXCIlLCBcIityLmwrXCIlLCBcIityLmErXCIpXCJ9LHE9ZnVuY3Rpb24oZSl7dmFyIHI9ZS5oLHQ9ZS5zLG89ZS52LG49ZS5hO3I9ci8zNjAqNix0Lz0xMDAsby89MTAwO3ZhciBhPU1hdGguZmxvb3IociksbD1vKigxLXQpLHU9byooMS0oci1hKSp0KSxjPW8qKDEtKDEtcithKSp0KSxpPWElNjtyZXR1cm57cjpiKDI1NSpbbyx1LGwsbCxjLG9dW2ldKSxnOmIoMjU1KltjLG8sbyx1LGwsbF1baV0pLGI6YigyNTUqW2wsbCxjLG8sbyx1XVtpXSksYTpiKG4sMil9fSxrPWZ1bmN0aW9uKGUpe3ZhciByPS9oc3ZhP1xcKD9cXHMqKC0/XFxkKlxcLj9cXGQrKShkZWd8cmFkfGdyYWR8dHVybik/WyxcXHNdKygtP1xcZCpcXC4/XFxkKyklP1ssXFxzXSsoLT9cXGQqXFwuP1xcZCspJT8sP1xccypbL1xcc10qKC0/XFxkKlxcLj9cXGQrKT8oJSk/XFxzKlxcKT8vaS5leGVjKGUpO3JldHVybiByP0soe2g6eChyWzFdLHJbMl0pLHM6TnVtYmVyKHJbM10pLHY6TnVtYmVyKHJbNF0pLGE6dm9pZCAwPT09cls1XT8xOk51bWJlcihyWzVdKS8ocls2XT8xMDA6MSl9KTp7aDowLHM6MCx2OjAsYToxfX0sTz1rLEk9ZnVuY3Rpb24oZSl7dmFyIHI9L3JnYmE/XFwoP1xccyooLT9cXGQqXFwuP1xcZCspKCUpP1ssXFxzXSsoLT9cXGQqXFwuP1xcZCspKCUpP1ssXFxzXSsoLT9cXGQqXFwuP1xcZCspKCUpPyw/XFxzKlsvXFxzXSooLT9cXGQqXFwuP1xcZCspPyglKT9cXHMqXFwpPy9pLmV4ZWMoZSk7cmV0dXJuIHI/Qih7cjpOdW1iZXIoclsxXSkvKHJbMl0/MTAwLzI1NToxKSxnOk51bWJlcihyWzNdKS8ocls0XT8xMDAvMjU1OjEpLGI6TnVtYmVyKHJbNV0pLyhyWzZdPzEwMC8yNTU6MSksYTp2b2lkIDA9PT1yWzddPzE6TnVtYmVyKHJbN10pLyhyWzhdPzEwMDoxKX0pOntoOjAsczowLHY6MCxhOjF9fSxqPUksej1mdW5jdGlvbihlKXt2YXIgcj1lLnRvU3RyaW5nKDE2KTtyZXR1cm4gci5sZW5ndGg8Mj9cIjBcIityOnJ9LEI9ZnVuY3Rpb24oZSl7dmFyIHI9ZS5yLHQ9ZS5nLG89ZS5iLG49ZS5hLGE9TWF0aC5tYXgocix0LG8pLGw9YS1NYXRoLm1pbihyLHQsbyksdT1sP2E9PT1yPyh0LW8pL2w6YT09PXQ/Misoby1yKS9sOjQrKHItdCkvbDowO3JldHVybntoOmIoNjAqKHU8MD91KzY6dSkpLHM6YihhP2wvYSoxMDA6MCksdjpiKGEvMjU1KjEwMCksYTpufX0sSz1mdW5jdGlvbihlKXtyZXR1cm57aDpiKGUuaCksczpiKGUucyksdjpiKGUudiksYTpiKGUuYSwyKX19LEE9ZS5tZW1vKGZ1bmN0aW9uKHIpe3ZhciB0PXIuaHVlLG89ci5vbkNoYW5nZSxuPWcoW1wicmVhY3QtY29sb3JmdWxfX2h1ZVwiLHIuY2xhc3NOYW1lXSk7cmV0dXJuIGUuY3JlYXRlRWxlbWVudChcImRpdlwiLHtjbGFzc05hbWU6bn0sZS5jcmVhdGVFbGVtZW50KG0se29uTW92ZTpmdW5jdGlvbihlKXtvKHtoOjM2MCplLmxlZnR9KX0sb25LZXk6ZnVuY3Rpb24oZSl7byh7aDpmKHQrMzYwKmUubGVmdCwwLDM2MCl9KX0sXCJhcmlhLWxhYmVsXCI6XCJIdWVcIixcImFyaWEtdmFsdWV0ZXh0XCI6Yih0KX0sZS5jcmVhdGVFbGVtZW50KHAse2NsYXNzTmFtZTpcInJlYWN0LWNvbG9yZnVsX19odWUtcG9pbnRlclwiLGxlZnQ6dC8zNjAsY29sb3I6dyh7aDp0LHM6MTAwLHY6MTAwLGE6MX0pfSkpKX0pLEw9ZS5tZW1vKGZ1bmN0aW9uKHIpe3ZhciB0PXIuaHN2YSxvPXIub25DaGFuZ2Usbj17YmFja2dyb3VuZENvbG9yOncoe2g6dC5oLHM6MTAwLHY6MTAwLGE6MX0pfTtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KFwiZGl2XCIse2NsYXNzTmFtZTpcInJlYWN0LWNvbG9yZnVsX19zYXR1cmF0aW9uXCIsc3R5bGU6bn0sZS5jcmVhdGVFbGVtZW50KG0se29uTW92ZTpmdW5jdGlvbihlKXtvKHtzOjEwMCplLmxlZnQsdjoxMDAtMTAwKmUudG9wfSl9LG9uS2V5OmZ1bmN0aW9uKGUpe28oe3M6Zih0LnMrMTAwKmUubGVmdCwwLDEwMCksdjpmKHQudi0xMDAqZS50b3AsMCwxMDApfSl9LFwiYXJpYS1sYWJlbFwiOlwiQ29sb3JcIixcImFyaWEtdmFsdWV0ZXh0XCI6XCJTYXR1cmF0aW9uIFwiK2IodC5zKStcIiUsIEJyaWdodG5lc3MgXCIrYih0LnYpK1wiJVwifSxlLmNyZWF0ZUVsZW1lbnQocCx7Y2xhc3NOYW1lOlwicmVhY3QtY29sb3JmdWxfX3NhdHVyYXRpb24tcG9pbnRlclwiLHRvcDoxLXQudi8xMDAsbGVmdDp0LnMvMTAwLGNvbG9yOncodCl9KSkpfSksRD1mdW5jdGlvbihlLHIpe2lmKGU9PT1yKXJldHVybiEwO2Zvcih2YXIgdCBpbiBlKWlmKGVbdF0hPT1yW3RdKXJldHVybiExO3JldHVybiEwfSxGPWZ1bmN0aW9uKGUscil7cmV0dXJuIGUucmVwbGFjZSgvXFxzL2csXCJcIik9PT1yLnJlcGxhY2UoL1xccy9nLFwiXCIpfTtmdW5jdGlvbiBTKGUscixsKXt2YXIgdT1pKGwpLGM9YShmdW5jdGlvbigpe3JldHVybiBlLnRvSHN2YShyKX0pLHM9Y1swXSxmPWNbMV0sdj1uKHtjb2xvcjpyLGhzdmE6c30pO3QoZnVuY3Rpb24oKXtpZighZS5lcXVhbChyLHYuY3VycmVudC5jb2xvcikpe3ZhciB0PWUudG9Ic3ZhKHIpO3YuY3VycmVudD17aHN2YTp0LGNvbG9yOnJ9LGYodCl9fSxbcixlXSksdChmdW5jdGlvbigpe3ZhciByO0Qocyx2LmN1cnJlbnQuaHN2YSl8fGUuZXF1YWwocj1lLmZyb21Ic3ZhKHMpLHYuY3VycmVudC5jb2xvcil8fCh2LmN1cnJlbnQ9e2hzdmE6cyxjb2xvcjpyfSx1KHIpKX0sW3MsZSx1XSk7dmFyIGQ9byhmdW5jdGlvbihlKXtmKGZ1bmN0aW9uKHIpe3JldHVybiBPYmplY3QuYXNzaWduKHt9LHIsZSl9KX0sW10pO3JldHVybltzLGRdfXZhciBQLFQ9ZnVuY3Rpb24oKXtyZXR1cm4gc3x8KFwidW5kZWZpbmVkXCIhPXR5cGVvZiBfX3dlYnBhY2tfbm9uY2VfXz9fX3dlYnBhY2tfbm9uY2VfXzp2b2lkIDApfSxYPWZ1bmN0aW9uKGUpe3M9ZX0sWT1mdW5jdGlvbigpe2MoZnVuY3Rpb24oKXtpZihcInVuZGVmaW5lZFwiIT10eXBlb2YgZG9jdW1lbnQmJiFQKXsoUD1kb2N1bWVudC5jcmVhdGVFbGVtZW50KFwic3R5bGVcIikpLmlubmVySFRNTD0nLnJlYWN0LWNvbG9yZnVse3Bvc2l0aW9uOnJlbGF0aXZlO2Rpc3BsYXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47d2lkdGg6MjAwcHg7aGVpZ2h0OjIwMHB4Oy13ZWJraXQtdXNlci1zZWxlY3Q6bm9uZTstbW96LXVzZXItc2VsZWN0Om5vbmU7LW1zLXVzZXItc2VsZWN0Om5vbmU7dXNlci1zZWxlY3Q6bm9uZTtjdXJzb3I6ZGVmYXVsdH0ucmVhY3QtY29sb3JmdWxfX3NhdHVyYXRpb257cG9zaXRpb246cmVsYXRpdmU7ZmxleC1ncm93OjE7Ym9yZGVyLWNvbG9yOnRyYW5zcGFyZW50O2JvcmRlci1ib3R0b206MTJweCBzb2xpZCAjMDAwO2JvcmRlci1yYWRpdXM6OHB4IDhweCAwIDA7YmFja2dyb3VuZC1pbWFnZTpsaW5lYXItZ3JhZGllbnQoMGRlZywjMDAwLHRyYW5zcGFyZW50KSxsaW5lYXItZ3JhZGllbnQoOTBkZWcsI2ZmZixoc2xhKDAsMCUsMTAwJSwwKSl9LnJlYWN0LWNvbG9yZnVsX19hbHBoYS1ncmFkaWVudCwucmVhY3QtY29sb3JmdWxfX3BvaW50ZXItZmlsbHtjb250ZW50OlwiXCI7cG9zaXRpb246YWJzb2x1dGU7bGVmdDowO3RvcDowO3JpZ2h0OjA7Ym90dG9tOjA7cG9pbnRlci1ldmVudHM6bm9uZTtib3JkZXItcmFkaXVzOmluaGVyaXR9LnJlYWN0LWNvbG9yZnVsX19hbHBoYS1ncmFkaWVudCwucmVhY3QtY29sb3JmdWxfX3NhdHVyYXRpb257Ym94LXNoYWRvdzppbnNldCAwIDAgMCAxcHggcmdiYSgwLDAsMCwuMDUpfS5yZWFjdC1jb2xvcmZ1bF9fYWxwaGEsLnJlYWN0LWNvbG9yZnVsX19odWV7cG9zaXRpb246cmVsYXRpdmU7aGVpZ2h0OjI0cHh9LnJlYWN0LWNvbG9yZnVsX19odWV7YmFja2dyb3VuZDpsaW5lYXItZ3JhZGllbnQoOTBkZWcscmVkIDAsI2ZmMCAxNyUsIzBmMCAzMyUsIzBmZiA1MCUsIzAwZiA2NyUsI2YwZiA4MyUscmVkKX0ucmVhY3QtY29sb3JmdWxfX2xhc3QtY29udHJvbHtib3JkZXItcmFkaXVzOjAgMCA4cHggOHB4fS5yZWFjdC1jb2xvcmZ1bF9faW50ZXJhY3RpdmV7cG9zaXRpb246YWJzb2x1dGU7bGVmdDowO3RvcDowO3JpZ2h0OjA7Ym90dG9tOjA7Ym9yZGVyLXJhZGl1czppbmhlcml0O291dGxpbmU6bm9uZTt0b3VjaC1hY3Rpb246bm9uZX0ucmVhY3QtY29sb3JmdWxfX3BvaW50ZXJ7cG9zaXRpb246YWJzb2x1dGU7ei1pbmRleDoxO2JveC1zaXppbmc6Ym9yZGVyLWJveDt3aWR0aDoyOHB4O2hlaWdodDoyOHB4O3RyYW5zZm9ybTp0cmFuc2xhdGUoLTUwJSwtNTAlKTtiYWNrZ3JvdW5kLWNvbG9yOiNmZmY7Ym9yZGVyOjJweCBzb2xpZCAjZmZmO2JvcmRlci1yYWRpdXM6NTAlO2JveC1zaGFkb3c6MCAycHggNHB4IHJnYmEoMCwwLDAsLjIpfS5yZWFjdC1jb2xvcmZ1bF9faW50ZXJhY3RpdmU6Zm9jdXMgLnJlYWN0LWNvbG9yZnVsX19wb2ludGVye3RyYW5zZm9ybTp0cmFuc2xhdGUoLTUwJSwtNTAlKSBzY2FsZSgxLjEpfS5yZWFjdC1jb2xvcmZ1bF9fYWxwaGEsLnJlYWN0LWNvbG9yZnVsX19hbHBoYS1wb2ludGVye2JhY2tncm91bmQtY29sb3I6I2ZmZjtiYWNrZ3JvdW5kLWltYWdlOnVybChcXCdkYXRhOmltYWdlL3N2Zyt4bWw7Y2hhcnNldD11dGYtOCw8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiB3aWR0aD1cIjE2XCIgaGVpZ2h0PVwiMTZcIiBmaWxsLW9wYWNpdHk9XCIuMDVcIj48cGF0aCBkPVwiTTggMGg4djhIOHpNMCA4aDh2OEgwelwiLz48L3N2Zz5cXCcpfS5yZWFjdC1jb2xvcmZ1bF9fc2F0dXJhdGlvbi1wb2ludGVye3otaW5kZXg6M30ucmVhY3QtY29sb3JmdWxfX2h1ZS1wb2ludGVye3otaW5kZXg6Mn0nO3ZhciBlPVQoKTtlJiZQLnNldEF0dHJpYnV0ZShcIm5vbmNlXCIsZSksZG9jdW1lbnQuaGVhZC5hcHBlbmRDaGlsZChQKX19LFtdKX0sJD1mdW5jdGlvbihyKXt2YXIgdD1yLmNsYXNzTmFtZSxvPXIuY29sb3JNb2RlbCxuPXIuY29sb3IsYT12b2lkIDA9PT1uP28uZGVmYXVsdENvbG9yOm4sYz1yLm9uQ2hhbmdlLGk9dShyLFtcImNsYXNzTmFtZVwiLFwiY29sb3JNb2RlbFwiLFwiY29sb3JcIixcIm9uQ2hhbmdlXCJdKTtZKCk7dmFyIHM9UyhvLGEsYyksZj1zWzBdLHY9c1sxXSxkPWcoW1wicmVhY3QtY29sb3JmdWxcIix0XSk7cmV0dXJuIGUuY3JlYXRlRWxlbWVudChcImRpdlwiLGwoe30saSx7Y2xhc3NOYW1lOmR9KSxlLmNyZWF0ZUVsZW1lbnQoTCx7aHN2YTpmLG9uQ2hhbmdlOnZ9KSxlLmNyZWF0ZUVsZW1lbnQoQSx7aHVlOmYuaCxvbkNoYW5nZTp2LGNsYXNzTmFtZTpcInJlYWN0LWNvbG9yZnVsX19sYXN0LWNvbnRyb2xcIn0pKX0sUj17ZGVmYXVsdENvbG9yOlwiMDAwXCIsdG9Ic3ZhOmZ1bmN0aW9uKGUpe3JldHVybiBCKEMoZSkpfSxmcm9tSHN2YTpmdW5jdGlvbihlKXtyZXR1cm4gdD0ocj1xKGUpKS5nLG89ci5iLFwiI1wiK3ooci5yKSt6KHQpK3oobyk7dmFyIHIsdCxvfSxlcXVhbDpmdW5jdGlvbihlLHIpe3JldHVybiBlLnRvTG93ZXJDYXNlKCk9PT1yLnRvTG93ZXJDYXNlKCl8fEQoQyhlKSxDKHIpKX19LEc9ZnVuY3Rpb24ocil7cmV0dXJuIGUuY3JlYXRlRWxlbWVudCgkLGwoe30scix7Y29sb3JNb2RlbDpSfSkpfSxKPWZ1bmN0aW9uKHIpe3ZhciB0PXIuY2xhc3NOYW1lLG89ci5oc3ZhLG49ci5vbkNoYW5nZSxhPXtiYWNrZ3JvdW5kSW1hZ2U6XCJsaW5lYXItZ3JhZGllbnQoOTBkZWcsIFwiK3koT2JqZWN0LmFzc2lnbih7fSxvLHthOjB9KSkrXCIsIFwiK3koT2JqZWN0LmFzc2lnbih7fSxvLHthOjF9KSkrXCIpXCJ9LGw9ZyhbXCJyZWFjdC1jb2xvcmZ1bF9fYWxwaGFcIix0XSk7cmV0dXJuIGUuY3JlYXRlRWxlbWVudChcImRpdlwiLHtjbGFzc05hbWU6bH0sZS5jcmVhdGVFbGVtZW50KFwiZGl2XCIse2NsYXNzTmFtZTpcInJlYWN0LWNvbG9yZnVsX19hbHBoYS1ncmFkaWVudFwiLHN0eWxlOmF9KSxlLmNyZWF0ZUVsZW1lbnQobSx7b25Nb3ZlOmZ1bmN0aW9uKGUpe24oe2E6ZS5sZWZ0fSl9LG9uS2V5OmZ1bmN0aW9uKGUpe24oe2E6ZihvLmErZS5sZWZ0KX0pfSxcImFyaWEtbGFiZWxcIjpcIkFscGhhXCIsXCJhcmlhLXZhbHVldGV4dFwiOmIoMTAwKm8uYSkrXCIlXCJ9LGUuY3JlYXRlRWxlbWVudChwLHtjbGFzc05hbWU6XCJyZWFjdC1jb2xvcmZ1bF9fYWxwaGEtcG9pbnRlclwiLGxlZnQ6by5hLGNvbG9yOnkobyl9KSkpfSxRPWZ1bmN0aW9uKHIpe3ZhciB0PXIuY2xhc3NOYW1lLG89ci5jb2xvck1vZGVsLG49ci5jb2xvcixhPXZvaWQgMD09PW4/by5kZWZhdWx0Q29sb3I6bixjPXIub25DaGFuZ2UsaT11KHIsW1wiY2xhc3NOYW1lXCIsXCJjb2xvck1vZGVsXCIsXCJjb2xvclwiLFwib25DaGFuZ2VcIl0pO1koKTt2YXIgcz1TKG8sYSxjKSxmPXNbMF0sdj1zWzFdLGQ9ZyhbXCJyZWFjdC1jb2xvcmZ1bFwiLHRdKTtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KFwiZGl2XCIsbCh7fSxpLHtjbGFzc05hbWU6ZH0pLGUuY3JlYXRlRWxlbWVudChMLHtoc3ZhOmYsb25DaGFuZ2U6dn0pLGUuY3JlYXRlRWxlbWVudChBLHtodWU6Zi5oLG9uQ2hhbmdlOnZ9KSxlLmNyZWF0ZUVsZW1lbnQoSix7aHN2YTpmLG9uQ2hhbmdlOnYsY2xhc3NOYW1lOlwicmVhY3QtY29sb3JmdWxfX2xhc3QtY29udHJvbFwifSkpfSxVPXtkZWZhdWx0Q29sb3I6e2g6MCxzOjAsbDowLGE6MX0sdG9Ic3ZhOk0sZnJvbUhzdmE6TixlcXVhbDpEfSxWPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoUSxsKHt9LHIse2NvbG9yTW9kZWw6VX0pKX0sVz17ZGVmYXVsdENvbG9yOlwiaHNsYSgwLCAwJSwgMCUsIDEpXCIsdG9Ic3ZhOkUsZnJvbUhzdmE6eSxlcXVhbDpGfSxaPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoUSxsKHt9LHIse2NvbG9yTW9kZWw6V30pKX0sZWU9e2RlZmF1bHRDb2xvcjp7aDowLHM6MCxsOjB9LHRvSHN2YTpmdW5jdGlvbihlKXtyZXR1cm4gTSh7aDplLmgsczplLnMsbDplLmwsYToxfSl9LGZyb21Ic3ZhOmZ1bmN0aW9uKGUpe3JldHVybntoOihyPU4oZSkpLmgsczpyLnMsbDpyLmx9O3ZhciByfSxlcXVhbDpEfSxyZT1mdW5jdGlvbihyKXtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KCQsbCh7fSxyLHtjb2xvck1vZGVsOmVlfSkpfSx0ZT17ZGVmYXVsdENvbG9yOlwiaHNsKDAsIDAlLCAwJSlcIix0b0hzdmE6SCxmcm9tSHN2YTp3LGVxdWFsOkZ9LG9lPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoJCxsKHt9LHIse2NvbG9yTW9kZWw6dGV9KSl9LG5lPXtkZWZhdWx0Q29sb3I6e2g6MCxzOjAsdjowLGE6MX0sdG9Ic3ZhOmZ1bmN0aW9uKGUpe3JldHVybiBlfSxmcm9tSHN2YTpLLGVxdWFsOkR9LGFlPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoUSxsKHt9LHIse2NvbG9yTW9kZWw6bmV9KSl9LGxlPXtkZWZhdWx0Q29sb3I6XCJoc3ZhKDAsIDAlLCAwJSwgMSlcIix0b0hzdmE6ayxmcm9tSHN2YTpmdW5jdGlvbihlKXt2YXIgcj1LKGUpO3JldHVyblwiaHN2YShcIityLmgrXCIsIFwiK3IucytcIiUsIFwiK3IuditcIiUsIFwiK3IuYStcIilcIn0sZXF1YWw6Rn0sdWU9ZnVuY3Rpb24ocil7cmV0dXJuIGUuY3JlYXRlRWxlbWVudChRLGwoe30scix7Y29sb3JNb2RlbDpsZX0pKX0sY2U9e2RlZmF1bHRDb2xvcjp7aDowLHM6MCx2OjB9LHRvSHN2YTpmdW5jdGlvbihlKXtyZXR1cm57aDplLmgsczplLnMsdjplLnYsYToxfX0sZnJvbUhzdmE6ZnVuY3Rpb24oZSl7dmFyIHI9SyhlKTtyZXR1cm57aDpyLmgsczpyLnMsdjpyLnZ9fSxlcXVhbDpEfSxpZT1mdW5jdGlvbihyKXtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KCQsbCh7fSxyLHtjb2xvck1vZGVsOmNlfSkpfSxzZT17ZGVmYXVsdENvbG9yOlwiaHN2KDAsIDAlLCAwJSlcIix0b0hzdmE6Tyxmcm9tSHN2YTpmdW5jdGlvbihlKXt2YXIgcj1LKGUpO3JldHVyblwiaHN2KFwiK3IuaCtcIiwgXCIrci5zK1wiJSwgXCIrci52K1wiJSlcIn0sZXF1YWw6Rn0sZmU9ZnVuY3Rpb24ocil7cmV0dXJuIGUuY3JlYXRlRWxlbWVudCgkLGwoe30scix7Y29sb3JNb2RlbDpzZX0pKX0sdmU9e2RlZmF1bHRDb2xvcjp7cjowLGc6MCxiOjAsYToxfSx0b0hzdmE6Qixmcm9tSHN2YTpxLGVxdWFsOkR9LGRlPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoUSxsKHt9LHIse2NvbG9yTW9kZWw6dmV9KSl9LGhlPXtkZWZhdWx0Q29sb3I6XCJyZ2JhKDAsIDAsIDAsIDEpXCIsdG9Ic3ZhOkksZnJvbUhzdmE6ZnVuY3Rpb24oZSl7dmFyIHI9cShlKTtyZXR1cm5cInJnYmEoXCIrci5yK1wiLCBcIityLmcrXCIsIFwiK3IuYitcIiwgXCIrci5hK1wiKVwifSxlcXVhbDpGfSxtZT1mdW5jdGlvbihyKXtyZXR1cm4gZS5jcmVhdGVFbGVtZW50KFEsbCh7fSxyLHtjb2xvck1vZGVsOmhlfSkpfSxnZT17ZGVmYXVsdENvbG9yOntyOjAsZzowLGI6MH0sdG9Ic3ZhOmZ1bmN0aW9uKGUpe3JldHVybiBCKHtyOmUucixnOmUuZyxiOmUuYixhOjF9KX0sZnJvbUhzdmE6ZnVuY3Rpb24oZSl7cmV0dXJue3I6KHI9cShlKSkucixnOnIuZyxiOnIuYn07dmFyIHJ9LGVxdWFsOkR9LHBlPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoJCxsKHt9LHIse2NvbG9yTW9kZWw6Z2V9KSl9LGJlPXtkZWZhdWx0Q29sb3I6XCJyZ2IoMCwgMCwgMClcIix0b0hzdmE6aixmcm9tSHN2YTpmdW5jdGlvbihlKXt2YXIgcj1xKGUpO3JldHVyblwicmdiKFwiK3IucitcIiwgXCIrci5nK1wiLCBcIityLmIrXCIpXCJ9LGVxdWFsOkZ9LF9lPWZ1bmN0aW9uKHIpe3JldHVybiBlLmNyZWF0ZUVsZW1lbnQoJCxsKHt9LHIse2NvbG9yTW9kZWw6YmV9KSl9LENlPS9eIz9bMC05QS1GXXszfSQvaSx4ZT0vXiM/WzAtOUEtRl17Nn0kL2ksRWU9ZnVuY3Rpb24oZSl7cmV0dXJuIHhlLnRlc3QoZSl8fENlLnRlc3QoZSl9LEhlPWZ1bmN0aW9uKGUpe3JldHVybiBlLnJlcGxhY2UoLyhbXjAtOUEtRl0rKS9naSxcIlwiKS5zdWJzdHIoMCw2KX0sTWU9ZnVuY3Rpb24ocil7dmFyIG49ci5jb2xvcixjPXZvaWQgMD09PW4/XCJcIjpuLHM9ci5vbkNoYW5nZSxmPXIub25CbHVyLHY9ci5wcmVmaXhlZCxkPXUocixbXCJjb2xvclwiLFwib25DaGFuZ2VcIixcIm9uQmx1clwiLFwicHJlZml4ZWRcIl0pLGg9YShmdW5jdGlvbigpe3JldHVybiBIZShjKX0pLG09aFswXSxnPWhbMV0scD1pKHMpLGI9aShmKSxfPW8oZnVuY3Rpb24oZSl7dmFyIHI9SGUoZS50YXJnZXQudmFsdWUpO2cociksRWUocikmJnAoXCIjXCIrcil9LFtwXSksQz1vKGZ1bmN0aW9uKGUpe0VlKGUudGFyZ2V0LnZhbHVlKXx8ZyhIZShjKSksYihlKX0sW2MsYl0pO3JldHVybiB0KGZ1bmN0aW9uKCl7ZyhIZShjKSl9LFtjXSksZS5jcmVhdGVFbGVtZW50KFwiaW5wdXRcIixsKHt9LGQse3ZhbHVlOih2P1wiI1wiOlwiXCIpK20sc3BlbGxDaGVjazpcImZhbHNlXCIsb25DaGFuZ2U6XyxvbkJsdXI6Q30pKX07ZXhwb3J0e01lIGFzIEhleENvbG9ySW5wdXQsRyBhcyBIZXhDb2xvclBpY2tlcixyZSBhcyBIc2xDb2xvclBpY2tlcixvZSBhcyBIc2xTdHJpbmdDb2xvclBpY2tlcixWIGFzIEhzbGFDb2xvclBpY2tlcixaIGFzIEhzbGFTdHJpbmdDb2xvclBpY2tlcixpZSBhcyBIc3ZDb2xvclBpY2tlcixmZSBhcyBIc3ZTdHJpbmdDb2xvclBpY2tlcixhZSBhcyBIc3ZhQ29sb3JQaWNrZXIsdWUgYXMgSHN2YVN0cmluZ0NvbG9yUGlja2VyLHBlIGFzIFJnYkNvbG9yUGlja2VyLF9lIGFzIFJnYlN0cmluZ0NvbG9yUGlja2VyLGRlIGFzIFJnYmFDb2xvclBpY2tlcixtZSBhcyBSZ2JhU3RyaW5nQ29sb3JQaWNrZXIsWCBhcyBzZXROb25jZX07XG4vLyMgc291cmNlTWFwcGluZ1VSTD1pbmRleC5tb2R1bGUuanMubWFwXG4iLCJpbXBvcnQgUmVhY3QsIHt1c2VDYWxsYmFjaywgdXNlTWVtb30gZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtcbiAgICBIc2xhQ29sb3IsXG4gICAgSHNsQ29sb3IsXG4gICAgSHN2YUNvbG9yLFxuICAgIEhzdkNvbG9yLFxuICAgIFJnYmFDb2xvcixcbiAgICBSZ2JDb2xvcixcbiAgICBIZXhDb2xvclBpY2tlcixcbiAgICBSZ2JhQ29sb3JQaWNrZXIsXG4gICAgUmdiYVN0cmluZ0NvbG9yUGlja2VyLFxuICAgIEhzbENvbG9yUGlja2VyLFxuICAgIEhzbFN0cmluZ0NvbG9yUGlja2VyLFxuICAgIFJnYkNvbG9yUGlja2VyLFxuICAgIFJnYlN0cmluZ0NvbG9yUGlja2VyLFxuICAgIEhzbGFDb2xvclBpY2tlcixcbiAgICBIc2xhU3RyaW5nQ29sb3JQaWNrZXIsXG4gICAgSHN2Q29sb3JQaWNrZXIsXG4gICAgSHN2YVN0cmluZ0NvbG9yUGlja2VyLFxuICAgIEhzdmFDb2xvclBpY2tlcixcbiAgICBIc3ZTdHJpbmdDb2xvclBpY2tlcixcbn0gZnJvbSAncmVhY3QtY29sb3JmdWwnO1xuXG5pbXBvcnQge1xuICAgIEFueURpY3QsXG4gICAgQ29tbW9uUHJlc2V0c1Byb3BzLFxuICAgIENvbW1vblN0eWxlUHJvcHMsXG4gICAgRGF6emxlclByb3BzLFxufSBmcm9tICcuLi8uLi8uLi9jb21tb25zL2pzL3R5cGVzJztcbmltcG9ydCB7Z2V0Q29tbW9uU3R5bGVzLCBnZXRQcmVzZXRzQ2xhc3NOYW1lcywgdGhyb3R0bGV9IGZyb20gJ2NvbW1vbnMnO1xuaW1wb3J0IHtBbnlDb2xvcn0gZnJvbSAncmVhY3QtY29sb3JmdWwvZGlzdC90eXBlcyc7XG5cbnR5cGUgQ29sb3JQaWNrZXJQcm9wcyA9IHtcbiAgICAvKipcbiAgICAgKiBDdXJyZW50IGNvbG9yIHZhbHVlXG4gICAgICovXG4gICAgdmFsdWU/OiBBbnlDb2xvcjtcbiAgICAvKipcbiAgICAgKiBUeXBlIG9mIGNvbG9yXG4gICAgICovXG4gICAgdHlwZT86ICdoZXgnIHwgJ3JnYicgfCAncmdiYScgfCAnaHNsJyB8ICdoc2xhJyB8ICdoc3YnIHwgJ2hzdmEnO1xuICAgIC8qKlxuICAgICAqIEFkZCBhIHRvZ2dsZSBidXR0b24gdG8gYWN0aXZhdGUgdGhlIGNvbG9yIHBpY2tlci5cbiAgICAgKi9cbiAgICB0b2dnbGVhYmxlPzogYm9vbGVhbjtcbiAgICAvKipcbiAgICAgKiBDb250ZW50IG9mIHRoZSB0b2dnbGUgYnV0dG9uLlxuICAgICAqL1xuICAgIHRvZ2dsZV9idXR0b24/OiBKU1guRWxlbWVudDtcbiAgICAvKipcbiAgICAgKiBDbG9zZSB0aGUgY29sb3IgcGlja2VyIHdoZW4gYSB2YWx1ZSBpcyBzZWxlY3RlZC5cbiAgICAgKi9cbiAgICB0b2dnbGVfb25fY2hvb3NlPzogYm9vbGVhbjtcbiAgICAvKipcbiAgICAgKiBEZWxheSBiZWZvcmUgY2xvc2luZyB0aGUgbW9kYWwgd2hlbiB0aGVcbiAgICAgKi9cbiAgICB0b2dnbGVfb25fY2hvb3NlX2RlbGF5PzogbnVtYmVyO1xuICAgIC8qKlxuICAgICAqIERpcmVjdGlvbiB0byBvcGVuIHRoZSBjb2xvciBwaWNrZXIgb24gdG9nZ2xlLlxuICAgICAqL1xuICAgIHRvZ2dsZV9kaXJlY3Rpb24/OlxuICAgICAgICB8ICd0b3AnXG4gICAgICAgIHwgJ3RvcC1sZWZ0J1xuICAgICAgICB8ICd0b3AtcmlnaHQnXG4gICAgICAgIHwgJ2xlZnQnXG4gICAgICAgIHwgJ3JpZ2h0J1xuICAgICAgICB8ICdib3R0b20nXG4gICAgICAgIHwgJ2JvdHRvbS1sZWZ0J1xuICAgICAgICB8ICdib3R0b20tcmlnaHQnO1xuICAgIC8qKlxuICAgICAqIFNob3cgdGhlIGNvbG9yIHBpY2tlci5cbiAgICAgKi9cbiAgICBhY3RpdmU/OiBib29sZWFuO1xuICAgIC8qKlxuICAgICAqIFVzZSBhIHNxdWFyZSB3aXRoIGJhY2tncm91bmQgY29sb3IgZnJvbSB0aGUgdmFsdWUgYXMgdGhlIHRvZ2dsZSBidXR0b24uXG4gICAgICovXG4gICAgdG9nZ2xlX2J1dHRvbl9jb2xvcj86IGJvb2xlYW47XG4gICAgLyoqXG4gICAgICogVGhlIHZhbHVlIHdpbGwgYWx3YXlzIGJlIGEgc3RyaW5nLCB1c2FibGUgZGlyZWN0bHkgaW4gc3R5bGVzLlxuICAgICAqXG4gICAgICogYGB0b2dnbGVfYnV0dG9uX2NvbG9yYGAgcmVxdWlyZXMgYSBzdHJpbmcgdmFsdWUgb3IgaGV4IHR5cGUuXG4gICAgICovXG4gICAgYXNfc3RyaW5nPzogYm9vbGVhbjtcbn0gJiBDb21tb25TdHlsZVByb3BzICZcbiAgICBDb21tb25QcmVzZXRzUHJvcHMgJlxuICAgIERhenpsZXJQcm9wcztcblxuLyoqXG4gKiBBIGNvbG9yIHBpY2tlciBwb3dlcmVkIGJ5IHJlYWN0LWNvbG9yZnVsXG4gKlxuICogQSB0b2dnbGUgYnV0dG9uIGlzIGluY2x1ZGVkIG9yIGNhbiBiZSBkaXNhYmxlZCB3aXRoIGBgdG9nZ2xlYWJsZT1GYWxzZWBgXG4gKiBhbmQgdGhlbiBpdCBiZSBhY3RpdmF0ZWQgYnkgYmluZGluZywgdGllIG9yIGluaXRpYWwgdmFsdWUuXG4gKlxuICogQ29tbW9uIHN0eWxlIGFzcGVjdHMgZ29lcyBvbiB0aGUgY29udGFpbmVyIG9mIHRoZSBwaWNrZXIsIGhpZGRlbiBieSBkZWZhdWx0LlxuICpcbiAqIDpDU1M6XG4gKlxuICogICAgICAtIGBgZGF6emxlci1leHRyYS1jb2xvci1waWNrZXJgYCAtIFRvcCBsZXZlbCBjb250YWluZXJcbiAqICAgICAgLSBgYGRhenpsZXItY29sb3ItcGlja2VyLXRvZ2dsZWBgIC0gVG9nZ2xlIGJ1dHRvblxuICogICAgICAtIGBgZGF6emxlci1jb2xvci1waWNrZXJgYCAtIFBpY2tlciBjb250YWluZXIuXG4gKlxuICogLi4gbGl0ZXJhbGluY2x1ZGU6OiAuLi8uLi90ZXN0cy9jb21wb25lbnRzL3BhZ2VzL2NvbG9yX3BpY2tlci5weVxuICovXG5jb25zdCBDb2xvclBpY2tlciA9IChwcm9wczogQ29sb3JQaWNrZXJQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtcbiAgICAgICAgaWRlbnRpdHksXG4gICAgICAgIGNsYXNzX25hbWUsXG4gICAgICAgIHN0eWxlLFxuICAgICAgICB0eXBlLFxuICAgICAgICB0b2dnbGVhYmxlLFxuICAgICAgICB0b2dnbGVfYnV0dG9uLFxuICAgICAgICB0b2dnbGVfb25fY2hvb3NlLFxuICAgICAgICB0b2dnbGVfb25fY2hvb3NlX2RlbGF5LFxuICAgICAgICB0b2dnbGVfYnV0dG9uX2NvbG9yLFxuICAgICAgICB0b2dnbGVfZGlyZWN0aW9uLFxuICAgICAgICBhY3RpdmUsXG4gICAgICAgIHZhbHVlLFxuICAgICAgICB1cGRhdGVBc3BlY3RzLFxuICAgICAgICBhc19zdHJpbmcsXG4gICAgICAgIC4uLnJlc3RcbiAgICB9ID0gcHJvcHM7XG4gICAgY29uc3QgY3NzID0gdXNlTWVtbyhcbiAgICAgICAgKCkgPT5cbiAgICAgICAgICAgIGdldFByZXNldHNDbGFzc05hbWVzKFxuICAgICAgICAgICAgICAgIHJlc3QsXG4gICAgICAgICAgICAgICAgJ2RhenpsZXItY29sb3ItcGlja2VyJyxcbiAgICAgICAgICAgICAgICBgdG9nZ2xlLWRpcmVjdGlvbi0ke3RvZ2dsZV9kaXJlY3Rpb24gYXMgc3RyaW5nfWBcbiAgICAgICAgICAgICksXG4gICAgICAgIFtyZXN0LCBhY3RpdmVdXG4gICAgKTtcblxuICAgIGNvbnN0IGNsYXNzTmFtZSA9IHVzZU1lbW8oKCkgPT4ge1xuICAgICAgICBjb25zdCBjID0gW2NsYXNzX25hbWVdO1xuICAgICAgICBpZiAoYWN0aXZlKSB7XG4gICAgICAgICAgICBjLnB1c2goJ2FjdGl2ZScpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBjLmpvaW4oJyAnKTtcbiAgICB9LCBbY2xhc3NfbmFtZSwgYWN0aXZlXSk7XG5cbiAgICBjb25zdCBzdHlsaW5nID0gdXNlTWVtbygoKSA9PiBnZXRDb21tb25TdHlsZXMocmVzdCwgc3R5bGUpLCBbcmVzdCwgc3R5bGVdKTtcblxuICAgIGNvbnN0IGF1dG9DbG9zZSA9IHVzZUNhbGxiYWNrKFxuICAgICAgICB0aHJvdHRsZTx2b2lkPihcbiAgICAgICAgICAgICgpID0+IHVwZGF0ZUFzcGVjdHMoe2FjdGl2ZTogZmFsc2V9KSxcbiAgICAgICAgICAgIHRvZ2dsZV9vbl9jaG9vc2VfZGVsYXksXG4gICAgICAgICAgICB0cnVlXG4gICAgICAgICksXG4gICAgICAgIFtdXG4gICAgKTtcblxuICAgIGNvbnN0IHBpY2tlciA9IHVzZU1lbW8oKCkgPT4ge1xuICAgICAgICBjb25zdCBvbkNoYW5nZSA9IChuZXdDb2xvcikgPT4ge1xuICAgICAgICAgICAgY29uc3QgcGF5bG9hZDogQW55RGljdCA9IHt2YWx1ZTogbmV3Q29sb3J9O1xuICAgICAgICAgICAgaWYgKHRvZ2dsZV9vbl9jaG9vc2UpIHtcbiAgICAgICAgICAgICAgICBhdXRvQ2xvc2UoKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMocGF5bG9hZCk7XG4gICAgICAgIH07XG4gICAgICAgIHN3aXRjaCAodHlwZSkge1xuICAgICAgICAgICAgY2FzZSAncmdiJzpcbiAgICAgICAgICAgICAgICBpZiAoYXNfc3RyaW5nKSB7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgICAgICA8UmdiU3RyaW5nQ29sb3JQaWNrZXJcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBvbkNoYW5nZT17b25DaGFuZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I9e3ZhbHVlIGFzIHN0cmluZ31cbiAgICAgICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgIDxSZ2JDb2xvclBpY2tlclxuICAgICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e29uQ2hhbmdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I9e3ZhbHVlIGFzIFJnYkNvbG9yfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICBjYXNlICdyZ2JhJzpcbiAgICAgICAgICAgICAgICBpZiAoYXNfc3RyaW5nKSB7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgICAgICA8UmdiYVN0cmluZ0NvbG9yUGlja2VyXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e29uQ2hhbmdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yPXt2YWx1ZSBhcyBzdHJpbmd9XG4gICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgICAgICA8UmdiYUNvbG9yUGlja2VyXG4gICAgICAgICAgICAgICAgICAgICAgICBvbkNoYW5nZT17b25DaGFuZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICBjb2xvcj17dmFsdWUgYXMgUmdiYUNvbG9yfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICBjYXNlICdoc2wnOlxuICAgICAgICAgICAgICAgIGlmIChhc19zdHJpbmcpIHtcbiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgICAgICAgICAgICAgIDxIc2xTdHJpbmdDb2xvclBpY2tlclxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXtvbkNoYW5nZX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb2xvcj17dmFsdWUgYXMgc3RyaW5nfVxuICAgICAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgICAgICAgICAgPEhzbENvbG9yUGlja2VyXG4gICAgICAgICAgICAgICAgICAgICAgICBvbkNoYW5nZT17b25DaGFuZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICBjb2xvcj17dmFsdWUgYXMgSHNsQ29sb3J9XG4gICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIGNhc2UgJ2hzbGEnOlxuICAgICAgICAgICAgICAgIGlmIChhc19zdHJpbmcpIHtcbiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgICAgICAgICAgICAgIDxIc2xhU3RyaW5nQ29sb3JQaWNrZXJcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBvbkNoYW5nZT17b25DaGFuZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I9e3ZhbHVlIGFzIHN0cmluZ31cbiAgICAgICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgIDxIc2xhQ29sb3JQaWNrZXJcbiAgICAgICAgICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXtvbkNoYW5nZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yPXt2YWx1ZSBhcyBIc2xhQ29sb3J9XG4gICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIGNhc2UgJ2hzdic6XG4gICAgICAgICAgICAgICAgaWYgKGFzX3N0cmluZykge1xuICAgICAgICAgICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgICAgICAgICAgPEhzdlN0cmluZ0NvbG9yUGlja2VyXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e29uQ2hhbmdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yPXt2YWx1ZSBhcyBzdHJpbmd9XG4gICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgICAgICA8SHN2Q29sb3JQaWNrZXJcbiAgICAgICAgICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXtvbkNoYW5nZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yPXt2YWx1ZSBhcyBIc3ZDb2xvcn1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgY2FzZSAnaHN2YSc6XG4gICAgICAgICAgICAgICAgaWYgKGFzX3N0cmluZykge1xuICAgICAgICAgICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgICAgICAgICAgPEhzdmFTdHJpbmdDb2xvclBpY2tlclxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXtvbkNoYW5nZX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb2xvcj17dmFsdWUgYXMgc3RyaW5nfVxuICAgICAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgICAgICAgICAgPEhzdmFDb2xvclBpY2tlclxuICAgICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e29uQ2hhbmdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I9e3ZhbHVlIGFzIEhzdmFDb2xvcn1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgY2FzZSAnaGV4JzpcbiAgICAgICAgICAgIGRlZmF1bHQ6XG4gICAgICAgICAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgICAgICAgICAgPEhleENvbG9yUGlja2VyXG4gICAgICAgICAgICAgICAgICAgICAgICBvbkNoYW5nZT17b25DaGFuZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICBjb2xvcj17dmFsdWUgYXMgc3RyaW5nfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICk7XG4gICAgICAgIH1cbiAgICB9LCBbXG4gICAgICAgIHR5cGUsXG4gICAgICAgIHZhbHVlLFxuICAgICAgICB1cGRhdGVBc3BlY3RzLFxuICAgICAgICB0b2dnbGVfb25fY2hvb3NlLFxuICAgICAgICB0b2dnbGVfb25fY2hvb3NlX2RlbGF5LFxuICAgICAgICBhc19zdHJpbmcsXG4gICAgXSk7XG5cbiAgICBjb25zdCB0b2dnbGVCdXR0b24gPSB1c2VNZW1vKCgpID0+IHtcbiAgICAgICAgaWYgKHRvZ2dsZV9idXR0b25fY29sb3IpIHtcbiAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgPGRpdlxuICAgICAgICAgICAgICAgICAgICBjbGFzc05hbWU9XCJ0b2dnbGUtYnV0dG9uLWNvbG9yXCJcbiAgICAgICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgICAgICBzdHlsZT17e2JhY2tncm91bmRDb2xvcjogdmFsdWV9fVxuICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB0b2dnbGVfYnV0dG9uO1xuICAgIH0sIFt0b2dnbGVfYnV0dG9uLCB0b2dnbGVfYnV0dG9uX2NvbG9yLCB2YWx1ZV0pO1xuXG4gICAgY29uc3Qgb25Ub2dnbGUgPSB1c2VDYWxsYmFjaygoKSA9PiB7XG4gICAgICAgIHVwZGF0ZUFzcGVjdHMoe2FjdGl2ZTogIWFjdGl2ZX0pO1xuICAgIH0sIFthY3RpdmUsIHVwZGF0ZUFzcGVjdHNdKTtcblxuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXYgaWQ9e2lkZW50aXR5fSBjbGFzc05hbWU9e2NsYXNzTmFtZX0+XG4gICAgICAgICAgICB7dG9nZ2xlYWJsZSAmJiAoXG4gICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJkYXp6bGVyLWNvbG9yLXBpY2tlci10b2dnbGVcIiBvbkNsaWNrPXtvblRvZ2dsZX0+XG4gICAgICAgICAgICAgICAgICAgIHt0b2dnbGVCdXR0b259XG4gICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9e2Nzc30gc3R5bGU9e3N0eWxpbmd9PlxuICAgICAgICAgICAgICAgIHtwaWNrZXJ9XG4gICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgPC9kaXY+XG4gICAgKTtcbn07XG5cbkNvbG9yUGlja2VyLmRlZmF1bHRQcm9wcyA9IHtcbiAgICB0eXBlOiAnaGV4JyxcbiAgICB0b2dnbGVfYnV0dG9uOiAn8J+OqCcsXG4gICAgdG9nZ2xlYWJsZTogdHJ1ZSxcbiAgICB0b2dnbGVfb25fY2hvb3NlOiB0cnVlLFxuICAgIHRvZ2dsZV9vbl9jaG9vc2VfZGVsYXk6IDI1MDAsXG4gICAgdG9nZ2xlX2RpcmVjdGlvbjogJ3RvcC1sZWZ0Jyxcbn07XG5cbmV4cG9ydCBkZWZhdWx0IENvbG9yUGlja2VyO1xuIiwiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7am9pbiwgY29uY2F0fSBmcm9tICdyYW1kYSc7XG5pbXBvcnQge0NhcmV0UHJvcHMsIERyYXdlclByb3BzfSBmcm9tICcuLi90eXBlcyc7XG5cbmNvbnN0IENhcmV0ID0gKHtzaWRlLCBvcGVuZWR9OiBDYXJldFByb3BzKSA9PiB7XG4gICAgc3dpdGNoIChzaWRlKSB7XG4gICAgICAgIGNhc2UgJ3RvcCc6XG4gICAgICAgICAgICByZXR1cm4gb3BlbmVkID8gPHNwYW4+JiM5NjUwOzwvc3Bhbj4gOiA8c3Bhbj4mIzk2NjA7PC9zcGFuPjtcbiAgICAgICAgY2FzZSAncmlnaHQnOlxuICAgICAgICAgICAgcmV0dXJuIG9wZW5lZCA/IDxzcGFuPiYjOTY1Njs8L3NwYW4+IDogPHNwYW4+JiM5NjY2Ozwvc3Bhbj47XG4gICAgICAgIGNhc2UgJ2xlZnQnOlxuICAgICAgICAgICAgcmV0dXJuIG9wZW5lZCA/IDxzcGFuPiYjOTY2Njs8L3NwYW4+IDogPHNwYW4+JiM5NjU2Ozwvc3Bhbj47XG4gICAgICAgIGNhc2UgJ2JvdHRvbSc6XG4gICAgICAgICAgICByZXR1cm4gb3BlbmVkID8gPHNwYW4+JiM5NjYwOzwvc3Bhbj4gOiA8c3Bhbj4mIzk2NTA7PC9zcGFuPjtcbiAgICAgICAgZGVmYXVsdDpcbiAgICAgICAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbn07XG5cbi8qKlxuICogRHJhdyBjb250ZW50IGZyb20gdGhlIHNpZGVzIG9mIHRoZSBzY3JlZW4uXG4gKlxuICogOkNTUzpcbiAqXG4gKiAgICAgLSBgYGRhenpsZXItZXh0cmEtZHJhd2VyYGBcbiAqICAgICAtIGBgZHJhd2VyLWNvbnRlbnRgYFxuICogICAgIC0gYGBkcmF3ZXItY29udHJvbGBgXG4gKiAgICAgLSBgYHZlcnRpY2FsYGBcbiAqICAgICAtIGBgaG9yaXpvbnRhbGBgXG4gKiAgICAgLSBgYHJpZ2h0YGBcbiAqICAgICAtIGBgYm90dG9tYGBcbiAqL1xuY29uc3QgRHJhd2VyID0gKHByb3BzOiBEcmF3ZXJQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtjbGFzc19uYW1lLCBpZGVudGl0eSwgc3R5bGUsIGNoaWxkcmVuLCBvcGVuZWQsIHNpZGUsIHVwZGF0ZUFzcGVjdHN9ID1cbiAgICAgICAgcHJvcHM7XG5cbiAgICBjb25zdCBjc3M6IHN0cmluZ1tdID0gW3NpZGVdO1xuXG4gICAgaWYgKHNpZGUgPT09ICd0b3AnIHx8IHNpZGUgPT09ICdib3R0b20nKSB7XG4gICAgICAgIGNzcy5wdXNoKCdob3Jpem9udGFsJyk7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgY3NzLnB1c2goJ3ZlcnRpY2FsJyk7XG4gICAgfVxuXG4gICAgcmV0dXJuIChcbiAgICAgICAgPGRpdlxuICAgICAgICAgICAgY2xhc3NOYW1lPXtqb2luKCcgJywgY29uY2F0KGNzcywgW2NsYXNzX25hbWVdKSl9XG4gICAgICAgICAgICBpZD17aWRlbnRpdHl9XG4gICAgICAgICAgICBzdHlsZT17c3R5bGV9XG4gICAgICAgID5cbiAgICAgICAgICAgIHtvcGVuZWQgJiYgKFxuICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPXtqb2luKCcgJywgY29uY2F0KGNzcywgWydkcmF3ZXItY29udGVudCddKSl9PlxuICAgICAgICAgICAgICAgICAgICB7Y2hpbGRyZW59XG4gICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgICAgPGRpdlxuICAgICAgICAgICAgICAgIGNsYXNzTmFtZT17am9pbignICcsIGNvbmNhdChjc3MsIFsnZHJhd2VyLWNvbnRyb2wnXSkpfVxuICAgICAgICAgICAgICAgIG9uQ2xpY2s9eygpID0+IHVwZGF0ZUFzcGVjdHMoe29wZW5lZDogIW9wZW5lZH0pfVxuICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgIDxDYXJldCBvcGVuZWQ9e29wZW5lZH0gc2lkZT17c2lkZX0gLz5cbiAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICA8L2Rpdj5cbiAgICApO1xufTtcblxuRHJhd2VyLmRlZmF1bHRQcm9wcyA9IHtcbiAgICBzaWRlOiAndG9wJyxcbn07XG5cbmV4cG9ydCBkZWZhdWx0IERyYXdlcjtcbiIsImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQge3RpbWVzdGFtcFByb3B9IGZyb20gJ2NvbW1vbnMnO1xuaW1wb3J0IHttZXJnZX0gZnJvbSAncmFtZGEnO1xuaW1wb3J0IHtOb3RpY2VQcm9wc30gZnJvbSAnLi4vdHlwZXMnO1xuXG4vKipcbiAqIEJyb3dzZXIgbm90aWZpY2F0aW9ucyB3aXRoIHBlcm1pc3Npb25zIGhhbmRsaW5nLlxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBOb3RpY2UgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQ8Tm90aWNlUHJvcHM+IHtcbiAgICBjb25zdHJ1Y3Rvcihwcm9wcykge1xuICAgICAgICBzdXBlcihwcm9wcyk7XG4gICAgICAgIHRoaXMuc3RhdGUgPSB7XG4gICAgICAgICAgICBsYXN0TWVzc2FnZTogcHJvcHMuYm9keSxcbiAgICAgICAgICAgIG5vdGlmaWNhdGlvbjogbnVsbCxcbiAgICAgICAgfTtcbiAgICAgICAgdGhpcy5vblBlcm1pc3Npb24gPSB0aGlzLm9uUGVybWlzc2lvbi5iaW5kKHRoaXMpO1xuICAgIH1cblxuICAgIGNvbXBvbmVudERpZE1vdW50KCkge1xuICAgICAgICBjb25zdCB7dXBkYXRlQXNwZWN0c30gPSB0aGlzLnByb3BzO1xuICAgICAgICBpZiAoISgnTm90aWZpY2F0aW9uJyBpbiB3aW5kb3cpICYmIHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMoe3Blcm1pc3Npb246ICd1bnN1cHBvcnRlZCd9KTtcbiAgICAgICAgfSBlbHNlIGlmIChOb3RpZmljYXRpb24ucGVybWlzc2lvbiA9PT0gJ2RlZmF1bHQnKSB7XG4gICAgICAgICAgICBOb3RpZmljYXRpb24ucmVxdWVzdFBlcm1pc3Npb24oKS50aGVuKHRoaXMub25QZXJtaXNzaW9uKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHRoaXMub25QZXJtaXNzaW9uKHdpbmRvdy5Ob3RpZmljYXRpb24ucGVybWlzc2lvbik7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBjb21wb25lbnREaWRVcGRhdGUocHJldlByb3BzKSB7XG4gICAgICAgIGlmICghcHJldlByb3BzLmRpc3BsYXllZCAmJiB0aGlzLnByb3BzLmRpc3BsYXllZCkge1xuICAgICAgICAgICAgdGhpcy5zZW5kTm90aWZpY2F0aW9uKHRoaXMucHJvcHMucGVybWlzc2lvbik7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBzZW5kTm90aWZpY2F0aW9uKHBlcm1pc3Npb24pIHtcbiAgICAgICAgY29uc3Qge1xuICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyxcbiAgICAgICAgICAgIGJvZHksXG4gICAgICAgICAgICB0aXRsZSxcbiAgICAgICAgICAgIGljb24sXG4gICAgICAgICAgICByZXF1aXJlX2ludGVyYWN0aW9uLFxuICAgICAgICAgICAgbGFuZyxcbiAgICAgICAgICAgIGJhZGdlLFxuICAgICAgICAgICAgdGFnLFxuICAgICAgICAgICAgaW1hZ2UsXG4gICAgICAgICAgICB2aWJyYXRlLFxuICAgICAgICB9ID0gdGhpcy5wcm9wcztcbiAgICAgICAgaWYgKHBlcm1pc3Npb24gPT09ICdncmFudGVkJykge1xuICAgICAgICAgICAgY29uc3Qgb3B0aW9ucyA9IHtcbiAgICAgICAgICAgICAgICByZXF1aXJlSW50ZXJhY3Rpb246IHJlcXVpcmVfaW50ZXJhY3Rpb24sXG4gICAgICAgICAgICAgICAgYm9keSxcbiAgICAgICAgICAgICAgICBpY29uLFxuICAgICAgICAgICAgICAgIGxhbmcsXG4gICAgICAgICAgICAgICAgYmFkZ2UsXG4gICAgICAgICAgICAgICAgdGFnLFxuICAgICAgICAgICAgICAgIGltYWdlLFxuICAgICAgICAgICAgICAgIHZpYnJhdGUsXG4gICAgICAgICAgICB9O1xuICAgICAgICAgICAgY29uc3Qgbm90aWZpY2F0aW9uID0gbmV3IE5vdGlmaWNhdGlvbih0aXRsZSwgb3B0aW9ucyk7XG4gICAgICAgICAgICBub3RpZmljYXRpb24ub25jbGljayA9ICgpID0+IHtcbiAgICAgICAgICAgICAgICBpZiAodXBkYXRlQXNwZWN0cykge1xuICAgICAgICAgICAgICAgICAgICB1cGRhdGVBc3BlY3RzKFxuICAgICAgICAgICAgICAgICAgICAgICAgbWVyZ2UoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAge2Rpc3BsYXllZDogZmFsc2V9LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpbWVzdGFtcFByb3AoJ2NsaWNrcycsIHRoaXMucHJvcHMuY2xpY2tzICsgMSlcbiAgICAgICAgICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9O1xuICAgICAgICAgICAgbm90aWZpY2F0aW9uLm9uY2xvc2UgPSAoKSA9PiB7XG4gICAgICAgICAgICAgICAgaWYgKHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyhcbiAgICAgICAgICAgICAgICAgICAgICAgIG1lcmdlKFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtkaXNwbGF5ZWQ6IGZhbHNlfSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aW1lc3RhbXBQcm9wKCdjbG9zZXMnLCB0aGlzLnByb3BzLmNsb3NlcyArIDEpXG4gICAgICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIG9uUGVybWlzc2lvbihwZXJtaXNzaW9uKSB7XG4gICAgICAgIGNvbnN0IHtkaXNwbGF5ZWQsIHVwZGF0ZUFzcGVjdHN9ID0gdGhpcy5wcm9wcztcbiAgICAgICAgaWYgKHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMoe3Blcm1pc3Npb259KTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoZGlzcGxheWVkKSB7XG4gICAgICAgICAgICB0aGlzLnNlbmROb3RpZmljYXRpb24ocGVybWlzc2lvbik7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICByZW5kZXIoKSB7XG4gICAgICAgIHJldHVybiBudWxsO1xuICAgIH1cblxuICAgIHN0YXRpYyBkZWZhdWx0UHJvcHM6IHtcbiAgICAgICAgcmVxdWlyZV9pbnRlcmFjdGlvbjogZmFsc2U7XG4gICAgICAgIGNsaWNrczogMDtcbiAgICAgICAgY2xpY2tzX3RpbWVzdGFtcDogLTE7XG4gICAgICAgIGNsb3NlczogMDtcbiAgICAgICAgY2xvc2VzX3RpbWVzdGFtcDogLTE7XG4gICAgfTtcbn1cbiIsImltcG9ydCBSZWFjdCwge3VzZUVmZmVjdCwgdXNlU3RhdGV9IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7RGF6emxlclByb3BzfSBmcm9tICcuLi8uLi8uLi9jb21tb25zL2pzL3R5cGVzJztcblxuLyoqXG4gKiBMaXN0IG9mIGxpbmtzIHRvIG90aGVyIHBhZ2UgaW4gdGhlIGFwcC5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS1wYWdlLW1hcGBgXG4gKi9cbmNvbnN0IFBhZ2VNYXAgPSAocHJvcHM6IERhenpsZXJQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtjbGFzc19uYW1lLCBzdHlsZSwgaWRlbnRpdHl9ID0gcHJvcHM7XG4gICAgY29uc3QgW3BhZ2VNYXAsIHNldFBhZ2VNYXBdID0gdXNlU3RhdGUobnVsbCk7XG5cbiAgICB1c2VFZmZlY3QoKCkgPT4ge1xuICAgICAgICAvLyBAdHMtaWdub3JlXG4gICAgICAgIGZldGNoKGAke3dpbmRvdy5kYXp6bGVyX2Jhc2VfdXJsfS9kYXp6bGVyL3BhZ2UtbWFwYCkudGhlbigocmVwKSA9PlxuICAgICAgICAgICAgcmVwLmpzb24oKS50aGVuKHNldFBhZ2VNYXApXG4gICAgICAgICk7XG4gICAgfSwgW10pO1xuXG4gICAgcmV0dXJuIChcbiAgICAgICAgPHVsIGNsYXNzTmFtZT17Y2xhc3NfbmFtZX0gc3R5bGU9e3N0eWxlfSBpZD17aWRlbnRpdHl9PlxuICAgICAgICAgICAge3BhZ2VNYXAgJiZcbiAgICAgICAgICAgICAgICBwYWdlTWFwLm1hcCgocGFnZSkgPT4gKFxuICAgICAgICAgICAgICAgICAgICA8bGkga2V5PXtwYWdlLm5hbWV9PlxuICAgICAgICAgICAgICAgICAgICAgICAgPGEgaHJlZj17cGFnZS51cmx9PntwYWdlLnRpdGxlfTwvYT5cbiAgICAgICAgICAgICAgICAgICAgPC9saT5cbiAgICAgICAgICAgICAgICApKX1cbiAgICAgICAgPC91bD5cbiAgICApO1xufTtcblxuUGFnZU1hcC5kZWZhdWx0UHJvcHMgPSB7fTtcblxuZXhwb3J0IGRlZmF1bHQgUGFnZU1hcDtcbiIsImltcG9ydCBSZWFjdCwge21lbW99IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7cmFuZ2UsIGpvaW59IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7UGFnZXJQYWdlUHJvcHMsIFBhZ2VyUHJvcHMsIFBhZ2VyU3RhdGV9IGZyb20gJy4uL3R5cGVzJztcblxuY29uc3Qgc3RhcnRPZmZzZXQgPSAocGFnZSwgaXRlbVBlclBhZ2UpID0+XG4gICAgKHBhZ2UgLSAxKSAqIChwYWdlID4gMSA/IGl0ZW1QZXJQYWdlIDogMCk7XG5cbmNvbnN0IGVuZE9mZnNldCA9IChzdGFydCwgaXRlbVBlclBhZ2UsIHBhZ2UsIHRvdGFsLCBsZWZ0T3ZlcikgPT5cbiAgICBwYWdlICE9PSB0b3RhbFxuICAgICAgICA/IHN0YXJ0ICsgaXRlbVBlclBhZ2VcbiAgICAgICAgOiBsZWZ0T3ZlciAhPT0gMFxuICAgICAgICA/IHN0YXJ0ICsgbGVmdE92ZXJcbiAgICAgICAgOiBzdGFydCArIGl0ZW1QZXJQYWdlO1xuXG5jb25zdCBzaG93TGlzdCA9IChwYWdlLCB0b3RhbCwgbikgPT4ge1xuICAgIGlmICh0b3RhbCA+IG4pIHtcbiAgICAgICAgY29uc3QgbWlkZGxlID0gTWF0aC5mbG9vcihuIC8gMik7XG4gICAgICAgIGNvbnN0IGZpcnN0ID1cbiAgICAgICAgICAgIHBhZ2UgPj0gdG90YWwgLSBtaWRkbGVcbiAgICAgICAgICAgICAgICA/IHRvdGFsIC0gbiArIDFcbiAgICAgICAgICAgICAgICA6IHBhZ2UgPiBtaWRkbGVcbiAgICAgICAgICAgICAgICA/IHBhZ2UgLSBtaWRkbGVcbiAgICAgICAgICAgICAgICA6IDE7XG4gICAgICAgIGNvbnN0IGxhc3QgPSBwYWdlIDwgdG90YWwgLSBtaWRkbGUgPyBmaXJzdCArIG4gOiB0b3RhbCArIDE7XG4gICAgICAgIHJldHVybiByYW5nZShmaXJzdCwgbGFzdCk7XG4gICAgfVxuICAgIHJldHVybiByYW5nZSgxLCB0b3RhbCArIDEpO1xufTtcblxuY29uc3QgUGFnZSA9IG1lbW8oXG4gICAgKHtzdHlsZSwgY2xhc3NfbmFtZSwgb25fY2hhbmdlLCB0ZXh0LCBwYWdlLCBjdXJyZW50fTogUGFnZXJQYWdlUHJvcHMpID0+IChcbiAgICAgICAgPHNwYW5cbiAgICAgICAgICAgIHN0eWxlPXtzdHlsZX1cbiAgICAgICAgICAgIGNsYXNzTmFtZT17YCR7Y2xhc3NfbmFtZX0ke2N1cnJlbnQgPyAnIGN1cnJlbnQtcGFnZScgOiAnJ31gfVxuICAgICAgICAgICAgb25DbGljaz17KCkgPT4gIWN1cnJlbnQgJiYgb25fY2hhbmdlKHBhZ2UpfVxuICAgICAgICA+XG4gICAgICAgICAgICB7dGV4dCB8fCBwYWdlfVxuICAgICAgICA8L3NwYW4+XG4gICAgKVxuKTtcblxuLyoqXG4gKiBQYWdpbmcgZm9yIGRhenpsZXIgYXBwcy5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS1wYWdlcmBgXG4gKiAgICAgLSBgYHBhZ2VgYFxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBQYWdlciBleHRlbmRzIFJlYWN0LkNvbXBvbmVudDxQYWdlclByb3BzLCBQYWdlclN0YXRlPiB7XG4gICAgY29uc3RydWN0b3IocHJvcHMpIHtcbiAgICAgICAgc3VwZXIocHJvcHMpO1xuICAgICAgICB0aGlzLnN0YXRlID0ge1xuICAgICAgICAgICAgY3VycmVudF9wYWdlOiBudWxsLFxuICAgICAgICAgICAgc3RhcnRfb2Zmc2V0OiBudWxsLFxuICAgICAgICAgICAgZW5kX29mZnNldDogbnVsbCxcbiAgICAgICAgICAgIHBhZ2VzOiBbXSxcbiAgICAgICAgICAgIHRvdGFsX3BhZ2VzOiBNYXRoLmNlaWwocHJvcHMudG90YWxfaXRlbXMgLyBwcm9wcy5pdGVtc19wZXJfcGFnZSksXG4gICAgICAgIH07XG4gICAgICAgIHRoaXMub25DaGFuZ2VQYWdlID0gdGhpcy5vbkNoYW5nZVBhZ2UuYmluZCh0aGlzKTtcbiAgICB9XG5cbiAgICBVTlNBRkVfY29tcG9uZW50V2lsbE1vdW50KCkge1xuICAgICAgICB0aGlzLm9uQ2hhbmdlUGFnZSh0aGlzLnByb3BzLmN1cnJlbnRfcGFnZSk7XG4gICAgfVxuXG4gICAgb25DaGFuZ2VQYWdlKHBhZ2UpIHtcbiAgICAgICAgY29uc3Qge2l0ZW1zX3Blcl9wYWdlLCB0b3RhbF9pdGVtcywgdXBkYXRlQXNwZWN0cywgcGFnZXNfZGlzcGxheWVkfSA9XG4gICAgICAgICAgICB0aGlzLnByb3BzO1xuICAgICAgICBjb25zdCB7dG90YWxfcGFnZXN9ID0gdGhpcy5zdGF0ZTtcblxuICAgICAgICBjb25zdCBzdGFydF9vZmZzZXQgPSBzdGFydE9mZnNldChwYWdlLCBpdGVtc19wZXJfcGFnZSk7XG4gICAgICAgIGNvbnN0IGxlZnRPdmVyID0gdG90YWxfaXRlbXMgJSBpdGVtc19wZXJfcGFnZTtcblxuICAgICAgICBjb25zdCBlbmRfb2Zmc2V0ID0gZW5kT2Zmc2V0KFxuICAgICAgICAgICAgc3RhcnRfb2Zmc2V0LFxuICAgICAgICAgICAgaXRlbXNfcGVyX3BhZ2UsXG4gICAgICAgICAgICBwYWdlLFxuICAgICAgICAgICAgdG90YWxfcGFnZXMsXG4gICAgICAgICAgICBsZWZ0T3ZlclxuICAgICAgICApO1xuXG4gICAgICAgIGNvbnN0IHBheWxvYWQ6IFBhZ2VyU3RhdGUgPSB7XG4gICAgICAgICAgICBjdXJyZW50X3BhZ2U6IHBhZ2UsXG4gICAgICAgICAgICBzdGFydF9vZmZzZXQ6IHN0YXJ0X29mZnNldCxcbiAgICAgICAgICAgIGVuZF9vZmZzZXQ6IGVuZF9vZmZzZXQsXG4gICAgICAgICAgICBwYWdlczogc2hvd0xpc3QocGFnZSwgdG90YWxfcGFnZXMsIHBhZ2VzX2Rpc3BsYXllZCksXG4gICAgICAgIH07XG4gICAgICAgIHRoaXMuc2V0U3RhdGUocGF5bG9hZCk7XG5cbiAgICAgICAgaWYgKHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgICAgIGlmICh0aGlzLnN0YXRlLnRvdGFsX3BhZ2VzICE9PSB0aGlzLnByb3BzLnRvdGFsX3BhZ2VzKSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC50b3RhbF9wYWdlcyA9IHRoaXMuc3RhdGUudG90YWxfcGFnZXM7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICB1cGRhdGVBc3BlY3RzKHBheWxvYWQpO1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgVU5TQUZFX2NvbXBvbmVudFdpbGxSZWNlaXZlUHJvcHMocHJvcHMpIHtcbiAgICAgICAgaWYgKHByb3BzLmN1cnJlbnRfcGFnZSAhPT0gdGhpcy5zdGF0ZS5jdXJyZW50X3BhZ2UpIHtcbiAgICAgICAgICAgIHRoaXMub25DaGFuZ2VQYWdlKHByb3BzLmN1cnJlbnRfcGFnZSk7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKHByb3BzLnRvdGFsX2l0ZW1zICE9PSB0aGlzLnByb3BzLnRvdGFsX2l0ZW1zKSB7XG4gICAgICAgICAgICBjb25zdCB0b3RhbF9wYWdlcyA9IE1hdGguY2VpbChcbiAgICAgICAgICAgICAgICBwcm9wcy50b3RhbF9pdGVtcyAvIHByb3BzLml0ZW1zX3Blcl9wYWdlXG4gICAgICAgICAgICApO1xuICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZSh7XG4gICAgICAgICAgICAgICAgdG90YWxfcGFnZXMsXG4gICAgICAgICAgICAgICAgcGFnZXM6IHNob3dMaXN0KFxuICAgICAgICAgICAgICAgICAgICBwcm9wcy5jdXJyZW50X3BhZ2UsXG4gICAgICAgICAgICAgICAgICAgIHRvdGFsX3BhZ2VzLFxuICAgICAgICAgICAgICAgICAgICBwcm9wcy5wYWdlc19kaXNwbGF5ZWRcbiAgICAgICAgICAgICAgICApLFxuICAgICAgICAgICAgfSk7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICByZW5kZXIoKSB7XG4gICAgICAgIGNvbnN0IHtjdXJyZW50X3BhZ2UsIHBhZ2VzLCB0b3RhbF9wYWdlc30gPSB0aGlzLnN0YXRlO1xuICAgICAgICBjb25zdCB7XG4gICAgICAgICAgICBjbGFzc19uYW1lLFxuICAgICAgICAgICAgaWRlbnRpdHksXG4gICAgICAgICAgICBwYWdlX3N0eWxlLFxuICAgICAgICAgICAgcGFnZV9jbGFzc19uYW1lLFxuICAgICAgICAgICAgcGFnZXNfZGlzcGxheWVkLFxuICAgICAgICAgICAgbmV4dF9sYWJlbCxcbiAgICAgICAgICAgIHByZXZpb3VzX2xhYmVsLFxuICAgICAgICB9ID0gdGhpcy5wcm9wcztcblxuICAgICAgICBjb25zdCBjc3M6IHN0cmluZ1tdID0gWydwYWdlJ107XG4gICAgICAgIGlmIChwYWdlX2NsYXNzX25hbWUpIHtcbiAgICAgICAgICAgIGNzcy5wdXNoKHBhZ2VfY2xhc3NfbmFtZSk7XG4gICAgICAgIH1cbiAgICAgICAgY29uc3QgcGFnZUNzcyA9IGpvaW4oJyAnLCBjc3MpO1xuXG4gICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT17Y2xhc3NfbmFtZX0gaWQ9e2lkZW50aXR5fT5cbiAgICAgICAgICAgICAgICB7Y3VycmVudF9wYWdlID4gMSAmJiAoXG4gICAgICAgICAgICAgICAgICAgIDxQYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICBwYWdlPXtjdXJyZW50X3BhZ2UgLSAxfVxuICAgICAgICAgICAgICAgICAgICAgICAgdGV4dD17cHJldmlvdXNfbGFiZWx9XG4gICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT17cGFnZV9zdHlsZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGNsYXNzX25hbWU9e3BhZ2VDc3N9XG4gICAgICAgICAgICAgICAgICAgICAgICBvbl9jaGFuZ2U9e3RoaXMub25DaGFuZ2VQYWdlfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICl9XG4gICAgICAgICAgICAgICAge2N1cnJlbnRfcGFnZSArIDEgPj0gcGFnZXNfZGlzcGxheWVkICYmXG4gICAgICAgICAgICAgICAgICAgIHRvdGFsX3BhZ2VzID4gcGFnZXNfZGlzcGxheWVkICYmIChcbiAgICAgICAgICAgICAgICAgICAgICAgIDw+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgPFBhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFnZT17MX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGV4dD17JzEnfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT17cGFnZV9zdHlsZX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2xhc3NfbmFtZT17cGFnZUNzc31cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fY2hhbmdlPXt0aGlzLm9uQ2hhbmdlUGFnZX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxQYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhZ2U9ey0xfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0ZXh0PXsnLi4uJ31cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fY2hhbmdlPXsoKSA9PiBudWxsfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjbGFzc19uYW1lPXtgJHtwYWdlQ3NzfSBtb3JlLXBhZ2VzYH1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgPC8+XG4gICAgICAgICAgICAgICAgICAgICl9XG4gICAgICAgICAgICAgICAge3BhZ2VzLm1hcCgoZSkgPT4gKFxuICAgICAgICAgICAgICAgICAgICA8UGFnZVxuICAgICAgICAgICAgICAgICAgICAgICAgcGFnZT17ZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGtleT17YHBhZ2UtJHtlfWB9XG4gICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT17cGFnZV9zdHlsZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGNsYXNzX25hbWU9e3BhZ2VDc3N9XG4gICAgICAgICAgICAgICAgICAgICAgICBvbl9jaGFuZ2U9e3RoaXMub25DaGFuZ2VQYWdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgY3VycmVudD17ZSA9PT0gY3VycmVudF9wYWdlfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICkpfVxuICAgICAgICAgICAgICAgIHt0b3RhbF9wYWdlcyAtIGN1cnJlbnRfcGFnZSA+PSBNYXRoLmNlaWwocGFnZXNfZGlzcGxheWVkIC8gMikgJiZcbiAgICAgICAgICAgICAgICAgICAgdG90YWxfcGFnZXMgPiBwYWdlc19kaXNwbGF5ZWQgJiYgKFxuICAgICAgICAgICAgICAgICAgICAgICAgPD5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8UGFnZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYWdlPXstMX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGV4dD17Jy4uLid9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNsYXNzX25hbWU9e2Ake3BhZ2VDc3N9IG1vcmUtcGFnZXNgfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvbl9jaGFuZ2U9eygpID0+IG51bGx9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8UGFnZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYWdlPXt0b3RhbF9wYWdlc31cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3R5bGU9e3BhZ2Vfc3R5bGV9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNsYXNzX25hbWU9e3BhZ2VDc3N9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX2NoYW5nZT17dGhpcy5vbkNoYW5nZVBhZ2V9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICAgICAgICAgIDwvPlxuICAgICAgICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICAgIHtjdXJyZW50X3BhZ2UgPCB0b3RhbF9wYWdlcyAmJiAoXG4gICAgICAgICAgICAgICAgICAgIDxQYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICBwYWdlPXtjdXJyZW50X3BhZ2UgKyAxfVxuICAgICAgICAgICAgICAgICAgICAgICAgdGV4dD17bmV4dF9sYWJlbH1cbiAgICAgICAgICAgICAgICAgICAgICAgIHN0eWxlPXtwYWdlX3N0eWxlfVxuICAgICAgICAgICAgICAgICAgICAgICAgY2xhc3NfbmFtZT17cGFnZUNzc31cbiAgICAgICAgICAgICAgICAgICAgICAgIG9uX2NoYW5nZT17dGhpcy5vbkNoYW5nZVBhZ2V9XG4gICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgKX1cbiAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICApO1xuICAgIH1cblxuICAgIHN0YXRpYyBkZWZhdWx0UHJvcHMgPSB7XG4gICAgICAgIGN1cnJlbnRfcGFnZTogMSxcbiAgICAgICAgaXRlbXNfcGVyX3BhZ2U6IDEwLFxuICAgICAgICBwYWdlc19kaXNwbGF5ZWQ6IDEwLFxuICAgICAgICBuZXh0X2xhYmVsOiAnbmV4dCcsXG4gICAgICAgIHByZXZpb3VzX2xhYmVsOiAncHJldmlvdXMnLFxuICAgIH07XG59XG4iLCJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtQb3BVcFByb3BzfSBmcm9tICcuLi90eXBlcyc7XG5cbmZ1bmN0aW9uIGdldE1vdXNlWChlLCBwb3B1cCkge1xuICAgIHJldHVybiAoXG4gICAgICAgIGUuY2xpZW50WCAtXG4gICAgICAgIGUudGFyZ2V0LmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLmxlZnQgLVxuICAgICAgICBwb3B1cC5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKS53aWR0aCAvIDJcbiAgICApO1xufVxuXG50eXBlIFBvcFVwU3RhdGUgPSB7XG4gICAgcG9zPzogbnVtYmVyO1xufTtcblxuLyoqXG4gKiBXcmFwcyBhIGNvbXBvbmVudC90ZXh0IHRvIHJlbmRlciBhIHBvcHVwIHdoZW4gaG92ZXJpbmdcbiAqIG92ZXIgdGhlIGNoaWxkcmVuIG9yIGNsaWNraW5nIG9uIGl0LlxuICpcbiAqIDpDU1M6XG4gKlxuICogICAgIC0gYGBkYXp6bGVyLWV4dHJhLXBvcC11cGBgXG4gKiAgICAgLSBgYHBvcHVwLWNvbnRlbnRgYFxuICogICAgIC0gYGB2aXNpYmxlYGBcbiAqL1xuZXhwb3J0IGRlZmF1bHQgY2xhc3MgUG9wVXAgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQ8UG9wVXBQcm9wcywgUG9wVXBTdGF0ZT4ge1xuICAgIHBvcHVwUmVmPzogYW55O1xuXG4gICAgY29uc3RydWN0b3IocHJvcHMpIHtcbiAgICAgICAgc3VwZXIocHJvcHMpO1xuICAgICAgICB0aGlzLnN0YXRlID0ge1xuICAgICAgICAgICAgcG9zOiBudWxsLFxuICAgICAgICB9O1xuICAgIH1cbiAgICByZW5kZXIoKSB7XG4gICAgICAgIGNvbnN0IHtcbiAgICAgICAgICAgIGNsYXNzX25hbWUsXG4gICAgICAgICAgICBzdHlsZSxcbiAgICAgICAgICAgIGlkZW50aXR5LFxuICAgICAgICAgICAgY2hpbGRyZW4sXG4gICAgICAgICAgICBjb250ZW50LFxuICAgICAgICAgICAgbW9kZSxcbiAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgICAgICBhY3RpdmUsXG4gICAgICAgICAgICBjb250ZW50X3N0eWxlLFxuICAgICAgICAgICAgY2hpbGRyZW5fc3R5bGUsXG4gICAgICAgIH0gPSB0aGlzLnByb3BzO1xuXG4gICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT17Y2xhc3NfbmFtZX0gc3R5bGU9e3N0eWxlfSBpZD17aWRlbnRpdHl9PlxuICAgICAgICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgICAgICAgICAgY2xhc3NOYW1lPXsncG9wdXAtY29udGVudCcgKyAoYWN0aXZlID8gJyB2aXNpYmxlJyA6ICcnKX1cbiAgICAgICAgICAgICAgICAgICAgc3R5bGU9e3tcbiAgICAgICAgICAgICAgICAgICAgICAgIC4uLihjb250ZW50X3N0eWxlIHx8IHt9KSxcbiAgICAgICAgICAgICAgICAgICAgICAgIGxlZnQ6IHRoaXMuc3RhdGUucG9zIHx8IDAsXG4gICAgICAgICAgICAgICAgICAgIH19XG4gICAgICAgICAgICAgICAgICAgIHJlZj17KHIpID0+ICh0aGlzLnBvcHVwUmVmID0gcil9XG4gICAgICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgICAgICB7Y29udGVudH1cbiAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICA8ZGl2XG4gICAgICAgICAgICAgICAgICAgIGNsYXNzTmFtZT1cInBvcHVwLWNoaWxkcmVuXCJcbiAgICAgICAgICAgICAgICAgICAgb25Nb3VzZUVudGVyPXsoZSkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKG1vZGUgPT09ICdob3ZlcicpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aGlzLnNldFN0YXRlKFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7cG9zOiBnZXRNb3VzZVgoZSwgdGhpcy5wb3B1cFJlZil9LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoKSA9PiB1cGRhdGVBc3BlY3RzKHthY3RpdmU6IHRydWV9KVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIH19XG4gICAgICAgICAgICAgICAgICAgIG9uTW91c2VMZWF2ZT17KCkgPT5cbiAgICAgICAgICAgICAgICAgICAgICAgIG1vZGUgPT09ICdob3ZlcicgJiYgdXBkYXRlQXNwZWN0cyh7YWN0aXZlOiBmYWxzZX0pXG4gICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgb25DbGljaz17KGUpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChtb2RlID09PSAnY2xpY2snKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAge3BvczogZ2V0TW91c2VYKGUsIHRoaXMucG9wdXBSZWYpfSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKCkgPT4gdXBkYXRlQXNwZWN0cyh7YWN0aXZlOiAhYWN0aXZlfSlcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICB9fVxuICAgICAgICAgICAgICAgICAgICBzdHlsZT17Y2hpbGRyZW5fc3R5bGV9XG4gICAgICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgICAgICB7Y2hpbGRyZW59XG4gICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgKTtcbiAgICB9XG5cbiAgICBzdGF0aWMgZGVmYXVsdFByb3BzID0ge1xuICAgICAgICBtb2RlOiAnaG92ZXInLFxuICAgICAgICBhY3RpdmU6IGZhbHNlLFxuICAgIH07XG59XG4iLCJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtEYXp6bGVyUHJvcHN9IGZyb20gJy4uLy4uLy4uL2NvbW1vbnMvanMvdHlwZXMnO1xuXG4vKipcbiAqIFNpbXBsZSBodG1sL2NzcyBzcGlubmVyLlxuICovXG5jb25zdCBTcGlubmVyID0gKHByb3BzOiBEYXp6bGVyUHJvcHMpID0+IHtcbiAgICBjb25zdCB7Y2xhc3NfbmFtZSwgc3R5bGUsIGlkZW50aXR5fSA9IHByb3BzO1xuICAgIHJldHVybiA8ZGl2IGlkPXtpZGVudGl0eX0gY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBzdHlsZT17c3R5bGV9IC8+O1xufTtcblxuZXhwb3J0IGRlZmF1bHQgU3Bpbm5lcjtcbiIsImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQge21lcmdlQWxsfSBmcm9tICdyYW1kYSc7XG5pbXBvcnQge1N0aWNreVByb3BzfSBmcm9tICcuLi90eXBlcyc7XG5cbi8qKlxuICogQSBzaG9ydGhhbmQgY29tcG9uZW50IGZvciBhIHN0aWNreSBkaXYuXG4gKi9cbmNvbnN0IFN0aWNreSA9IChwcm9wczogU3RpY2t5UHJvcHMpID0+IHtcbiAgICBjb25zdCB7Y2xhc3NfbmFtZSwgaWRlbnRpdHksIHN0eWxlLCBjaGlsZHJlbiwgdG9wLCBsZWZ0LCByaWdodCwgYm90dG9tfSA9XG4gICAgICAgIHByb3BzO1xuICAgIGNvbnN0IHN0eWxlcyA9IG1lcmdlQWxsKFtzdHlsZSwge3RvcCwgbGVmdCwgcmlnaHQsIGJvdHRvbX1dKTtcbiAgICByZXR1cm4gKFxuICAgICAgICA8ZGl2IGNsYXNzTmFtZT17Y2xhc3NfbmFtZX0gaWQ9e2lkZW50aXR5fSBzdHlsZT17c3R5bGVzfT5cbiAgICAgICAgICAgIHtjaGlsZHJlbn1cbiAgICAgICAgPC9kaXY+XG4gICAgKTtcbn07XG5cbmV4cG9ydCBkZWZhdWx0IFN0aWNreTtcbiIsImltcG9ydCBSZWFjdCwge3VzZUVmZmVjdCwgdXNlTWVtbywgdXNlU3RhdGV9IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7am9pbn0gZnJvbSAncmFtZGEnO1xuaW1wb3J0IHtUb2FzdFByb3BzfSBmcm9tICcuLi90eXBlcyc7XG5cbi8qKlxuICogRGlzcGxheSBhIG1lc3NhZ2Ugb3ZlciB0aGUgdWkgdGhhdCB3aWxsIGRpc2FwcGVhcnMgYWZ0ZXIgYSBkZWxheS5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS10b2FzdGBgXG4gKiAgICAgLSBgYG9wZW5lZGBgXG4gKiAgICAgLSBgYHRvYXN0LWlubmVyYGBcbiAqICAgICAtIGBgdG9wYGBcbiAqICAgICAtIGBgdG9wLWxlZnRgYFxuICogICAgIC0gYGB0b3AtcmlnaHRgYFxuICogICAgIC0gYGBib3R0b21gYFxuICogICAgIC0gYGBib3R0b20tbGVmdGBgXG4gKiAgICAgLSBgYGJvdHRvbS1yaWdodGBgXG4gKiAgICAgLSBgYHJpZ2h0YGBcbiAqL1xuY29uc3QgVG9hc3QgPSAocHJvcHM6IFRvYXN0UHJvcHMpID0+IHtcbiAgICBjb25zdCB7XG4gICAgICAgIGNsYXNzX25hbWUsXG4gICAgICAgIHN0eWxlLFxuICAgICAgICBpZGVudGl0eSxcbiAgICAgICAgbWVzc2FnZSxcbiAgICAgICAgcG9zaXRpb24sXG4gICAgICAgIG9wZW5lZCxcbiAgICAgICAgZGVsYXksXG4gICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgfSA9IHByb3BzO1xuICAgIGNvbnN0IFtkaXNwbGF5ZWQsIHNldERpc3BsYXllZF0gPSB1c2VTdGF0ZShmYWxzZSk7XG5cbiAgICBjb25zdCBjc3MgPSB1c2VNZW1vKCgpID0+IHtcbiAgICAgICAgY29uc3QgYyA9IFtjbGFzc19uYW1lLCBwb3NpdGlvbl07XG4gICAgICAgIGlmIChvcGVuZWQpIHtcbiAgICAgICAgICAgIGMucHVzaCgnb3BlbmVkJyk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIGpvaW4oJyAnLCBjKTtcbiAgICB9LCBbY2xhc3NfbmFtZSwgb3BlbmVkLCBwb3NpdGlvbl0pO1xuICAgIHVzZUVmZmVjdCgoKSA9PiB7XG4gICAgICAgIGlmIChvcGVuZWQgJiYgIWRpc3BsYXllZCkge1xuICAgICAgICAgICAgc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyh7b3BlbmVkOiBmYWxzZX0pO1xuICAgICAgICAgICAgICAgIHNldERpc3BsYXllZChmYWxzZSk7XG4gICAgICAgICAgICB9LCBkZWxheSk7XG4gICAgICAgICAgICBzZXREaXNwbGF5ZWQodHJ1ZSk7XG4gICAgICAgIH1cbiAgICB9LCBbb3BlbmVkLCBkaXNwbGF5ZWQsIGRlbGF5XSk7XG5cbiAgICByZXR1cm4gKFxuICAgICAgICA8ZGl2IGNsYXNzTmFtZT17Y3NzfSBzdHlsZT17c3R5bGV9IGlkPXtpZGVudGl0eX0+XG4gICAgICAgICAgICB7bWVzc2FnZX1cbiAgICAgICAgPC9kaXY+XG4gICAgKTtcbn07XG5cblRvYXN0LmRlZmF1bHRQcm9wcyA9IHtcbiAgICBkZWxheTogMzAwMCxcbiAgICBwb3NpdGlvbjogJ3RvcCcsXG4gICAgb3BlbmVkOiB0cnVlLFxufTtcblxuZXhwb3J0IGRlZmF1bHQgVG9hc3Q7XG4iLCJpbXBvcnQgUmVhY3QsIHt1c2VNZW1vfSBmcm9tICdyZWFjdCc7XG5pbXBvcnQge2lzLCBqb2luLCBpbmNsdWRlcywgc3BsaXQsIHNsaWNlLCBjb25jYXQsIHdpdGhvdXR9IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7VHJlZVZpZXdJdGVtUHJvcHMsIFRyZWVWaWV3UHJvcHN9IGZyb20gJy4uL3R5cGVzJztcblxuY29uc3QgVHJlZVZpZXdFbGVtZW50ID0gKHtcbiAgICBsYWJlbCxcbiAgICBvbkNsaWNrLFxuICAgIGlkZW50aWZpZXIsXG4gICAgaXRlbXMsXG4gICAgbGV2ZWwsXG4gICAgc2VsZWN0ZWQsXG4gICAgZXhwYW5kZWRfaXRlbXMsXG4gICAgbmVzdF9pY29uX2V4cGFuZGVkLFxuICAgIG5lc3RfaWNvbl9jb2xsYXBzZWQsXG59OiBUcmVlVmlld0l0ZW1Qcm9wcykgPT4ge1xuICAgIGNvbnN0IGlzU2VsZWN0ZWQgPSB1c2VNZW1vKFxuICAgICAgICAoKSA9PiBzZWxlY3RlZCAmJiBpbmNsdWRlcyhpZGVudGlmaWVyLCBzZWxlY3RlZCksXG4gICAgICAgIFtzZWxlY3RlZCwgaWRlbnRpZmllcl1cbiAgICApO1xuICAgIGNvbnN0IGlzRXhwYW5kZWQgPSB1c2VNZW1vKFxuICAgICAgICAoKSA9PiBpbmNsdWRlcyhpZGVudGlmaWVyLCBleHBhbmRlZF9pdGVtcyksXG4gICAgICAgIFtleHBhbmRlZF9pdGVtcywgZXhwYW5kZWRfaXRlbXNdXG4gICAgKTtcbiAgICBjb25zdCBjc3MgPSBbJ3RyZWUtaXRlbS1sYWJlbCcsIGBsZXZlbC0ke2xldmVsfWBdO1xuICAgIGlmIChpc1NlbGVjdGVkKSB7XG4gICAgICAgIGNzcy5wdXNoKCdzZWxlY3RlZCcpO1xuICAgIH1cblxuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXZcbiAgICAgICAgICAgIGNsYXNzTmFtZT17YHRyZWUtaXRlbSBsZXZlbC0ke2xldmVsfWB9XG4gICAgICAgICAgICBzdHlsZT17e21hcmdpbkxlZnQ6IGAke2xldmVsfXJlbWB9fVxuICAgICAgICA+XG4gICAgICAgICAgICA8ZGl2XG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPXtqb2luKCcgJywgY3NzKX1cbiAgICAgICAgICAgICAgICBvbkNsaWNrPXsoZSkgPT4gb25DbGljayhlLCBpZGVudGlmaWVyLCBCb29sZWFuKGl0ZW1zKSl9XG4gICAgICAgICAgICA+XG4gICAgICAgICAgICAgICAge2l0ZW1zICYmIChcbiAgICAgICAgICAgICAgICAgICAgPHNwYW4gY2xhc3NOYW1lPVwidHJlZS1jYXJldFwiPlxuICAgICAgICAgICAgICAgICAgICAgICAge2lzRXhwYW5kZWQgPyBuZXN0X2ljb25fZXhwYW5kZWQgOiBuZXN0X2ljb25fY29sbGFwc2VkfVxuICAgICAgICAgICAgICAgICAgICA8L3NwYW4+XG4gICAgICAgICAgICAgICAgKX1cbiAgICAgICAgICAgICAgICB7bGFiZWwgfHwgaWRlbnRpZmllcn1cbiAgICAgICAgICAgIDwvZGl2PlxuXG4gICAgICAgICAgICB7aXRlbXMgJiYgaXNFeHBhbmRlZCAmJiAoXG4gICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJ0cmVlLXN1Yi1pdGVtc1wiPlxuICAgICAgICAgICAgICAgICAgICB7aXRlbXMubWFwKChpdGVtKSA9PlxuICAgICAgICAgICAgICAgICAgICAgICAgcmVuZGVySXRlbSh7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFyZW50OiBpZGVudGlmaWVyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uQ2xpY2ssXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgaXRlbSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsZXZlbDogbGV2ZWwgKyAxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGVjdGVkLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5lc3RfaWNvbl9leHBhbmRlZCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBuZXN0X2ljb25fY29sbGFwc2VkLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGV4cGFuZGVkX2l0ZW1zLFxuICAgICAgICAgICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgICAgICAgICAgKX1cbiAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICl9XG4gICAgICAgIDwvZGl2PlxuICAgICk7XG59O1xuXG5jb25zdCByZW5kZXJJdGVtID0gKHtwYXJlbnQsIGl0ZW0sIGxldmVsLCAuLi5yZXN0fTogYW55KSA9PiB7XG4gICAgaWYgKGlzKFN0cmluZywgaXRlbSkpIHtcbiAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgIDxUcmVlVmlld0VsZW1lbnRcbiAgICAgICAgICAgICAgICBsYWJlbD17aXRlbX1cbiAgICAgICAgICAgICAgICBpZGVudGlmaWVyPXtwYXJlbnQgPyBqb2luKCcuJywgW3BhcmVudCwgaXRlbV0pIDogaXRlbX1cbiAgICAgICAgICAgICAgICBsZXZlbD17bGV2ZWwgfHwgMH1cbiAgICAgICAgICAgICAgICBrZXk9e2l0ZW19XG4gICAgICAgICAgICAgICAgey4uLnJlc3R9XG4gICAgICAgICAgICAvPlxuICAgICAgICApO1xuICAgIH1cbiAgICByZXR1cm4gKFxuICAgICAgICA8VHJlZVZpZXdFbGVtZW50XG4gICAgICAgICAgICB7Li4uaXRlbX1cbiAgICAgICAgICAgIGxldmVsPXtsZXZlbCB8fCAwfVxuICAgICAgICAgICAga2V5PXtpdGVtLmlkZW50aWZpZXJ9XG4gICAgICAgICAgICBpZGVudGlmaWVyPXtcbiAgICAgICAgICAgICAgICBwYXJlbnQgPyBqb2luKCcuJywgW3BhcmVudCwgaXRlbS5pZGVudGlmaWVyXSkgOiBpdGVtLmlkZW50aWZpZXJcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHsuLi5yZXN0fVxuICAgICAgICAvPlxuICAgICk7XG59O1xuXG4vKipcbiAqIEEgdHJlZSBvZiBuZXN0ZWQgaXRlbXMuXG4gKlxuICogOkNTUzpcbiAqXG4gKiAgICAgLSBgYGRhenpsZXItZXh0cmEtdHJlZS12aWV3YGBcbiAqICAgICAtIGBgdHJlZS1pdGVtYGBcbiAqICAgICAtIGBgdHJlZS1pdGVtLWxhYmVsYGBcbiAqICAgICAtIGBgdHJlZS1zdWItaXRlbXNgYFxuICogICAgIC0gYGB0cmVlLWNhcmV0YGBcbiAqICAgICAtIGBgc2VsZWN0ZWRgYFxuICogICAgIC0gYGBsZXZlbC17bn1gYFxuICpcbiAqIDpleGFtcGxlOlxuICpcbiAqIC4uIGxpdGVyYWxpbmNsdWRlOjogLi4vLi4vdGVzdHMvY29tcG9uZW50cy9wYWdlcy90cmVldmlldy5weVxuICovXG5jb25zdCBUcmVlVmlldyA9ICh7XG4gICAgY2xhc3NfbmFtZSxcbiAgICBzdHlsZSxcbiAgICBpZGVudGl0eSxcbiAgICB1cGRhdGVBc3BlY3RzLFxuICAgIGl0ZW1zLFxuICAgIHNlbGVjdGVkLFxuICAgIGV4cGFuZGVkX2l0ZW1zLFxuICAgIG5lc3RfaWNvbl9leHBhbmRlZCxcbiAgICBuZXN0X2ljb25fY29sbGFwc2VkLFxufTogVHJlZVZpZXdQcm9wcykgPT4ge1xuICAgIGNvbnN0IG9uQ2xpY2sgPSAoZSwgaWRlbnRpZmllciwgZXhwYW5kKSA9PiB7XG4gICAgICAgIGUuc3RvcFByb3BhZ2F0aW9uKCk7XG4gICAgICAgIGNvbnN0IHBheWxvYWQ6IGFueSA9IHt9O1xuICAgICAgICBpZiAoc2VsZWN0ZWQgJiYgaW5jbHVkZXMoaWRlbnRpZmllciwgc2VsZWN0ZWQpKSB7XG4gICAgICAgICAgICBsZXQgbGFzdCA9IHNwbGl0KCcuJywgaWRlbnRpZmllcik7XG4gICAgICAgICAgICBsYXN0ID0gc2xpY2UoMCwgbGFzdC5sZW5ndGggLSAxLCBsYXN0KTtcbiAgICAgICAgICAgIGlmIChsYXN0Lmxlbmd0aCA9PT0gMCkge1xuICAgICAgICAgICAgICAgIHBheWxvYWQuc2VsZWN0ZWQgPSBudWxsO1xuICAgICAgICAgICAgfSBlbHNlIGlmIChsYXN0Lmxlbmd0aCA9PT0gMSkge1xuICAgICAgICAgICAgICAgIHBheWxvYWQuc2VsZWN0ZWQgPSBsYXN0WzBdO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICBwYXlsb2FkLnNlbGVjdGVkID0gam9pbignLicsIGxhc3QpO1xuICAgICAgICAgICAgfVxuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgcGF5bG9hZC5zZWxlY3RlZCA9IGlkZW50aWZpZXI7XG4gICAgICAgIH1cblxuICAgICAgICBpZiAoZXhwYW5kKSB7XG4gICAgICAgICAgICBpZiAoaW5jbHVkZXMoaWRlbnRpZmllciwgZXhwYW5kZWRfaXRlbXMpKSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC5leHBhbmRlZF9pdGVtcyA9IHdpdGhvdXQoW2lkZW50aWZpZXJdLCBleHBhbmRlZF9pdGVtcyk7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIHBheWxvYWQuZXhwYW5kZWRfaXRlbXMgPSBjb25jYXQoZXhwYW5kZWRfaXRlbXMsIFtpZGVudGlmaWVyXSk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgICAgdXBkYXRlQXNwZWN0cyhwYXlsb2FkKTtcbiAgICB9O1xuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBzdHlsZT17c3R5bGV9IGlkPXtpZGVudGl0eX0+XG4gICAgICAgICAgICB7aXRlbXMubWFwKChpdGVtKSA9PlxuICAgICAgICAgICAgICAgIHJlbmRlckl0ZW0oe1xuICAgICAgICAgICAgICAgICAgICBpdGVtLFxuICAgICAgICAgICAgICAgICAgICBvbkNsaWNrLFxuICAgICAgICAgICAgICAgICAgICBzZWxlY3RlZCxcbiAgICAgICAgICAgICAgICAgICAgbmVzdF9pY29uX2V4cGFuZGVkLFxuICAgICAgICAgICAgICAgICAgICBuZXN0X2ljb25fY29sbGFwc2VkLFxuICAgICAgICAgICAgICAgICAgICBleHBhbmRlZF9pdGVtcyxcbiAgICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgKX1cbiAgICAgICAgPC9kaXY+XG4gICAgKTtcbn07XG5cblRyZWVWaWV3LmRlZmF1bHRQcm9wcyA9IHtcbiAgICBuZXN0X2ljb25fY29sbGFwc2VkOiAn4o+1JyxcbiAgICBuZXN0X2ljb25fZXhwYW5kZWQ6ICfij7cnLFxuICAgIGV4cGFuZGVkX2l0ZW1zOiBbXSxcbn07XG5cbmV4cG9ydCBkZWZhdWx0IFRyZWVWaWV3O1xuIiwiaW1wb3J0ICcuLi9zY3NzL2luZGV4LnNjc3MnO1xuXG5pbXBvcnQgTm90aWNlIGZyb20gJy4vY29tcG9uZW50cy9Ob3RpY2UnO1xuaW1wb3J0IFBhZ2VyIGZyb20gJy4vY29tcG9uZW50cy9QYWdlcic7XG5pbXBvcnQgU3Bpbm5lciBmcm9tICcuL2NvbXBvbmVudHMvU3Bpbm5lcic7XG5pbXBvcnQgU3RpY2t5IGZyb20gJy4vY29tcG9uZW50cy9TdGlja3knO1xuaW1wb3J0IERyYXdlciBmcm9tICcuL2NvbXBvbmVudHMvRHJhd2VyJztcbmltcG9ydCBQb3BVcCBmcm9tICcuL2NvbXBvbmVudHMvUG9wVXAnO1xuaW1wb3J0IFRyZWVWaWV3IGZyb20gJy4vY29tcG9uZW50cy9UcmVlVmlldyc7XG5pbXBvcnQgVG9hc3QgZnJvbSAnLi9jb21wb25lbnRzL1RvYXN0JztcbmltcG9ydCBQYWdlTWFwIGZyb20gJy4vY29tcG9uZW50cy9QYWdlTWFwJztcbmltcG9ydCBDb2xvclBpY2tlciBmcm9tICcuL2NvbXBvbmVudHMvQ29sb3JQaWNrZXInO1xuXG5leHBvcnQge1xuICAgIE5vdGljZSxcbiAgICBQYWdlcixcbiAgICBTcGlubmVyLFxuICAgIFN0aWNreSxcbiAgICBEcmF3ZXIsXG4gICAgUG9wVXAsXG4gICAgVHJlZVZpZXcsXG4gICAgVG9hc3QsXG4gICAgUGFnZU1hcCxcbiAgICBDb2xvclBpY2tlcixcbn07XG4iLCJtb2R1bGUuZXhwb3J0cyA9IF9fV0VCUEFDS19FWFRFUk5BTF9NT0RVTEVfcmVhY3RfXzsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=