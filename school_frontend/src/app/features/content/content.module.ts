import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContentPageComponent } from './content-page/content-page-component/content-page.component';
import { ContentRoutingModule } from './content-routing.module';
import { NavbarModule } from '../navbar/navbar.module';
import { TableComponentModule } from '../table/table-component.module'

@NgModule({
    declarations: [
        ContentPageComponent,
    ],
    imports: [
        CommonModule,
        NavbarModule,
        TableComponentModule
    ],
    exports: [
        ContentPageComponent,
        ContentRoutingModule
    ]
})
export class ContentModule { }