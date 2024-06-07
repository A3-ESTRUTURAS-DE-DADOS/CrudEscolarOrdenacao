import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponentComponent } from './navbar-component/navbar-component.component';
import { AvatarModule } from 'primeng/avatar';
import { AvatarGroupModule } from 'primeng/avatargroup';
import { MenuModule } from 'primeng/menu';
import { MenubarModule } from 'primeng/menubar';
import { BadgeModule } from 'primeng/badge';

@NgModule({
    declarations: [
        NavbarComponentComponent
    ],
    imports: [
        CommonModule,
        AvatarModule,
        AvatarGroupModule,
        MenuModule,
        MenubarModule,
        BadgeModule
    ],
    exports: [
        NavbarComponentComponent
    ]
})
export class NavbarModule { }