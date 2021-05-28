export class Pagination{
    public page:number;
    public perPage:number;


    constructor(page:number, perPage:number) {
        this.page = page;
        this.perPage = perPage;
    }
}