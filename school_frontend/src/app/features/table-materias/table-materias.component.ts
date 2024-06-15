import { Component, OnInit } from '@angular/core';
import { Materia } from '../../models/Materia';
import { MateriaService } from '../../services/materia_service/materia.service';

@Component({
  selector: 'table-materias',
  templateUrl: './table-materias.component.html',
  styleUrls: ['./table-materias.component.scss']
})
export class TableMateriasComponent implements OnInit {

  materias: Materia[] = [];

  constructor(
    private materiaService: MateriaService
  ) { }

  ngOnInit(): void {
    this.getMateria();
  }

  getMateria(): void {
    this.materiaService.getMateria()
      .subscribe((response: any) => this.materias = response.Materias);
  }
}
