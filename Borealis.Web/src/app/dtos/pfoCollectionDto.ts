
export class PFOCollectionDto<T>{
    public page: Number;
    public pageCount: Number;
    public perPage: Number;
    public orderBy: String;
    public orderByDescending: Boolean;
    public items: T[];

    constructor(page, pageCount, perPage, orderBy, orderByDescending, items) {
        this.page = page;
        this.pageCount = pageCount;
        this.perPage = perPage;
        this.orderBy = orderBy;
        this.orderByDescending = orderByDescending;
        this.items = items;
    }
}