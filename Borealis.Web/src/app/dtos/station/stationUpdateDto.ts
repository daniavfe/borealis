import { NeighborhoodDto } from "../density/neighborhoodDto";

export class StationUpdateDto{
    public id:number;
    public name:string;
    public address:string;
    public startDate:Date;
    public endDate:Date;
    public latitude:string;
    public longitude:string;
    public altitude:number;
    public neighborhood:NeighborhoodDto;
    public neighborhoodId= ()=> this.neighborhood.id;

    constructor(id:number, name:string, address:string, startDate:Date, endDate:Date, latitude:string, longitude:string, altitude:number) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.startDate = startDate;
        this.endDate = endDate;
        this.latitude = latitude;
        this.longitude = longitude;
        this.altitude = altitude;
    }
}