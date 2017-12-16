import { Component, OnInit, Input } from '@angular/core';

import { Poi } from './../poi';


@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {

    @Input() poi: Poi;

	constructor() { }

    directPictureLinksLine1 = []
	directPictureLinksLine2 = []
	directPictureLinksLine3 = []
	modalActive = false
	imageLink = ""
	imageName = ""

	ngOnInit() {
		let amount = this.poi.imageUrls.length
		let rest = amount % 3
		let additional = 0
		if(rest < 3 && rest > 0){
			additional = 1
		}
		for(var i = 0; i < ((amount - rest) / 3) + additional; i++){
			this.directPictureLinksLine1.push({url: this.poi.imageUrls[i]})
		}
		if(rest == 2){
			additional = 2
		}
		else {
			additional = 0
		}
		for(i; i < (((amount - rest) / 3) * 2) + additional; i++){
			this.directPictureLinksLine2.push({url: this.poi.imageUrls[i]})
		}
		for(i; i < amount; i++){
			this.directPictureLinksLine3.push({url: this.poi.imageUrls[i]})
		}
	}

	showModal(link){
		this.imageLink = link.url
		this.modalActive = true
	}

	closeModal(){
		this.modalActive = false
	}

}
