export class Poi {
    public name: string;
    public description: string;
    public imageUrl: string;
    public latitude: number;
    public longitude: number;
    public linkUrls: [string];

    constructor(name: string, description: string, imageUrl: string, latitude: number, longitude: number, linkUrls: [string]) {
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
        this.latitude = latitude;
        this.longitude = longitude;
        this.linkUrls = linkUrls;
    }
}
