import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Materia } from '../../models/Materia';
import { MateriaService } from '../../services/materia_service/materia.service';

@Component({
  selector: 'form-materias',
  templateUrl: './form-materias.component.html',
  styleUrls: ['./form-materias.component.scss']
})
export class FormMateriasComponent implements OnInit {

  public materias: Materia[] = [];
  public materia!: Materia;
  public materiaForm!: FormGroup;
  public modeSave = 'post';
  public visible: boolean = false;

  constructor(
    private fb: FormBuilder,
    private materiaService: MateriaService
  ) { 
    this.criarForm();
  }

  ngOnInit(): void {
  }

  criarForm() {
    this.materiaForm = this.fb.group({
      id: [0],
      nome: ['', Validators.required],
    });
  }

  showDialog() {
    this.visible = true;
  }

  postMateria() {
    if (this.materiaForm.valid) {
      this.materia = this.materiaForm.value;
      this.materiaService.postMateria(this.materia).subscribe(
        (materia: Materia) => {
          this.materias.push(materia);
          console.log('Materia posted:', materia);
          this.materiaForm.reset();
        },
        error => {
          console.error('Error posting materia:', error);
        }
      );
    }
  }
}
