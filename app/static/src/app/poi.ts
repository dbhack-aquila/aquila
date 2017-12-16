export class Poi {
    public name: string;
    public description: string;
    public profilePicture: string;
    public latitude: number;
    public longitude: number;
    public linkUrls: [string];
    public imageUrls: [string];

    constructor(name: string, description: string, profilePicture: string, latitude: number, longitude: number, linkUrls: [string], imageUrls: [string]) {
        this.name = name;
        this.description = description;
        this.profilePicture = profilePicture;
        this.latitude = latitude;
        this.longitude = longitude;
        this.linkUrls = linkUrls;
        this.imageUrls = imageUrls;
    }
}
