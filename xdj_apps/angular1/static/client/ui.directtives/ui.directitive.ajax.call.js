angularDefine(function(mdl){
    /**
 * <call data-id="ajax function name" [data-params="param variable"] [data-callback="callback function name"] [data-function="function name"/>
 */
mdl.directive("call",["$parse",function($parse){
    return {
        restrict:"ECA",
        priority:2,
        scope:false,
        link:function(s,e,a){

            s.$watch(e.parent().attr("ws")||"$ws",function(o,v){
                var scope=findScopeById(e.parent().attr("s-id")*1)||s;
                var ws=undefined;
                function exec(params,callback){
                    
                        var data=params||scope.$eval(a.params);
                        ws.call(a.id,data,function(e,r){
                            if(e){
                                throw(e);
                                return;
                            }
                            if(callback){
                                callback(r);
                                return;
                            }
                            if(a.callback){
                                var fn=scope.$eval(a.callback);
                                if(angular.isFunction(fn)){
                                    fn(r);
                                }
                            }
                            if(a.ngModel){
                                $parse(a.ngModel).assign(scope,r);
                                scope.$applyAsync();
                            }
                        });
                }
                if(angular.isDefined(v)){
                    ws=v;
                    if(a.id && (!a.function)){
                        exec();

                    }
                    else {
                        $parse(a.function).assign(scope,exec);
                    }
                }
            })
            
        }
    }
}])


})