!function(t,i){for(var e in i)t[e]=i[e]}(window,webpackJsonp([21,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],{"./cms/static/js/factories/xblock_validation.js":function(t,i,e){"use strict";function s(t,i,e,s,a){var l,r;i&&!e&&(t.showSummaryOnly=!0),r=t,r.isUnit=s,l=new o(r,{parse:!0}),l.get("empty")||new n({el:a,model:l,root:e}).render()}Object.defineProperty(i,"__esModule",{value:!0}),i.default=s,e.d(i,"XBlockValidationFactory",function(){return s});var n=e("./cms/static/js/views/xblock_validation.js"),o=(e.n(n),e("./cms/static/js/models/xblock_validation.js"));e.n(o)},"./cms/static/js/models/xblock_validation.js":function(t,i,e){var s,n;s=[e(2),e(3),e(1)],void 0!==(n=function(t,i,e){return t.Model.extend({defaults:{summary:{},messages:[],empty:!0,xblock_id:null},WARNING:"warning",ERROR:"error",NOT_CONFIGURED:"not-configured",parse:function(t){if(!t.empty){var s="summary"in t?t.summary:{},n="messages"in t?t.messages:[];s.text||(t.isUnit?s.text=i("This unit has validation issues."):s.text=i("This component has validation issues.")),s.type||(s.type=this.WARNING,e.find(n,function(t){return t.type===this.ERROR&&(s.type=this.ERROR,!0)},this)),t.summary=s,t.showSummaryOnly&&(n=[]),t.messages=n}return t}})}.apply(i,s))&&(t.exports=n)},"./cms/static/js/views/xblock_validation.js":function(t,i,e){var s,n;s=[e(0),e(1),e("./cms/static/js/views/baseview.js"),e(3)],void 0!==(n=function(t,i,e,s){return e.extend({initialize:function(t){e.prototype.initialize.call(this),this.template=this.loadTemplate("xblock-validation-messages"),this.root=t.root},render:function(){return this.$el.html(this.template({validation:this.model,additionalClasses:this.getAdditionalClasses(),getIcon:this.getIcon.bind(this),getDisplayName:this.getDisplayName.bind(this)})),this},getIcon:function(t){return t===this.model.ERROR?"fa-exclamation-circle":t===this.model.WARNING||t===this.model.NOT_CONFIGURED?"fa-exclamation-triangle":null},getDisplayName:function(t){return t===this.model.WARNING||t===this.model.NOT_CONFIGURED?s("Warning"):t===this.model.ERROR?s("Error"):null},getAdditionalClasses:function(){return this.root&&this.model.get("summary").type===this.model.NOT_CONFIGURED&&0===this.model.get("messages").length?"no-container-content":""}})}.apply(i,s))&&(t.exports=n)},0:function(t,i){!function(){t.exports=window.jQuery}()},1:function(t,i){!function(){t.exports=window._}()},2:function(t,i){!function(){t.exports=window.Backbone}()},3:function(t,i){!function(){t.exports=window.gettext}()}},["./cms/static/js/factories/xblock_validation.js"]));