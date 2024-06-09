import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Prova } from '../../models/Prova';

@Injectable({
  providedIn: 'root'
})

export class ProvaService {

  baseURL = `${environment.urlAPI}`;
  
  constructor(
    private http: HttpClient
  ) { }

  getProva(): Observable<Prova[]>{
    return this.http.get<Prova[]>(`$(this.baseURL)/get/provas/`);
  }

  postProva(prova: Prova) {
    return this.http.post(this.baseURL, prova);
  }

  deleteProva(id: number) {
    return this.http.delete(`$(this.baseURL)/${id}`);
  }
}
