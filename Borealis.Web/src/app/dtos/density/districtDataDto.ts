import { NeighborhoodDataDto } from "./neighborhoodDataDto";

export class DistrictDataDto {
    public id: number;
    public name: string;
    public neighborhoods: NeighborhoodDataDto[];
}