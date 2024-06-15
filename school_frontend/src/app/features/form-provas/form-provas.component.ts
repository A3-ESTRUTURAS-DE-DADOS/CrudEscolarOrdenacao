import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Prova } from '../../models/Prova';
import { ProvaService } from '../../services/prova_service/prova.service';

@Component({
  selector: 'form-provas',
  templateUrl: './form-provas.component.html',
  styleUrls: ['./form-provas.component.scss']
})
export class FormProvasComponent implements OnInit {

  public provas: Prova[] = [];
  public prova!: Prova;
  public provaForm!: FormGroup;
  public modeSave = 'post';
  public visible: boolean = false;

  constructor(
    private fb: FormBuilder,
    private provaService: ProvaService
  ) { 
    this.criarForm();
  }

  ngOnInit(): void {

  }

  showDialog() {
    this.visible = true;
  }

  criarForm() {
    this.provaForm = this.fb.group({
      id: [0],
      id_aluno: ['', Validators.required],
      id_materia: ['', Validators.required],
      nota: ['', Validators.required],
    });
  }

  postProva() {
    if (this.provaForm.valid) {
      this.prova = this.provaForm.value;
      this.provaService.postProva(this.prova).subscribe(
        (prova: Prova) => {
          this.provas.push(prova);
          console.log('Prova posted:', prova);
          this.provaForm.reset();
        },
        error => {
          console.error('Error posting prova:', error);
        }
      );
    }
  }
}
