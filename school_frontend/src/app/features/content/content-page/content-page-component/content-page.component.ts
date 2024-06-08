import { Component, Input, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'content-page',
  templateUrl: './content-page.component.html',
  styleUrls: ['./content-page.component.scss']
})
export class ContentPageComponent implements OnInit {

  items!: MenuItem[];

  ngOnInit() {
    this.items = [
      {
        label: 'Alunos',
        icon:  'pi pi-home',
      },
      {
        label: 'Provas',
        icon:  'pi pi-star',
      }
    ]
  }

}
