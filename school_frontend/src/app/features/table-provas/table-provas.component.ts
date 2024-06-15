import { Component, OnInit } from '@angular/core';
import { Prova } from '../../models/Prova';
import { ProvaService } from '../../services/prova_service/prova.service';

@Component({
  selector: 'table-provas',
  templateUrl: './table-provas.component.html',
  styleUrls: ['./table-provas.component.scss']
})
export class TableProvasComponent implements OnInit {

  provas: Prova[] = []

  constructor(
    private provaService: ProvaService
  ) { }

  ngOnInit(): void {
    this.getProva();
  }

  getProva(): void {
    this.provaService.getProva()
      .subscribe((response: any) => this.provas = response.Provas);
  }
}
