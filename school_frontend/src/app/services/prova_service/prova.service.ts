import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Prova } from '../../models/Prova';

@Injectable({
  providedIn: 'root'
})
export class ProvaService {

  baseURL = `${environment.urlAPI}`;

  constructor(private http: HttpClient) { }

  getProva(): Observable<Prova[]> {
    return this.http.get<Prova[]>(`${this.baseURL}/get/provas/`);
  }

  getProvaById(id: number): Observable<Prova> {
    return this.http.get<Prova>(`${this.baseURL}/get/provas/${id}`);
  }

  postProva(prova: Prova): Observable<Prova> {
    return this.http.post<Prova>(`${this.baseURL}/post/provas/`, prova);
  }

  putProva(prova: Prova): Observable<Prova> {
    return this.http.put<Prova>(`${this.baseURL}/put/provas/${prova.id}`, prova);
  }

  deleteProva(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseURL}/delete/provas/${id}`);
  }
}
