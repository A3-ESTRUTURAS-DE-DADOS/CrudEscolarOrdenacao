import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContentPageComponent } from './content-page/content-page-component/content-page.component';


@NgModule({
    declarations: [
        ContentPageComponent
    ],
    imports: [
        CommonModule
    ],
    exports: [
        ContentPageComponent
    ]
})
export class ContentModule { }