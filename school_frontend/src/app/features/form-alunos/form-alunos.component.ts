import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Aluno } from '../../models/Aluno';
import { AlunoService } from '../../services/aluno_service/aluno.service';

@Component({
  selector: 'form-alunos',
  templateUrl: './form-alunos.component.html',
  styleUrls: ['./form-alunos.component.scss']
})
export class FormAlunosComponent implements OnInit {

  public alunos: Aluno[] = [];
  public aluno!: Aluno;
  public alunoForm!: FormGroup;
  public modeSave = 'post';
  public visible: boolean = false;

  constructor(
    private fb: FormBuilder,
    private alunoService: AlunoService
  ) { 
    this.criarForm();
  }

  ngOnInit(): void {
    // Optional: Load existing students if needed
    // this.getAlunos();
  }

  criarForm() {
    this.alunoForm = this.fb.group({
      id: [0],
      nome: ['', Validators.required],
      idade: ['', Validators.required],
      endereco: ['', Validators.required],
      ano: ['', Validators.required],
    });
  }

  showDialog() {
    this.visible = true;
  }

  postAluno() {
    if (this.alunoForm.valid) {
      this.aluno = this.alunoForm.value;
      this.alunoService.postAluno(this.aluno).subscribe(
        (aluno: Aluno) => {
          this.alunos.push(aluno);
          console.log('Aluno posted:', aluno);
          this.alunoForm.reset();
        },
        error => {
          console.error('Error posting aluno:', error);
        }
      );
    }
  }
}
