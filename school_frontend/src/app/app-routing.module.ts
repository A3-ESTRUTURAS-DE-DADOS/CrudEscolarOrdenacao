import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './features/main/main.component';
import { TableProvasComponent } from './features/table-provas/table-provas.component';
import { TableMateriasComponent } from './features/table-materias/table-materias.component';
import { TableAlunosComponent } from './features/table-alunos/table-alunos.component';

const routes: Routes = [
  {
    path: '',
    component: MainComponent,
    children: [
      { path: 'alunos', component: TableAlunosComponent },
      { path: 'materias', component: TableMateriasComponent },
      { path: 'provas', component: TableProvasComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
