import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TableComponentComponent } from './table-component/table-component.component';

@NgModule({
    declarations: [
        TableComponentComponent
    ],
    imports: [
        CommonModule
    ],
    exports: [
        TableComponentComponent
    ]
})
export class TableModule {}