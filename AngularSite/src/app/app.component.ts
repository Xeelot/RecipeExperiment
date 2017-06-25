import { Component } from '@angular/core';

const HEROES: Hero[] = [
  {id: 1, name: 'Jon Snow'},
  {id: 2, name: 'Danaeryus Stormborn'},
  {id: 3, name: 'Little Finger'}
];

export class Hero {
  id: number;
  name: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Game of Thrones';
  heroes = HEROES;
  selectedHero: Hero;

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  }
}


