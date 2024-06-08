import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'table-component',
  templateUrl: './table-component.component.html',
  styleUrls: ['./table-component.component.scss']
})
export class TableComponentComponent implements OnInit {
 
  //@Input() customers: any[] = [];
  
  alunos: any[] = [
    { 
      nome: 'Samuel', 
      idade: 20, 
      ano_escolar: '2ª Médio', 
      endereco: 'Av. Paulista, 1000'
    },
    {
      nome: 'Maria', 
      idade: 18, 
      ano_escolar: '1ª Médio', 
      endereco: 'Av. Paulista, 1000'
    },
    {
      nome: 'João', 
      idade: 17, 
      ano_escolar: '3ª Médio', 
      endereco: 'Av. Paulista, 1000'
    },
    {
      nome: 'Pedro', 
      idade: 19, 
      ano_escolar: '2ª Médio', 
      endereco: 'Av. Paulista, 1000'
    }
  ];
  
  constructor() {}

  ngOnInit() {
  }

}
