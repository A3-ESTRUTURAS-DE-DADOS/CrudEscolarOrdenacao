import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  item: any[] = [
    {
      label: 'Alunos',
      icon: 'pi pi-user',
      route: '/alunos'
    },
    {
      label: 'Materias',
      icon: 'pi pi-file',
      route: '/materias'
    },
    {
      label: 'Provas',
      icon: 'pi pi-pencil',
      route: '/provas'
    }
  ]

  constructor() { }

  ngOnInit() {
  }

}
