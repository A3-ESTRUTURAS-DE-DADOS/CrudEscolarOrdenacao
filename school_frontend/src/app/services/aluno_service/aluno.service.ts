import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Aluno } from '../../models/Aluno';

@Injectable({
  providedIn: 'root'
})
export class AlunoService {

  baseURL = `${environment.urlAPI}`;

  constructor(private http: HttpClient) { }

  getAluno(): Observable<Aluno[]> {
    return this.http.get<Aluno[]>(`${this.baseURL}/get/alunos/`);
  }

  getAlunoById(id: number): Observable<Aluno> {
    return this.http.get<Aluno>(`${this.baseURL}/get/alunos/${id}`);
  }

  postAluno(aluno: Aluno): Observable<Aluno> {
    return this.http.post<Aluno>(`${this.baseURL}/post/alunos/`, aluno);
  }

  putAluno(aluno: Aluno): Observable<Aluno> {
    return this.http.put<Aluno>(`${this.baseURL}/put/alunos/${aluno.id}`, aluno);
  }

  deleteAluno(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseURL}/delete/alunos/${id}`);
  }
}
