var _JUPYTERLAB;(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@beakerx/beakerx-widgets"]=(()=>{"use strict";var e,r,t,a,n,o,i,l,u,d,s,f,c,p,h,b,m,g,v,y,w,j,k,x={24144:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(463),t.e(125),t.e(411),t.e(111),t.e(133)]).then((()=>()=>t(32133))),"./extension":()=>Promise.all([t.e(463),t.e(125),t.e(411),t.e(111),t.e(133)]).then((()=>()=>t(32133)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a=t.S.default,n="default";if(a&&a!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[n]=e,t.I(n,r)}};t.d(r,{get:()=>n,init:()=>o})}},P={};function S(e){if(P[e])return P[e].exports;var r=P[e]={id:e,loaded:!1,exports:{}};return x[e].call(r.exports,r,r.exports,S),r.loaded=!0,r.exports}return S.m=x,S.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return S.d(r,{a:r}),r},S.d=(e,r)=>{for(var t in r)S.o(r,t)&&!S.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},S.f={},S.e=e=>Promise.all(Object.keys(S.f).reduce(((r,t)=>(S.f[t](e,r),r)),[])),S.u=e=>e+"."+{42:"7926e4bb2d5827ee2c83",111:"7d5b14e3e803a226eaca",125:"5b8995ac9a1710175b02",133:"641f5b5c5676b15c3d14",302:"98a58195130a9e6390f3",346:"895410b9236af7702b34",411:"d3331f7a1bba6a5a4f32",420:"dde4264172817d53dd1c",445:"efcf5223510bcbc5bfb8",456:"2fd574a9bb0c00901787",463:"64c332916e63766926a9",527:"98fecdc71c437697381d",539:"6c9a67bdde79c658af52",700:"ad4071b0e71e6b32a555",755:"5a8f589450c22945efdd",963:"97849915014af6a0ee64"}[e]+".js",S.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),S.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="@beakerx/beakerx-widgets:",S.l=(t,a,n,o)=>{if(e[t])e[t].push(a);else{var i,l;if(void 0!==n)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var s=u[d];if(s.getAttribute("src")==t||s.getAttribute("data-webpack")==r+n){i=s;break}}i||(l=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,S.nc&&i.setAttribute("nonce",S.nc),i.setAttribute("data-webpack",r+n),i.src=t),e[t]=[a];var f=(r,a)=>{i.onerror=i.onload=null,clearTimeout(c);var n=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(a))),r)return r(a)},c=setTimeout(f.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=f.bind(null,i.onerror),i.onload=f.bind(null,i.onload),l&&document.head.appendChild(i)}},S.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},S.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{S.S={};var e={},r={};S.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];S.o(S.S,t)||(S.S[t]={});var o=S.S[t],i="@beakerx/beakerx-widgets",l=(e,r,t,a)=>{var n=o[e]=o[e]||{},l=n[r];(!l||!l.loaded&&(!a!=!l.eager?a:i>l.from))&&(n[r]={get:t,from:i,eager:!!a})},u=[];switch(t){case"default":l("@beakerx/beakerx-widgets","2.3.4",(()=>Promise.all([S.e(463),S.e(125),S.e(411),S.e(111),S.e(133)]).then((()=>()=>S(32133))))),l("@jupyter-widgets/controls","3.0.0",(()=>Promise.all([S.e(420),S.e(125),S.e(456),S.e(111),S.e(539)]).then((()=>()=>S(57420))))),l("big.js","5.2.2",(()=>S.e(302).then((()=>()=>S(93302))))),l("d3","5.16.0",(()=>Promise.all([S.e(42),S.e(463)]).then((()=>()=>S(40042))))),l("flatpickr","4.6.9",(()=>S.e(527).then((()=>()=>S(78527))))),l("jquery-ui.combobox","1.0.7",(()=>S.e(445).then((()=>()=>S(36445))))),l("jquery","3.5.1",(()=>S.e(755).then((()=>()=>S(19755))))),l("moment-timezone","0.5.32",(()=>Promise.all([S.e(346),S.e(700)]).then((()=>()=>S(80008))))),l("underscore","1.12.0",(()=>S.e(963).then((()=>()=>S(77963)))))}return e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;S.g.importScripts&&(e=S.g.location+"");var r=S.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),S.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],o=(typeof n)[0];if(a>=r.length)return"u"==o;var i=r[a],l=(typeof i)[0];if(o!=l)return"o"==o&&"n"==l||"s"==l||"u"==o;if("o"!=o&&"u"!=o&&n!=i)return n<i;a++}},n=e=>{if(1===e.length)return"*";if(0 in e){var r="",t=e[0];r+=0==t?">=":-1==t?"<":1==t?"^":2==t?"~":t>0?"=":"!=";for(var a=1,o=1;o<e.length;o++)a--,r+="u"==(typeof(l=e[o]))[0]?"-":(a>0?".":"")+(a=2,l);return r}var i=[];for(o=1;o<e.length;o++){var l=e[o];i.push(0===l?"not("+u()+")":1===l?"("+u()+" || "+u()+")":2===l?i.pop()+" "+i.pop():n(l))}return u();function u(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var i=0,l=1,u=!0;;l++,i++){var d,s,f=l<e.length?(typeof e[l])[0]:"";if(i>=r.length||"o"==(s=(typeof(d=r[i]))[0]))return!u||("u"==f?l>a&&!n:""==f!=n);if("u"==s){if(!u||"u"!=f)return!1}else if(u)if(f==s)if(l<=a){if(d!=e[l])return!1}else{if(n?d>e[l]:d<e[l])return!1;d!=e[l]&&(u=!1)}else if("s"!=f&&"n"!=f){if(n||l<=a)return!1;u=!1,l--}else{if(l<=a||s<f!=n)return!1;u=!1}else"s"!=f&&"n"!=f&&(u=!1,l--)}}var c=[],p=c.pop.bind(c);for(i=1;i<e.length;i++){var h=e[i];c.push(1==h?p()|p():2==h?p()&p():h?o(h,r):!p())}return!!p()},i=(e,r)=>{var t=S.S[e];if(!t||!S.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},l=(e,r)=>{var t=e[r];return(r=Object.keys(t).reduce(((e,r)=>!e||a(e,r)?r:e),0))&&t[r]},u=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},d=(e,r,t)=>"Unsatisfied version "+r+" of shared singleton module "+e+" (required "+n(t)+")",s=(e,r,t,a)=>{var n=u(e,t);return o(a,n)||"undefined"!=typeof console&&console.warn&&console.warn(d(t,n,a)),h(e[t][n])},f=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!o(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},c=(e,r,t,a)=>{var o=e[t];return"No satisfying version ("+n(a)+") of shared module "+t+" found in shared scope "+r+".\nAvailable versions: "+Object.keys(o).map((e=>e+" from "+o[e].from)).join(", ")},p=(e,r,t,a)=>{"undefined"!=typeof console&&console.warn&&console.warn(c(e,r,t,a))},h=e=>(e.loaded=1,e.get()),m=(b=e=>function(r,t,a,n){var o=S.I(r);return o&&o.then?o.then(e.bind(e,r,S.S[r],t,a,n)):e(r,S.S[r],t,a,n)})(((e,r,t,a)=>r&&S.o(r,t)?h(l(r,t)):a())),g=b(((e,r,t,a)=>(i(e,t),h(f(r,t,a)||p(r,e,t,a)||l(r,t))))),v=b(((e,r,t,a)=>(i(e,t),s(r,0,t,a)))),y=b(((e,r,t,a,n)=>{var o=r&&S.o(r,t)&&f(r,t,a);return o?h(o):n()})),w={},j={6168:()=>v("default","@lumino/signaling",[1,1,4,3]),13211:()=>v("default","@lumino/messaging",[1,1,4,3]),66510:()=>v("default","@lumino/widgets",[1,1,16,1]),70445:()=>m("default","jquery",(()=>S.e(755).then((()=>()=>S(19755))))),5446:()=>y("default","jquery",[1,3,5,1],(()=>S.e(755).then((()=>()=>S(19755))))),7441:()=>v("default","@jupyterlab/apputils",[1,3,0,5]),10323:()=>y("default","d3",[1,5,16,0],(()=>S.e(42).then((()=>()=>S(40042))))),18275:()=>v("default","@jupyterlab/coreutils",[1,5,0,3]),19129:()=>v("default","@lumino/disposable",[1,1,4,3]),21408:()=>v("default","@jupyterlab/application",[1,3,0,6]),35389:()=>v("default","@jupyterlab/settingregistry",[1,3,0,3]),39897:()=>y("default","@jupyter-widgets/controls",[,[1,3,0,0],[1,2,0,0],1],(()=>Promise.all([S.e(420),S.e(456)]).then((()=>()=>S(57420))))),41797:()=>v("default","@lumino/coreutils",[1,1,5,3]),46028:()=>y("default","moment-timezone",[2,0,5,28],(()=>Promise.all([S.e(346),S.e(700)]).then((()=>()=>S(80008))))),48237:()=>y("default","underscore",[1,1,10,2],(()=>S.e(963).then((()=>()=>S(77963))))),52453:()=>v("default","@jupyterlab/codemirror",[1,3,0,5]),53887:()=>y("default","flatpickr",[1,4,6,3],(()=>S.e(527).then((()=>()=>S(78527))))),70517:()=>y("default","jquery-ui.combobox",[1,1,0,7],(()=>S.e(445).then((()=>()=>S(36445))))),74582:()=>g("default","@jupyterlab/cells",[1,3,0,6]),78097:()=>v("default","@jupyter-widgets/base",[,[1,4,0,0],[1,3,0,0],[1,2,0,2],1,1]),79290:()=>v("default","@jupyterlab/services",[1,6,0,5]),79678:()=>y("default","big.js",[1,5,2,2],(()=>S.e(302).then((()=>()=>S(93302))))),94968:()=>v("default","@lumino/commands",[1,1,12,0]),18731:()=>y("default","underscore",[1,1,8,3],(()=>S.e(963).then((()=>()=>S(77963))))),19850:()=>v("default","@lumino/algorithm",[1,1,3,3]),76728:()=>v("default","@jupyter-widgets/base",[1,4,0,0]),87190:()=>y("default","jquery",[1,3,1,1],(()=>S.e(755).then((()=>()=>S(19755))))),90608:()=>v("default","@lumino/domutils",[1,1,2,3]),22576:()=>y("default","jquery",[0,1,6],(()=>S.e(755).then((()=>()=>S(19755)))))},k={111:[6168,13211,66510,70445],133:[5446,7441,10323,18275,19129,21408,35389,39897,41797,46028,48237,52453,53887,70517,74582,78097,79290,79678,94968],445:[22576],456:[18731,19850,76728,87190,90608]},S.f.consumes=(e,r)=>{S.o(k,e)&&k[e].forEach((e=>{if(S.o(w,e))return r.push(w[e]);var t=r=>{w[e]=0,x[e]=t=>{delete P[e],t.exports=r()}},a=r=>{delete w[e],x[e]=t=>{throw delete P[e],r}};try{var n=j[e]();n.then?r.push(w[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{var e={129:0};S.f.j=(r,t)=>{var a=S.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(/^(111|456)$/.test(r))e[r]=0;else{var n=new Promise(((t,n)=>{a=e[r]=[t,n]}));t.push(a[2]=n);var o=S.p+S.u(r),i=new Error;S.l(o,(t=>{if(S.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",i.name="ChunkLoadError",i.type=n,i.request=o,a[1](i)}}),"chunk-"+r,r)}};var r=(r,t)=>{for(var a,n,[o,i,l]=t,u=0,d=[];u<o.length;u++)n=o[u],S.o(e,n)&&e[n]&&d.push(e[n][0]),e[n]=0;for(a in i)S.o(i,a)&&(S.m[a]=i[a]);for(l&&l(S),r&&r(t);d.length;)d.shift()()},t=self.webpackChunk_beakerx_beakerx_widgets=self.webpackChunk_beakerx_beakerx_widgets||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),S(24144)})();