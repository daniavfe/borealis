import { HttpParams } from "@angular/common/http";

export class HttpHelper{

    public static createQueryParams(params:any):HttpParams
    {
        let queryParams = new HttpParams();
        for(let key in params){
            if (params[key] == null)
                continue;
            switch(typeof(params[key])){
                case typeof(Boolean):
                    if(params[key]){
                        queryParams = queryParams.set(key, '');
                    }
                    break;
                case typeof(Object()):
                    var items: any[] = params[key]
                    for (let item of items){
                        queryParams = queryParams.append(key, item);
                    }
                    break;
                default:
                    queryParams = queryParams.set(key, String(params[key]));
            }
        }
        return queryParams;
    }
}