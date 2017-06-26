import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

import { HeroDetailComponent } from './herodetail/hero-detail.component';
import { HeroesComponent } from './heroes/heroes.component';
import { HeroService } from './service/hero.service';
import {RouterModule} from "@angular/router";

@NgModule({
  declarations: [
    AppComponent,
    HeroDetailComponent,
    HeroesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot([{
      path: 'heroes',
      component: HeroesComponent
    }])
  ],
  providers: [HeroService],
  bootstrap: [AppComponent]
})
export class AppModule { }
