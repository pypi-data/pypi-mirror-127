(self.webpackChunk_unfolded_jupyter_map_sdk=self.webpackChunk_unfolded_jupyter_map_sdk||[]).push([[568,591],{51568:function(e,t,n){"use strict";var i=this&&this.__createBinding||(Object.create?function(e,t,n,i){void 0===i&&(i=n),Object.defineProperty(e,i,{enumerable:!0,get:function(){return t[n]}})}:function(e,t,n,i){void 0===i&&(i=n),e[i]=t[n]}),o=this&&this.__exportStar||function(e,t){for(var n in e)"default"===n||Object.prototype.hasOwnProperty.call(t,n)||i(t,e,n)};Object.defineProperty(t,"__esModule",{value:!0}),o(n(18657),t),o(n(48601),t),o(n(40954),t)},11743:(e,t)=>{"use strict";var n;Object.defineProperty(t,"__esModule",{value:!0}),function(e){e.ON_LOAD="on_load",e.ON_FILTER="on_filter",e.ON_TIMELINE_INTERVAL_CHANGE="on_timeline_interval_change",e.ON_LAYER_TIMELINE_TIME_CHANGE="on_layer_timeline_time_change",e.ON_HOVER="on_hover",e.ON_CLICK="on_click",e.ON_GEOMETRY_SELECTION="on_geometry_selection"}(n||(n={})),t.default=class{constructor(e){this.queue=new Array,this.mapReady=!1,this.destroyed=!1,this.finalize=()=>{this.destroyed=!0,this.model.off("msg:custom",this.messageReceived),this.model.stopListening(this.model,"destroy",this.finalize);const e=this.model.get("map");e&&e.setMapEventHandlers(null)},this.messageReceived=(e,t)=>{this.destroyed||(console.log("messageReceived",e),this.mapReady?this.callSDKFunction(e):this.queue.push(e))},this.sendResponseToJupyter=(e,t)=>{if(this.destroyed)return;const n={messageId:e,data:t};console.log("sendResponse",n),this.model.send(n,[])},this.sendCallbackEventToJupyter=(e,t)=>{this.model.send({eventType:e,data:t},[])},this.model=e,this.model.on("msg:custom",this.messageReceived),this.model.listenTo(this.model,"destroy",this.finalize)}setMapReady(e){if(this.mapReady=e,this.mapReady){let e;for(;void 0!==(e=this.queue.shift());)this.callSDKFunction(e);const t=this.model.get("map");t&&t.setMapEventHandlers({onFilter:e=>this.sendCallbackEventToJupyter(n.ON_FILTER,e),onLoad:()=>this.sendCallbackEventToJupyter(n.ON_LOAD),onTimelineIntervalChange:e=>this.sendCallbackEventToJupyter(n.ON_TIMELINE_INTERVAL_CHANGE,e),onLayerTimelineTimeChange:e=>this.sendCallbackEventToJupyter(n.ON_LAYER_TIMELINE_TIME_CHANGE,e),onHover:e=>this.sendCallbackEventToJupyter(n.ON_HOVER,e),onClick:e=>this.sendCallbackEventToJupyter(n.ON_CLICK,e),onGeometrySelection:e=>this.sendCallbackEventToJupyter(n.ON_GEOMETRY_SELECTION,e)})}}callSDKFunction(e){const{messageId:t,type:n,data:i}=e;this.model.get("map")._callSDKFunction(n,i).then((e=>this.sendResponseToJupyter(t,e)))}}},3872:function(e,t,n){"use strict";var i=this&&this.__awaiter||function(e,t,n,i){return new(n||(n=Promise))((function(o,s){function a(e){try{l(i.next(e))}catch(e){s(e)}}function r(e){try{l(i.throw(e))}catch(e){s(e)}}function l(e){var t;e.done?o(e.value):(t=e.value,t instanceof n?t:new n((function(e){e(t)}))).then(a,r)}l((i=i.apply(e,t||[])).next())}))},o=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.createAwsBasemap=void 0;const s=o(n(56914)),a=n(17852);function r(e){return i(this,void 0,void 0,(function*(){yield e.refreshPromise(),setTimeout(r,e.expireTime.getTime()-(new Date).getTime())}))}t.createAwsBasemap=function({basemapStyle:e,identityPoolId:t}){return i(this,void 0,void 0,(function*(){let n,i;const o=t.split(":")[0],l=new s.default.CognitoIdentityCredentials({IdentityPoolId:t},{region:o});return n=(e=>t=>({url:a.Signer.signUrl(t,{access_key:e.accessKeyId,secret_key:e.secretAccessKey,session_token:e.sessionToken})}))(l),yield r(l),i={mapStyle:{mapStyles:{awsBasemap:{id:"awsBasemap",label:"AWS Basemap",url:n(e).url}},styleType:"awsBasemap"}},{transformRequest:n,initialState:i}}))}},90278:(e,t)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.loadScript=void 0;const n={};t.loadScript=function(e){if(!n[e]){const t=document.createElement("script");t.type="text/javascript",t.src=e;const i=document.querySelector("head");null==i||i.appendChild(t),n[e]=new Promise((e=>{t.onload=e}))}return n[e]}},18657:(e,t,n)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.MODULE_NAME=t.MODULE_VERSION=void 0;const i=n(60306);t.MODULE_VERSION=i.version,t.MODULE_NAME=i.name},48601:function(e,t,n){"use strict";var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.UnfoldedMapModel=void 0;const o=n(82565),s=n(18657),a=i(n(11743));class r extends o.DOMWidgetModel{constructor(){super(...arguments),this.transport=new a.default(this),this.onMapLoaded=()=>{this.transport.setMapReady(!0)}}defaults(){return Object.assign(Object.assign({},super.defaults()),{_model_name:r.model_name,_model_module:r.model_module,_model_module_version:r.model_module_version,_view_name:r.view_name,_view_module:r.view_module,_view_module_version:r.view_module_version,map:null})}}t.UnfoldedMapModel=r,r.serializers=Object.assign({},o.DOMWidgetModel.serializers),r.model_name="UnfoldedMapModel",r.model_module=s.MODULE_NAME,r.model_module_version=s.MODULE_VERSION,r.view_name="UnfoldedMapView",r.view_module=s.MODULE_NAME,r.view_module_version=s.MODULE_VERSION},40954:function(e,t,n){"use strict";var i=this&&this.__awaiter||function(e,t,n,i){return new(n||(n=Promise))((function(o,s){function a(e){try{l(i.next(e))}catch(e){s(e)}}function r(e){try{l(i.throw(e))}catch(e){s(e)}}function l(e){var t;e.done?o(e.value):(t=e.value,t instanceof n?t:new n((function(e){e(t)}))).then(a,r)}l((i=i.apply(e,t||[])).next())}))};Object.defineProperty(t,"__esModule",{value:!0}),t.UnfoldedMapView=void 0;const o=n(82565);n(17204);const s=n(44161),a=n(90278),r=n(3872),l="unfolded-widget";class d extends o.DOMWidgetView{initialize(){return i(this,void 0,void 0,(function*(){const e=this.model.get("width"),t=this.model.get("height"),n=this.model.get("mapUUID"),o=this.model.get("mapUrl"),l=this.model.get("iframe"),d=this.model.get("sdkUrl");let c;if(!l){const o=this.model.get("_basemap_style"),s=this.model.get("_identity_pool_id");let l={};if(o&&s){const{transformRequest:e,initialState:t}=yield r.createAwsBasemap({basemapStyle:o,identityPoolId:s});l={_transformRequest:e,initialState:t}}const u=yield(e=>i(void 0,void 0,void 0,(function*(){const t=()=>{var e;return null===(e=globalThis.Unfolded)||void 0===e?void 0:e.LocalUnfoldedMap};let n=t();if(!n)try{yield a.loadScript(`${e||"https://studio.unfolded.ai"}/studio-bundle.js`),n=t()}catch(e){console.error("Could not load Studio bundle",e)}return n})))(d);u&&(c=new u(Object.assign({mapUUID:n,width:e,height:t,onLoad:this.model.onMapLoaded},l)))}c||(c=new s.UnfoldedMap({mapUUID:n,mapUrl:o,appendToDocument:!1,width:e,height:t,embed:!0,onLoad:this.model.onMapLoaded})),this.model.set("map",c),this.model.save_changes(),this.render()}))}render(){if(this.el.classList.contains(l))return;const e=this.model.get("map");e&&(this.el.classList.add(l),e.render(this.el))}}t.UnfoldedMapView=d},23889:(e,t,n)=>{(t=n(23645)(!1)).push([e.id,".unfolded-widget {\n    width: 100%;\n    height: 100%;\n    min-height: 400px;\n}\n.unfolded-widget iframe {\n    border: none;\n}\n",""]),e.exports=t},23645:e=>{"use strict";e.exports=function(e){var t=[];return t.toString=function(){return this.map((function(t){var n=function(e,t){var n,i,o,s=e[1]||"",a=e[3];if(!a)return s;if(t&&"function"==typeof btoa){var r=(n=a,i=btoa(unescape(encodeURIComponent(JSON.stringify(n)))),o="sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(i),"/*# ".concat(o," */")),l=a.sources.map((function(e){return"/*# sourceURL=".concat(a.sourceRoot||"").concat(e," */")}));return[s].concat(l).concat([r]).join("\n")}return[s].join("\n")}(t,e);return t[2]?"@media ".concat(t[2]," {").concat(n,"}"):n})).join("")},t.i=function(e,n,i){"string"==typeof e&&(e=[[null,e,""]]);var o={};if(i)for(var s=0;s<this.length;s++){var a=this[s][0];null!=a&&(o[a]=!0)}for(var r=0;r<e.length;r++){var l=[].concat(e[r]);i&&o[l[0]]||(n&&(l[2]?l[2]="".concat(n," and ").concat(l[2]):l[2]=n),t.push(l))}},t}},17204:(e,t,n)=>{var i=n(93379),o=n(23889);"string"==typeof(o=o.__esModule?o.default:o)&&(o=[[e.id,o,""]]);i(o,{insert:"head",singleton:!1}),e.exports=o.locals||{}},93379:(e,t,n)=>{"use strict";var i,o=function(){var e={};return function(t){if(void 0===e[t]){var n=document.querySelector(t);if(window.HTMLIFrameElement&&n instanceof window.HTMLIFrameElement)try{n=n.contentDocument.head}catch(e){n=null}e[t]=n}return e[t]}}(),s=[];function a(e){for(var t=-1,n=0;n<s.length;n++)if(s[n].identifier===e){t=n;break}return t}function r(e,t){for(var n={},i=[],o=0;o<e.length;o++){var r=e[o],l=t.base?r[0]+t.base:r[0],d=n[l]||0,c="".concat(l," ").concat(d);n[l]=d+1;var u=a(c),p={css:r[1],media:r[2],sourceMap:r[3]};-1!==u?(s[u].references++,s[u].updater(p)):s.push({identifier:c,updater:h(p,t),references:1}),i.push(c)}return i}function l(e){var t=document.createElement("style"),i=e.attributes||{};if(void 0===i.nonce){var s=n.nc;s&&(i.nonce=s)}if(Object.keys(i).forEach((function(e){t.setAttribute(e,i[e])})),"function"==typeof e.insert)e.insert(t);else{var a=o(e.insert||"head");if(!a)throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");a.appendChild(t)}return t}var d,c=(d=[],function(e,t){return d[e]=t,d.filter(Boolean).join("\n")});function u(e,t,n,i){var o=n?"":i.media?"@media ".concat(i.media," {").concat(i.css,"}"):i.css;if(e.styleSheet)e.styleSheet.cssText=c(t,o);else{var s=document.createTextNode(o),a=e.childNodes;a[t]&&e.removeChild(a[t]),a.length?e.insertBefore(s,a[t]):e.appendChild(s)}}function p(e,t,n){var i=n.css,o=n.media,s=n.sourceMap;if(o?e.setAttribute("media",o):e.removeAttribute("media"),s&&"undefined"!=typeof btoa&&(i+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(s))))," */")),e.styleSheet)e.styleSheet.cssText=i;else{for(;e.firstChild;)e.removeChild(e.firstChild);e.appendChild(document.createTextNode(i))}}var m=null,f=0;function h(e,t){var n,i,o;if(t.singleton){var s=f++;n=m||(m=l(t)),i=u.bind(null,n,s,!1),o=u.bind(null,n,s,!0)}else n=l(t),i=p.bind(null,n,t),o=function(){!function(e){if(null===e.parentNode)return!1;e.parentNode.removeChild(e)}(n)};return i(e),function(t){if(t){if(t.css===e.css&&t.media===e.media&&t.sourceMap===e.sourceMap)return;i(e=t)}else o()}}e.exports=function(e,t){(t=t||{}).singleton||"boolean"==typeof t.singleton||(t.singleton=(void 0===i&&(i=Boolean(window&&document&&document.all&&!window.atob)),i));var n=r(e=e||[],t);return function(e){if(e=e||[],"[object Array]"===Object.prototype.toString.call(e)){for(var i=0;i<n.length;i++){var o=a(n[i]);s[o].references--}for(var l=r(e,t),d=0;d<n.length;d++){var c=a(n[d]);0===s[c].references&&(s[c].updater(),s.splice(c,1))}n=l}}}},60306:e=>{"use strict";e.exports=JSON.parse('{"name":"@unfolded/jupyter-map-sdk","version":"0.4.1","description":"A Custom Jupyter Widget Library","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/UnfoldedInc/platform","bugs":{"url":"https://github.com/UnfoldedInc/platform/issues"},"license":"UNLICENSED","author":{"name":"Unfolded Inc.","email":"ilya@unfolded.ai"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/UnfoldedInc/platform"},"scripts":{"start":"yarn run watch","build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc && rimraf lib/__tests__","build:nbextension":"webpack --mode production","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf unfolded/map_sdk/labextension","clean:nbextension":"rimraf unfolded/map_sdk/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:prod","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode development","typescript":"tsc --noEmit"},"dependencies":{"@aws-amplify/core":"^4.2.9","@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0","@unfolded/map-sdk":"^0.3.0","aws-sdk":"^2.988.0"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.0.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"unfolded/map_sdk/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}')}}]);