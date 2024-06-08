import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TableComponentComponent } from './table-component/table-component.component';
import { TableModule } from 'primeng/table';

@NgModule({
    declarations: [
        TableComponentComponent
    ],
    imports: [
        CommonModule,
        TableModule
    ],
    exports: [
        TableComponentComponent
    ]
})
export class TableComponentModule {}