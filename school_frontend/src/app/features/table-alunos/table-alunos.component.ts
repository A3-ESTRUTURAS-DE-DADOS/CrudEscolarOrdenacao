import { Component, OnInit } from '@angular/core';
import { Aluno } from '../../models/Aluno';
import { AlunoService } from '../../services/aluno_service/aluno.service';

@Component({
  selector: 'table-alunos',
  templateUrl: './table-alunos.component.html',
  styleUrls: ['./table-alunos.component.scss']
})
export class TableAlunosComponent implements OnInit {

  alunos: Aluno[] = [];

  constructor(private alunoService: AlunoService) { }

  ngOnInit(): void {
    this.getAlunos();
  }

  getAlunos(): void {
    this.alunoService.getAluno()
      .subscribe((response: any) => this.alunos = response.Alunos);
  }
}
