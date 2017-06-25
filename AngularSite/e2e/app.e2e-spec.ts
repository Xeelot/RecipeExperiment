import { CookieRecipeTrackerPage } from './app.po';

describe('cookie-recipe-tracker App', () => {
  let page: CookieRecipeTrackerPage;

  beforeEach(() => {
    page = new CookieRecipeTrackerPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
