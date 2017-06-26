import { Injectable } from '@angular/core';
import { Hero } from '../data/hero';

const HEROES: Hero[] = [
  {id: 1, name: 'Jon Snow'},
  {id: 2, name: 'Danaeryus Stormborn'},
  {id: 3, name: 'Little Finger'}
];

@Injectable()
export class HeroService {
  getHeroes(): Promise<Hero[]> {
    return Promise.resolve(HEROES);
  }
  getHeroesSlowly(): Promise<Hero[]> {
    return new Promise(resolve => {
      // Simulate server latency with 2 second delay
      setTimeout(() => resolve(this.getHeroes()), 2000);
    });
  }
}
