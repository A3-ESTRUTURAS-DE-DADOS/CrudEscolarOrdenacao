import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Materia } from '../../models/Materia';

@Injectable({
  providedIn: 'root'
})
export class MateriaService {

  baseURL = `${environment.urlAPI}`;

  constructor(
    private http: HttpClient
   ) { }

   getAluno(): Observable<Materia[]> {
    return this.http.get<Materia[]>(`$(this.baseURL)/get/materias/`);
  }

  postMateria(materia: Materia) {
    return this.http.post(this.baseURL, materia);
  }

  deleteMateria(id: number) {
    return this.http.delete(`$(this.baseURL)/${id}`);
  }
}
