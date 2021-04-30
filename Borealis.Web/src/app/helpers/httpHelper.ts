import { HttpParams } from "@angular/common/http";

export class HttpHelper{

    public static createQueryParams(params:any):HttpParams
    {
        let queryParams = new HttpParams();

        for(let key in params){
            switch(typeof(params[key])){
                case typeof(Boolean()):
                    if(params[key]){
                        queryParams = queryParams.set(key, '');
                    }
                    break;
                default:
                    queryParams = queryParams.set(key, String(params[key]));
            }
        }
        return queryParams;
    }
}