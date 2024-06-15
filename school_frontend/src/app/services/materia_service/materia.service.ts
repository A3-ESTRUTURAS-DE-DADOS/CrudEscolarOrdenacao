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

  constructor(private http: HttpClient) { }

  getMateria(): Observable<Materia[]> {
    return this.http.get<Materia[]>(`${this.baseURL}/get/materias/`);
  } 

  getMateriaById(id: number): Observable<Materia> {
    return this.http.get<Materia>(`${this.baseURL}/get/materias/${id}`);
  }

  postMateria(materia: Materia): Observable<Materia> {
    return this.http.post<Materia>(`${this.baseURL}/post/materias/`, materia);
  }

  putMateria(materia: Materia): Observable<Materia> {
    return this.http.put<Materia>(`${this.baseURL}/put/materias/${materia.id}`, materia);
  }

  deleteMateria(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseURL}/delete/materias/${id}`);
  }
}
