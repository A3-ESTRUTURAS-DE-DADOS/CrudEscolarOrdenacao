import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { InputNumberModule } from 'primeng/inputnumber';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { DialogModule } from 'primeng/dialog';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import { DropdownModule } from 'primeng/dropdown';
import { RadioButtonModule } from 'primeng/radiobutton';
import { RatingModule } from 'primeng/rating';
import { ToolbarModule } from 'primeng/toolbar';
import { ConfirmationService } from 'primeng/api';
import { AvatarModule } from 'primeng/avatar';
import { AvatarGroupModule } from 'primeng/avatargroup';
import { MenuModule } from 'primeng/menu';
import { MenubarModule } from 'primeng/menubar';
import { BadgeModule } from 'primeng/badge';

import { TableProvasComponent } from './table-provas/table-provas.component';
import { TableAlunosComponent } from './table-alunos/table-alunos.component';
import { TableMateriasComponent } from './table-materias/table-materias.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MainComponent } from './main/main.component';
import { FormAlunosComponent } from './form-alunos/form-alunos.component';
import { FormMateriasComponent } from './form-materias/form-materias.component';
import { FormProvasComponent } from './form-provas/form-provas.component';

import { AlunoService } from '../services/aluno_service/aluno.service';
import { MateriaService } from '../services/materia_service/materia.service';
import { ProvaService } from '../services/prova_service/prova.service';

@NgModule({
    declarations: [
        TableProvasComponent,
        TableAlunosComponent,
        TableMateriasComponent,
        NavbarComponent,
        MainComponent,
        FormAlunosComponent,
        FormMateriasComponent,
        FormProvasComponent
    ],
    imports: [
        ReactiveFormsModule,
        CommonModule,
        FormsModule,
        InputTextModule,
        InputTextareaModule,
        InputNumberModule,
        ButtonModule,
        TableModule,
        DialogModule,
        ConfirmDialogModule,
        DropdownModule,
        RadioButtonModule,
        RatingModule,
        ToolbarModule,
        AvatarModule,
        AvatarGroupModule,
        MenuModule,
        MenubarModule,
        BadgeModule
    ],
    exports: [
        TableProvasComponent,
        TableAlunosComponent,
        TableMateriasComponent,
        NavbarComponent,
        MainComponent,
        FormAlunosComponent,
        FormMateriasComponent,
        FormProvasComponent
    ],
    providers: [
        ConfirmationService,
        AlunoService,
        MateriaService,
        ProvaService
    ]
})
export class FeaturesModule { }