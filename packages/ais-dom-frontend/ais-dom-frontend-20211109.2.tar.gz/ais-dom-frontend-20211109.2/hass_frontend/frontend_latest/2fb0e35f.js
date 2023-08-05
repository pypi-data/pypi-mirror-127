/*! For license information please see 2fb0e35f.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[56238],{14166:(t,e,n)=>{n.d(e,{W:()=>s});var i=function(){return i=Object.assign||function(t){for(var e,n=1,i=arguments.length;n<i;n++)for(var s in e=arguments[n])Object.prototype.hasOwnProperty.call(e,s)&&(t[s]=e[s]);return t},i.apply(this,arguments)};function s(t,e,n){void 0===e&&(e=Date.now()),void 0===n&&(n={});var s=i(i({},o),n||{}),r=(+t-+e)/1e3;if(Math.abs(r)<s.second)return{value:Math.round(r),unit:"second"};var a=r/60;if(Math.abs(a)<s.minute)return{value:Math.round(a),unit:"minute"};var c=r/3600;if(Math.abs(c)<s.hour)return{value:Math.round(c),unit:"hour"};var h=r/86400;if(Math.abs(h)<s.day)return{value:Math.round(h),unit:"day"};var u=new Date(t),d=new Date(e),l=u.getFullYear()-d.getFullYear();if(Math.round(Math.abs(l))>0)return{value:Math.round(l),unit:"year"};var p=12*l+u.getMonth()-d.getMonth();if(Math.round(Math.abs(p))>0)return{value:Math.round(p),unit:"month"};var v=r/604800;return{value:Math.round(v),unit:"week"}}var o={second:45,minute:45,hour:22,day:5}},14114:(t,e,n)=>{n.d(e,{P:()=>i});const i=t=>(e,n)=>{if(e.constructor._observers){if(!e.constructor.hasOwnProperty("_observers")){const t=e.constructor._observers;e.constructor._observers=new Map,t.forEach(((t,n)=>e.constructor._observers.set(n,t)))}}else{e.constructor._observers=new Map;const t=e.updated;e.updated=function(e){t.call(this,e),e.forEach(((t,e)=>{const n=this.constructor._observers.get(e);void 0!==n&&n.call(this,this[e],t)}))}}e.constructor._observers.set(n,t)}},63207:(t,e,n)=>{n(65660),n(15112);var i=n(9672),s=n(87156),o=n(50856),r=n(65233);(0,i.k)({_template:o.d`
    <style>
      :host {
        @apply --layout-inline;
        @apply --layout-center-center;
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        @apply --iron-icon;
      }

      :host([hidden]) {
        display: none;
      }
    </style>
`,is:"iron-icon",properties:{icon:{type:String},theme:{type:String},src:{type:String},_meta:{value:r.XY.create("iron-meta",{type:"iconset"})}},observers:["_updateIcon(_meta, isAttached)","_updateIcon(theme, isAttached)","_srcChanged(src, isAttached)","_iconChanged(icon, isAttached)"],_DEFAULT_ICONSET:"icons",_iconChanged:function(t){var e=(t||"").split(":");this._iconName=e.pop(),this._iconsetName=e.pop()||this._DEFAULT_ICONSET,this._updateIcon()},_srcChanged:function(t){this._updateIcon()},_usesIconset:function(){return this.icon||!this.src},_updateIcon:function(){this._usesIconset()?(this._img&&this._img.parentNode&&(0,s.vz)(this.root).removeChild(this._img),""===this._iconName?this._iconset&&this._iconset.removeIcon(this):this._iconsetName&&this._meta&&(this._iconset=this._meta.byKey(this._iconsetName),this._iconset?(this._iconset.applyIcon(this,this._iconName,this.theme),this.unlisten(window,"iron-iconset-added","_updateIcon")):this.listen(window,"iron-iconset-added","_updateIcon"))):(this._iconset&&this._iconset.removeIcon(this),this._img||(this._img=document.createElement("img"),this._img.style.width="100%",this._img.style.height="100%",this._img.draggable=!1),this._img.src=this.src,(0,s.vz)(this.root).appendChild(this._img))}})},49075:(t,e,n)=>{n.d(e,{S:()=>r,B:()=>a});n(65233);var i=n(51644),s=n(26110),o=n(84938);const r={observers:["_focusedChanged(receivedFocusFromKeyboard)"],_focusedChanged:function(t){t&&this.ensureRipple(),this.hasRipple()&&(this._ripple.holdDown=t)},_createRipple:function(){var t=o.o._createRipple();return t.id="ink",t.setAttribute("center",""),t.classList.add("circle"),t}},a=[i.P,s.a,o.o,r]},25782:(t,e,n)=>{n(65233),n(65660),n(70019),n(97968);var i=n(9672),s=n(50856),o=n(33760);(0,i.k)({_template:s.d`
    <style include="paper-item-shared-styles"></style>
    <style>
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
        @apply --paper-icon-item;
      }

      .content-icon {
        @apply --layout-horizontal;
        @apply --layout-center;

        width: var(--paper-item-icon-width, 56px);
        @apply --paper-item-icon;
      }
    </style>

    <div id="contentIcon" class="content-icon">
      <slot name="item-icon"></slot>
    </div>
    <slot></slot>
`,is:"paper-icon-item",behaviors:[o.U]})},21560:(t,e,n)=>{n.d(e,{ZH:()=>u,MT:()=>o,U2:()=>c,RV:()=>s,t8:()=>h});const i=function(){if(!(!navigator.userAgentData&&/Safari\//.test(navigator.userAgent)&&!/Chrom(e|ium)\//.test(navigator.userAgent))||!indexedDB.databases)return Promise.resolve();let t;return new Promise((e=>{const n=()=>indexedDB.databases().finally(e);t=setInterval(n,100),n()})).finally((()=>clearInterval(t)))};function s(t){return new Promise(((e,n)=>{t.oncomplete=t.onsuccess=()=>e(t.result),t.onabort=t.onerror=()=>n(t.error)}))}function o(t,e){const n=i().then((()=>{const n=indexedDB.open(t);return n.onupgradeneeded=()=>n.result.createObjectStore(e),s(n)}));return(t,i)=>n.then((n=>i(n.transaction(e,t).objectStore(e))))}let r;function a(){return r||(r=o("keyval-store","keyval")),r}function c(t,e=a()){return e("readonly",(e=>s(e.get(t))))}function h(t,e,n=a()){return n("readwrite",(n=>(n.put(e,t),s(n.transaction))))}function u(t=a()){return t("readwrite",(t=>(t.clear(),s(t.transaction))))}},32930:(t,e,n)=>{n.d(e,{v:()=>s});var i=n(39030);function s(t="",e=!1,n=""){return(0,i.eZ)({descriptor:i=>({get(){var i,s,o;const r="slot"+(t?`[name=${t}]`:":not([name])");let a=null!==(o=null===(s=null===(i=this.renderRoot)||void 0===i?void 0:i.querySelector(r))||void 0===s?void 0:s.assignedNodes({flatten:e}))&&void 0!==o?o:[];return n&&(a=a.filter((t=>t.nodeType===Node.ELEMENT_NODE&&t.matches(n)))),a},enumerable:!0,configurable:!0})})}},22142:(t,e,n)=>{n.d(e,{C:()=>d});var i=n(15304),s=n(38941),o=n(81563),r=n(19596);class a{constructor(t){this.U=t}disconnect(){this.U=void 0}reconnect(t){this.U=t}deref(){return this.U}}class c{constructor(){this.Y=void 0,this.q=void 0}get(){return this.Y}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise((t=>this.q=t)))}resume(){var t;null===(t=this.q)||void 0===t||t.call(this),this.Y=this.q=void 0}}const h=t=>!(0,o.pt)(t)&&"function"==typeof t.then;class u extends r.s{constructor(){super(...arguments),this._$Cft=1073741823,this._$Cwt=[],this._$CG=new a(this),this._$CK=new c}render(...t){var e;return null!==(e=t.find((t=>!h(t))))&&void 0!==e?e:i.Jb}update(t,e){const n=this._$Cwt;let s=n.length;this._$Cwt=e;const o=this._$CG,r=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<e.length&&!(t>this._$Cft);t++){const i=e[t];if(!h(i))return this._$Cft=t,i;t<s&&i===n[t]||(this._$Cft=1073741823,s=0,Promise.resolve(i).then((async t=>{for(;r.get();)await r.get();const e=o.deref();if(void 0!==e){const n=e._$Cwt.indexOf(i);n>-1&&n<e._$Cft&&(e._$Cft=n,e.setValue(t))}})))}return i.Jb}disconnected(){this._$CG.disconnect(),this._$CK.pause()}reconnected(){this._$CG.reconnect(this),this._$CK.resume()}}const d=(0,s.XM)(u)}}]);
//# sourceMappingURL=2fb0e35f.js.map