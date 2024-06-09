import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Aluno } from '../../models/Aluno';

@Injectable({
  providedIn: 'root'
})

export class ServiceService {

  baseURL = `${environment.urlAPI}`;

  constructor(
    private http: HttpClient
  ) { }

  getAluno(): Observable<Aluno[]> {
    return this.http.get<Aluno[]>(this.baseURL);
  }

  postAluno(aluno: Aluno) {
    return this.http.post(this.baseURL, aluno);
  }

  deleteAluno(id: number) {
    return this.http.delete(`$(this.baseURL)/${id}`);
  }
}
