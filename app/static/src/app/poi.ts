export class Poi {
    public name: string;
    public description: string;
    public imageUrl: string;
    public latitude: number;
    public longitude: number;
    public linkUrls: string[];
    public relatedPics: string[];

    constructor(description: string, imageUrl: string, latitude: number, linkUrls: [string], longitude: number, name: string) {
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
        this.latitude = latitude;
        this.longitude = longitude;
        this.linkUrls = linkUrls;
        this.relatedPics = [];
        this.relatedPics.push(imageUrl);
    }
}
