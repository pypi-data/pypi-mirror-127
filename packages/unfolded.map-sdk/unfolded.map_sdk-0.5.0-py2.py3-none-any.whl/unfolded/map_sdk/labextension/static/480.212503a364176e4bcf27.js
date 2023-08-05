(self.webpackChunk_unfolded_jupyter_map_sdk=self.webpackChunk_unfolded_jupyter_map_sdk||[]).push([[480],{568:function(e,t,n){"use strict";var i=this&&this.__createBinding||(Object.create?function(e,t,n,i){void 0===i&&(i=n),Object.defineProperty(e,i,{enumerable:!0,get:function(){return t[n]}})}:function(e,t,n,i){void 0===i&&(i=n),e[i]=t[n]}),s=this&&this.__exportStar||function(e,t){for(var n in e)"default"===n||Object.prototype.hasOwnProperty.call(t,n)||i(t,e,n)};Object.defineProperty(t,"__esModule",{value:!0}),s(n(657),t),s(n(601),t),s(n(954),t)},743:(e,t)=>{"use strict";var n;Object.defineProperty(t,"__esModule",{value:!0}),function(e){e.ON_LOAD="on_load",e.ON_FILTER="on_filter",e.ON_TIMELINE_INTERVAL_CHANGE="on_timeline_interval_change",e.ON_LAYER_TIMELINE_TIME_CHANGE="on_layer_timeline_time_change",e.ON_HOVER="on_hover",e.ON_CLICK="on_click",e.ON_GEOMETRY_SELECTION="on_geometry_selection"}(n||(n={})),t.default=class{constructor(e){this.queue=new Array,this.mapReady=!1,this.destroyed=!1,this.finalize=()=>{this.destroyed=!0,this.model.off("msg:custom",this.messageReceived),this.model.stopListening(this.model,"destroy",this.finalize);const e=this.model.get("map");e&&e.setMapEventHandlers(null)},this.messageReceived=(e,t)=>{this.destroyed||(console.log("messageReceived",e),this.mapReady?this.sendMessageToMapSDK(e):this.queue.push(e))},this.sendResponseToJupyter=(e,t)=>{if(this.destroyed)return;const n={messageId:e,data:t};console.log("sendResponse",n),this.model.send(n,[])},this.sendCallbackEventToJupyter=(e,t)=>{this.model.send({eventType:e,data:t},[])},this.model=e,this.model.on("msg:custom",this.messageReceived),this.model.listenTo(this.model,"destroy",this.finalize)}setMapReady(e){if(this.mapReady=e,this.mapReady){let e;for(;void 0!==(e=this.queue.shift());)this.sendMessageToMapSDK(e);const t=this.model.get("map");t&&t.setMapEventHandlers({onFilter:e=>this.sendCallbackEventToJupyter(n.ON_FILTER,e),onLoad:()=>this.sendCallbackEventToJupyter(n.ON_LOAD),onTimelineIntervalChange:e=>this.sendCallbackEventToJupyter(n.ON_TIMELINE_INTERVAL_CHANGE,e),onLayerTimelineTimeChange:e=>this.sendCallbackEventToJupyter(n.ON_LAYER_TIMELINE_TIME_CHANGE,e),onHover:e=>this.sendCallbackEventToJupyter(n.ON_HOVER,e),onClick:e=>this.sendCallbackEventToJupyter(n.ON_CLICK,e),onGeometrySelection:e=>this.sendCallbackEventToJupyter(n.ON_GEOMETRY_SELECTION,e)})}}sendMessageToMapSDK(e){const{messageId:t,type:n,data:i}=e;this.model.get("map").sendMessage(n,i).then((e=>this.sendResponseToJupyter(t,e)))}}},480:function(e,t,n){"use strict";var i=this&&this.__createBinding||(Object.create?function(e,t,n,i){void 0===i&&(i=n),Object.defineProperty(e,i,{enumerable:!0,get:function(){return t[n]}})}:function(e,t,n,i){void 0===i&&(i=n),e[i]=t[n]}),s=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),o=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n in e)"default"!==n&&Object.prototype.hasOwnProperty.call(e,n)&&i(t,e,n);return s(t,e),t};Object.defineProperty(t,"__esModule",{value:!0});const r=n(565),a=o(n(568)),l=n(657),d={id:"@unfolded/jupyter-map-sdk:plugin",requires:[r.IJupyterWidgetRegistry],activate:function(e,t){t.registerWidget({name:l.MODULE_NAME,version:l.MODULE_VERSION,exports:a})},autoStart:!0};t.default=d},657:(e,t,n)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.MODULE_NAME=t.MODULE_VERSION=void 0;const i=n(306);t.MODULE_VERSION=i.version,t.MODULE_NAME=i.name},601:function(e,t,n){"use strict";var i=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.UnfoldedMapModel=void 0;const s=n(565),o=n(657),r=i(n(743));class a extends s.DOMWidgetModel{constructor(){super(...arguments),this.transport=new r.default(this),this.onMapLoaded=()=>{this.transport.setMapReady(!0)}}defaults(){return Object.assign(Object.assign({},super.defaults()),{_model_name:a.model_name,_model_module:a.model_module,_model_module_version:a.model_module_version,_view_name:a.view_name,_view_module:a.view_module,_view_module_version:a.view_module_version,map:null})}}t.UnfoldedMapModel=a,a.serializers=Object.assign({},s.DOMWidgetModel.serializers),a.model_name="UnfoldedMapModel",a.model_module=o.MODULE_NAME,a.model_module_version=o.MODULE_VERSION,a.view_name="UnfoldedMapView",a.view_module=o.MODULE_NAME,a.view_module_version=o.MODULE_VERSION},954:(e,t,n)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.UnfoldedMapView=void 0;const i=n(565);n(204);const s=n(837);class o extends i.DOMWidgetView{initialize(){const e=this.model.get("width"),t=this.model.get("height"),n=this.model.get("mapUUID"),i=this.model.get("mapUrl"),o=new s.UnfoldedMap({mapUUID:n,mapUrl:i,appendToDocument:!1,width:e,height:t,embed:!0,onLoad:this.model.onMapLoaded});return this.model.set("map",o),this.model.save_changes(),o}render(){this.el.classList.add("unfolded-widget");const e=this.model.get("map"),{iframe:t}=e;this.el.appendChild(t)}}t.UnfoldedMapView=o},889:(e,t,n)=>{(t=n(645)(!1)).push([e.id,".unfolded-widget {\n    width: 100%;\n    height: 100%;\n    min-height: 400px;\n}\n.unfolded-widget iframe {\n    border: none;\n}\n",""]),e.exports=t},645:e=>{"use strict";e.exports=function(e){var t=[];return t.toString=function(){return this.map((function(t){var n=function(e,t){var n,i,s,o=e[1]||"",r=e[3];if(!r)return o;if(t&&"function"==typeof btoa){var a=(n=r,i=btoa(unescape(encodeURIComponent(JSON.stringify(n)))),s="sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(i),"/*# ".concat(s," */")),l=r.sources.map((function(e){return"/*# sourceURL=".concat(r.sourceRoot||"").concat(e," */")}));return[o].concat(l).concat([a]).join("\n")}return[o].join("\n")}(t,e);return t[2]?"@media ".concat(t[2]," {").concat(n,"}"):n})).join("")},t.i=function(e,n,i){"string"==typeof e&&(e=[[null,e,""]]);var s={};if(i)for(var o=0;o<this.length;o++){var r=this[o][0];null!=r&&(s[r]=!0)}for(var a=0;a<e.length;a++){var l=[].concat(e[a]);i&&s[l[0]]||(n&&(l[2]?l[2]="".concat(n," and ").concat(l[2]):l[2]=n),t.push(l))}},t}},204:(e,t,n)=>{var i=n(379),s=n(889);"string"==typeof(s=s.__esModule?s.default:s)&&(s=[[e.id,s,""]]);i(s,{insert:"head",singleton:!1}),e.exports=s.locals||{}},379:(e,t,n)=>{"use strict";var i,s=function(){var e={};return function(t){if(void 0===e[t]){var n=document.querySelector(t);if(window.HTMLIFrameElement&&n instanceof window.HTMLIFrameElement)try{n=n.contentDocument.head}catch(e){n=null}e[t]=n}return e[t]}}(),o=[];function r(e){for(var t=-1,n=0;n<o.length;n++)if(o[n].identifier===e){t=n;break}return t}function a(e,t){for(var n={},i=[],s=0;s<e.length;s++){var a=e[s],l=t.base?a[0]+t.base:a[0],d=n[l]||0,u="".concat(l," ").concat(d);n[l]=d+1;var c=r(u),p={css:a[1],media:a[2],sourceMap:a[3]};-1!==c?(o[c].references++,o[c].updater(p)):o.push({identifier:u,updater:h(p,t),references:1}),i.push(u)}return i}function l(e){var t=document.createElement("style"),i=e.attributes||{};if(void 0===i.nonce){var o=n.nc;o&&(i.nonce=o)}if(Object.keys(i).forEach((function(e){t.setAttribute(e,i[e])})),"function"==typeof e.insert)e.insert(t);else{var r=s(e.insert||"head");if(!r)throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");r.appendChild(t)}return t}var d,u=(d=[],function(e,t){return d[e]=t,d.filter(Boolean).join("\n")});function c(e,t,n,i){var s=n?"":i.media?"@media ".concat(i.media," {").concat(i.css,"}"):i.css;if(e.styleSheet)e.styleSheet.cssText=u(t,s);else{var o=document.createTextNode(s),r=e.childNodes;r[t]&&e.removeChild(r[t]),r.length?e.insertBefore(o,r[t]):e.appendChild(o)}}function p(e,t,n){var i=n.css,s=n.media,o=n.sourceMap;if(s?e.setAttribute("media",s):e.removeAttribute("media"),o&&"undefined"!=typeof btoa&&(i+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(o))))," */")),e.styleSheet)e.styleSheet.cssText=i;else{for(;e.firstChild;)e.removeChild(e.firstChild);e.appendChild(document.createTextNode(i))}}var f=null,m=0;function h(e,t){var n,i,s;if(t.singleton){var o=m++;n=f||(f=l(t)),i=c.bind(null,n,o,!1),s=c.bind(null,n,o,!0)}else n=l(t),i=p.bind(null,n,t),s=function(){!function(e){if(null===e.parentNode)return!1;e.parentNode.removeChild(e)}(n)};return i(e),function(t){if(t){if(t.css===e.css&&t.media===e.media&&t.sourceMap===e.sourceMap)return;i(e=t)}else s()}}e.exports=function(e,t){(t=t||{}).singleton||"boolean"==typeof t.singleton||(t.singleton=(void 0===i&&(i=Boolean(window&&document&&document.all&&!window.atob)),i));var n=a(e=e||[],t);return function(e){if(e=e||[],"[object Array]"===Object.prototype.toString.call(e)){for(var i=0;i<n.length;i++){var s=r(n[i]);o[s].references--}for(var l=a(e,t),d=0;d<n.length;d++){var u=r(n[d]);0===o[u].references&&(o[u].updater(),o.splice(u,1))}n=l}}}},306:e=>{"use strict";e.exports=JSON.parse('{"name":"@unfolded/jupyter-map-sdk","version":"0.3.0","description":"A Custom Jupyter Widget Library","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/UnfoldedInc/platform","bugs":{"url":"https://github.com/UnfoldedInc/platform/issues"},"license":"UNLICENSED","author":{"name":"Unfolded Inc.","email":"ilya@unfolded.ai"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/UnfoldedInc/platform"},"scripts":{"start":"yarn run watch","build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc && rimraf lib/__tests__","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf unfolded/map_sdk/labextension","clean:nbextension":"rimraf unfolded/map_sdk/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch","typescript":"tsc --noEmit"},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0","@unfolded/map-sdk":"0.2.3"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.0.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"unfolded/map_sdk/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}')}}]);