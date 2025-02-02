---
tags:
  - obsidian
---
A method to turn your obsidian repo into a digital garden for the whole world to see.
https://quartz.jzhao.xyz/
# Create Quartz Repo
1. `git clone https://github.com/jackyzha0/quartz.git`
2. `cd quartz`
3. `npm i`
4. `npm audit fix`. You will have to update your `deploy.yml` node version later on if you do this
5. `npx quartz create`

Create and load it from your obsidian repository's folder.
Make sure there is an `index.md`
The Quartz repo is located at `~/quartz`
# Build Quartz Locally
`npx quartz build --serve`
visit localhost:8080
# Setup Github Repo
1. Create a new github repo without any README, license or .gitignore
2. copy the remote repository URL ![[Quartz-20240331235619667.webp]]
3. `git remote set-url origin REMOTE-URL`
4. `npx quartz sync --no-pull`
5. create the file `~/quartz/.github/workflows/deploy.yml`
6. write the following in deploy.yml: 
```
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - v4
 
permissions:
  contents: read
  pages: write
  id-token: write
 
concurrency:
  group: "pages"
  cancel-in-progress: false
 
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public
 
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
Remember to update the node version to whatever your actual node version is (`node --version`)
7. Go to your repo on the web > settings > pages > source > Github Actions
8. `npx quartz sync`
You can now visit your quartz website at `<github-username>.github.io/<repository-name>`
