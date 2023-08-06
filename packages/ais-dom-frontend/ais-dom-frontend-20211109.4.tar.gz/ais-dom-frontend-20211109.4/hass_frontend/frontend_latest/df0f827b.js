/*! For license information please see df0f827b.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[36954],{14166:(t,e,s)=>{s.d(e,{W:()=>o});var i=function(){return i=Object.assign||function(t){for(var e,s=1,i=arguments.length;s<i;s++)for(var o in e=arguments[s])Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o]);return t},i.apply(this,arguments)};function o(t,e,s){void 0===e&&(e=Date.now()),void 0===s&&(s={});var o=i(i({},r),s||{}),n=(+t-+e)/1e3;if(Math.abs(n)<o.second)return{value:Math.round(n),unit:"second"};var a=n/60;if(Math.abs(a)<o.minute)return{value:Math.round(a),unit:"minute"};var h=n/3600;if(Math.abs(h)<o.hour)return{value:Math.round(h),unit:"hour"};var d=n/86400;if(Math.abs(d)<o.day)return{value:Math.round(d),unit:"day"};var l=new Date(t),c=new Date(e),u=l.getFullYear()-c.getFullYear();if(Math.round(Math.abs(u))>0)return{value:Math.round(u),unit:"year"};var _=12*u+l.getMonth()-c.getMonth();if(Math.round(Math.abs(_))>0)return{value:Math.round(_),unit:"month"};var v=n/604800;return{value:Math.round(v),unit:"week"}}var r={second:45,minute:45,hour:22,day:5}},49075:(t,e,s)=>{s.d(e,{S:()=>n,B:()=>a});s(65233);var i=s(51644),o=s(26110),r=s(84938);const n={observers:["_focusedChanged(receivedFocusFromKeyboard)"],_focusedChanged:function(t){t&&this.ensureRipple(),this.hasRipple()&&(this._ripple.holdDown=t)},_createRipple:function(){var t=r.o._createRipple();return t.id="ink",t.setAttribute("center",""),t.classList.add("circle"),t}},a=[i.P,o.a,r.o,n]},38034:(t,e,s)=>{var i=s(87480),o=s(37500),r=s(5701),n=s(17717);class a extends o.oi{constructor(){super(),this.min=0,this.max=100,this.step=1,this.startAngle=135,this.arcLength=270,this.handleSize=6,this.handleZoom=1.5,this.readonly=!1,this.disabled=!1,this.dragging=!1,this.rtl=!1,this._scale=1,this.dragEnd=this.dragEnd.bind(this),this.drag=this.drag.bind(this),this._keyStep=this._keyStep.bind(this)}connectedCallback(){super.connectedCallback(),document.addEventListener("mouseup",this.dragEnd),document.addEventListener("touchend",this.dragEnd,{passive:!1}),document.addEventListener("mousemove",this.drag),document.addEventListener("touchmove",this.drag,{passive:!1}),document.addEventListener("keydown",this._keyStep)}disconnectedCallback(){super.disconnectedCallback(),document.removeEventListener("mouseup",this.dragEnd),document.removeEventListener("touchend",this.dragEnd),document.removeEventListener("mousemove",this.drag),document.removeEventListener("touchmove",this.drag),document.removeEventListener("keydown",this._keyStep)}get _start(){return this.startAngle*Math.PI/180}get _len(){return Math.min(this.arcLength*Math.PI/180,2*Math.PI-.01)}get _end(){return this._start+this._len}get _showHandle(){return!this.readonly&&(null!=this.value||null!=this.high&&null!=this.low)}_angleInside(t){let e=(this.startAngle+this.arcLength/2-t+180+360)%360-180;return e<this.arcLength/2&&e>-this.arcLength/2}_angle2xy(t){return this.rtl?{x:-Math.cos(t),y:Math.sin(t)}:{x:Math.cos(t),y:Math.sin(t)}}_xy2angle(t,e){return this.rtl&&(t=-t),(Math.atan2(e,t)-this._start+2*Math.PI)%(2*Math.PI)}_value2angle(t){const e=((t=Math.min(this.max,Math.max(this.min,t)))-this.min)/(this.max-this.min);return this._start+e*this._len}_angle2value(t){return Math.round((t/this._len*(this.max-this.min)+this.min)/this.step)*this.step}get _boundaries(){const t=this._angle2xy(this._start),e=this._angle2xy(this._end);let s=1;this._angleInside(270)||(s=Math.max(-t.y,-e.y));let i=1;this._angleInside(90)||(i=Math.max(t.y,e.y));let o=1;this._angleInside(180)||(o=Math.max(-t.x,-e.x));let r=1;return this._angleInside(0)||(r=Math.max(t.x,e.x)),{up:s,down:i,left:o,right:r,height:s+i,width:o+r}}_mouse2value(t){const e=t.type.startsWith("touch")?t.touches[0].clientX:t.clientX,s=t.type.startsWith("touch")?t.touches[0].clientY:t.clientY,i=this.shadowRoot.querySelector("svg").getBoundingClientRect(),o=this._boundaries,r=e-(i.left+o.left*i.width/o.width),n=s-(i.top+o.up*i.height/o.height),a=this._xy2angle(r,n);return this._angle2value(a)}dragStart(t){if(!this._showHandle||this.disabled)return;let e,s=t.target;if(this._rotation&&"focus"!==this._rotation.type)return;if(s.classList.contains("shadowpath"))if("touchstart"===t.type&&(e=window.setTimeout((()=>{this._rotation&&(this._rotation.cooldown=void 0)}),200)),null==this.low)s=this.shadowRoot.querySelector("#value");else{const e=this._mouse2value(t);s=Math.abs(e-this.low)<Math.abs(e-this.high)?this.shadowRoot.querySelector("#low"):this.shadowRoot.querySelector("#high")}if(s.classList.contains("overflow")&&(s=s.nextElementSibling),!s.classList.contains("handle"))return;s.setAttribute("stroke-width",String(2*this.handleSize*this.handleZoom*this._scale));const i="high"===s.id?this.low:this.min,o="low"===s.id?this.high:this.max;this._rotation={handle:s,min:i,max:o,start:this[s.id],type:t.type,cooldown:e},this.dragging=!0}_cleanupRotation(){const t=this._rotation.handle;t.setAttribute("stroke-width",String(2*this.handleSize*this._scale)),this._rotation=void 0,this.dragging=!1,t.blur()}dragEnd(t){if(!this._showHandle||this.disabled)return;if(!this._rotation)return;const e=this._rotation.handle;this._cleanupRotation();let s=new CustomEvent("value-changed",{detail:{[e.id]:this[e.id]},bubbles:!0,composed:!0});this.dispatchEvent(s),this.low&&this.low>=.99*this.max?this._reverseOrder=!0:this._reverseOrder=!1}drag(t){if(!this._showHandle||this.disabled)return;if(!this._rotation)return;if(this._rotation.cooldown)return window.clearTimeout(this._rotation.cooldown),void this._cleanupRotation();if("focus"===this._rotation.type)return;t.preventDefault();const e=this._mouse2value(t);this._dragpos(e)}_dragpos(t){if(t<this._rotation.min||t>this._rotation.max)return;const e=this._rotation.handle;this[e.id]=t;let s=new CustomEvent("value-changing",{detail:{[e.id]:t},bubbles:!0,composed:!0});this.dispatchEvent(s)}_keyStep(t){if(!this._showHandle||this.disabled)return;if(!this._rotation)return;const e=this._rotation.handle;"ArrowLeft"!==t.key&&"ArrowDown"!==t.key||(t.preventDefault(),this.rtl?this._dragpos(this[e.id]+this.step):this._dragpos(this[e.id]-this.step)),"ArrowRight"!==t.key&&"ArrowUp"!==t.key||(t.preventDefault(),this.rtl?this._dragpos(this[e.id]-this.step):this._dragpos(this[e.id]+this.step)),"Home"===t.key&&(t.preventDefault(),this._dragpos(this.min)),"End"===t.key&&(t.preventDefault(),this._dragpos(this.max))}updated(t){if(this.shadowRoot.querySelector(".slider")){const t=window.getComputedStyle(this.shadowRoot.querySelector(".slider"));if(t&&t.strokeWidth){const e=parseFloat(t.strokeWidth);if(e>this.handleSize*this.handleZoom){const t=this._boundaries,s=`\n          ${e/2*Math.abs(t.up)}px\n          ${e/2*Math.abs(t.right)}px\n          ${e/2*Math.abs(t.down)}px\n          ${e/2*Math.abs(t.left)}px`;this.shadowRoot.querySelector("svg").style.margin=s}}}if(this.shadowRoot.querySelector("svg")&&void 0===this.shadowRoot.querySelector("svg").style.vectorEffect){t.has("_scale")&&1!=this._scale&&this.shadowRoot.querySelector("svg").querySelectorAll("path").forEach((t=>{if(t.getAttribute("stroke-width"))return;const e=parseFloat(getComputedStyle(t).getPropertyValue("stroke-width"));t.style.strokeWidth=e*this._scale+"px"}));const e=this.shadowRoot.querySelector("svg").getBoundingClientRect(),s=Math.max(e.width,e.height);this._scale=2/s}}_renderArc(t,e){const s=e-t,i=this._angle2xy(t),o=this._angle2xy(e+.001);return`\n      M ${i.x} ${i.y}\n      A 1 1,\n        0,\n        ${s>Math.PI?"1":"0"} ${this.rtl?"0":"1"},\n        ${o.x} ${o.y}\n    `}_renderHandle(t){const e=this._value2angle(this[t]),s=this._angle2xy(e),i={value:this.valueLabel,low:this.lowLabel,high:this.highLabel}[t]||"";return o.YP`
      <g class="${t} handle">
        <path
          id=${t}
          class="overflow"
          d="
          M ${s.x} ${s.y}
          L ${s.x+.001} ${s.y+.001}
          "
          vector-effect="non-scaling-stroke"
          stroke="rgba(0,0,0,0)"
          stroke-width="${4*this.handleSize*this._scale}"
          />
        <path
          id=${t}
          class="handle"
          d="
          M ${s.x} ${s.y}
          L ${s.x+.001} ${s.y+.001}
          "
          vector-effect="non-scaling-stroke"
          stroke-width="${2*this.handleSize*this._scale}"
          tabindex="0"
          @focus=${this.dragStart}
          @blur=${this.dragEnd}
          role="slider"
          aria-valuemin=${this.min}
          aria-valuemax=${this.max}
          aria-valuenow=${this[t]}
          aria-disabled=${this.disabled}
          aria-label=${i||""}
          />
        </g>
      `}render(){const t=this._boundaries;return o.dy`
      <svg
        @mousedown=${this.dragStart}
        @touchstart=${this.dragStart}
        xmln="http://www.w3.org/2000/svg"
        viewBox="${-t.left} ${-t.up} ${t.width} ${t.height}"
        style="margin: ${this.handleSize*this.handleZoom}px;"
        ?disabled=${this.disabled}
        focusable="false"
      >
        <g class="slider">
          <path
            class="path"
            d=${this._renderArc(this._start,this._end)}
            vector-effect="non-scaling-stroke"
          />
          <path
            class="bar"
            vector-effect="non-scaling-stroke"
            d=${this._renderArc(this._value2angle(null!=this.low?this.low:this.min),this._value2angle(null!=this.high?this.high:this.value))}
          />
          <path
            class="shadowpath"
            d=${this._renderArc(this._start,this._end)}
            vector-effect="non-scaling-stroke"
            stroke="rgba(0,0,0,0)"
            stroke-width="${3*this.handleSize*this._scale}"
            stroke-linecap="butt"
          />
        </g>

        <g class="handles">
          ${this._showHandle?null!=this.low?this._reverseOrder?o.YP`${this._renderHandle("high")} ${this._renderHandle("low")}`:o.YP`${this._renderHandle("low")} ${this._renderHandle("high")}`:o.YP`${this._renderHandle("value")}`:""}
        </g>
      </svg>
    `}static get styles(){return o.iv`
      :host {
        display: inline-block;
        width: 100%;
      }
      svg {
        overflow: visible;
        display: block;
      }
      path {
        transition: stroke 1s ease-out, stroke-width 200ms ease-out;
      }
      .slider {
        fill: none;
        stroke-width: var(--round-slider-path-width, 3);
        stroke-linecap: var(--round-slider-linecap, round);
      }
      .path {
        stroke: var(--round-slider-path-color, lightgray);
      }
      .bar {
        stroke: var(--round-slider-bar-color, deepskyblue);
      }
      svg[disabled] .bar {
        stroke: var(--round-slider-disabled-bar-color, darkgray);
      }
      g.handles {
        stroke: var(
          --round-slider-handle-color,
          var(--round-slider-bar-color, deepskyblue)
        );
        stroke-linecap: round;
        cursor: var(--round-slider-handle-cursor, pointer);
      }
      g.low.handle {
        stroke: var(--round-slider-low-handle-color);
      }
      g.high.handle {
        stroke: var(--round-slider-high-handle-color);
      }
      svg[disabled] g.handles {
        stroke: var(--round-slider-disabled-bar-color, darkgray);
      }
      .handle:focus {
        outline: unset;
      }
    `}}(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"value",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"high",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"low",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"min",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"max",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"step",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"startAngle",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"arcLength",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"handleSize",void 0),(0,i.__decorate)([(0,r.C)({type:Number})],a.prototype,"handleZoom",void 0),(0,i.__decorate)([(0,r.C)({type:Boolean})],a.prototype,"readonly",void 0),(0,i.__decorate)([(0,r.C)({type:Boolean})],a.prototype,"disabled",void 0),(0,i.__decorate)([(0,r.C)({type:Boolean,reflect:!0})],a.prototype,"dragging",void 0),(0,i.__decorate)([(0,r.C)({type:Boolean})],a.prototype,"rtl",void 0),(0,i.__decorate)([(0,r.C)()],a.prototype,"valueLabel",void 0),(0,i.__decorate)([(0,r.C)()],a.prototype,"lowLabel",void 0),(0,i.__decorate)([(0,r.C)()],a.prototype,"highLabel",void 0),(0,i.__decorate)([(0,n.S)()],a.prototype,"_scale",void 0),customElements.define("round-slider",a)},19596:(t,e,s)=>{s.d(e,{s:()=>c});var i=s(81563),o=s(38941);const r=(t,e)=>{var s,i;const o=t._$AN;if(void 0===o)return!1;for(const t of o)null===(i=(s=t)._$AO)||void 0===i||i.call(s,e,!1),r(t,e);return!0},n=t=>{let e,s;do{if(void 0===(e=t._$AM))break;s=e._$AN,s.delete(t),t=e}while(0===(null==s?void 0:s.size))},a=t=>{for(let e;e=t._$AM;t=e){let s=e._$AN;if(void 0===s)e._$AN=s=new Set;else if(s.has(t))break;s.add(t),l(e)}};function h(t){void 0!==this._$AN?(n(this),this._$AM=t,a(this)):this._$AM=t}function d(t,e=!1,s=0){const i=this._$AH,o=this._$AN;if(void 0!==o&&0!==o.size)if(e)if(Array.isArray(i))for(let t=s;t<i.length;t++)r(i[t],!1),n(i[t]);else null!=i&&(r(i,!1),n(i));else r(this,t)}const l=t=>{var e,s,i,r;t.type==o.pX.CHILD&&(null!==(e=(i=t)._$AP)&&void 0!==e||(i._$AP=d),null!==(s=(r=t)._$AQ)&&void 0!==s||(r._$AQ=h))};class c extends o.Xe{constructor(){super(...arguments),this._$AN=void 0}_$AT(t,e,s){super._$AT(t,e,s),a(this),this.isConnected=t._$AU}_$AO(t,e=!0){var s,i;t!==this.isConnected&&(this.isConnected=t,t?null===(s=this.reconnected)||void 0===s||s.call(this):null===(i=this.disconnected)||void 0===i||i.call(this)),e&&(r(this,t),n(this))}setValue(t){if((0,i.OR)(this._$Ct))this._$Ct._$AI(t,this);else{const e=[...this._$Ct._$AH];e[this._$Ci]=t,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}},81563:(t,e,s)=>{s.d(e,{E_:()=>p,i9:()=>_,_Y:()=>d,pt:()=>r,OR:()=>a,hN:()=>n,ws:()=>v,fk:()=>l,hl:()=>u});var i=s(15304);const{H:o}=i.Al,r=t=>null===t||"object"!=typeof t&&"function"!=typeof t,n=(t,e)=>{var s,i;return void 0===e?void 0!==(null===(s=t)||void 0===s?void 0:s._$litType$):(null===(i=t)||void 0===i?void 0:i._$litType$)===e},a=t=>void 0===t.strings,h=()=>document.createComment(""),d=(t,e,s)=>{var i;const r=t._$AA.parentNode,n=void 0===e?t._$AB:e._$AA;if(void 0===s){const e=r.insertBefore(h(),n),i=r.insertBefore(h(),n);s=new o(e,i,t,t.options)}else{const e=s._$AB.nextSibling,o=s._$AM,a=o!==t;if(a){let e;null===(i=s._$AQ)||void 0===i||i.call(s,t),s._$AM=t,void 0!==s._$AP&&(e=t._$AU)!==o._$AU&&s._$AP(e)}if(e!==n||a){let t=s._$AA;for(;t!==e;){const e=t.nextSibling;r.insertBefore(t,n),t=e}}}return s},l=(t,e,s=t)=>(t._$AI(e,s),t),c={},u=(t,e=c)=>t._$AH=e,_=t=>t._$AH,v=t=>{var e;null===(e=t._$AP)||void 0===e||e.call(t,!1,!0);let s=t._$AA;const i=t._$AB.nextSibling;for(;s!==i;){const t=s.nextSibling;s.remove(),s=t}},p=t=>{t._$AR()}},22142:(t,e,s)=>{s.d(e,{C:()=>c});var i=s(15304),o=s(38941),r=s(81563),n=s(19596);class a{constructor(t){this.U=t}disconnect(){this.U=void 0}reconnect(t){this.U=t}deref(){return this.U}}class h{constructor(){this.Y=void 0,this.q=void 0}get(){return this.Y}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise((t=>this.q=t)))}resume(){var t;null===(t=this.q)||void 0===t||t.call(this),this.Y=this.q=void 0}}const d=t=>!(0,r.pt)(t)&&"function"==typeof t.then;class l extends n.s{constructor(){super(...arguments),this._$Cft=1073741823,this._$Cwt=[],this._$CG=new a(this),this._$CK=new h}render(...t){var e;return null!==(e=t.find((t=>!d(t))))&&void 0!==e?e:i.Jb}update(t,e){const s=this._$Cwt;let o=s.length;this._$Cwt=e;const r=this._$CG,n=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<e.length&&!(t>this._$Cft);t++){const i=e[t];if(!d(i))return this._$Cft=t,i;t<o&&i===s[t]||(this._$Cft=1073741823,o=0,Promise.resolve(i).then((async t=>{for(;n.get();)await n.get();const e=r.deref();if(void 0!==e){const s=e._$Cwt.indexOf(i);s>-1&&s<e._$Cft&&(e._$Cft=s,e.setValue(t))}})))}return i.Jb}disconnected(){this._$CG.disconnect(),this._$CK.pause()}reconnected(){this._$CG.reconnect(this),this._$CK.resume()}}const c=(0,o.XM)(l)}}]);
//# sourceMappingURL=df0f827b.js.map