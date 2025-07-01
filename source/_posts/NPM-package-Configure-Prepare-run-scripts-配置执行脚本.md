---
title: NPM package Configure Prepare run scripts[配置执行脚本]
tags:
  - NPM
categories:
  - 技术
date: 2025-07-01 15:24:51
---

The final thing is to add three scripts entries into our package.json:

```json
{
  "scripts": {
    "start": "npm run serve | npm run dev",
    "serve": "./node_modules/.bin/http-server -p 8080",
    "dev": "webpack-dev-server --progress --colors --port 8090"
  },
  "name": "basic-property-grid",
  "version": "0.1.0",
  "main": "index.js",
  "dependencies": {
    "react": "~0.11.2"
  },
  "devDependencies": {
    "webpack": "~1.4.4",
    "webpack-dev-server": "~1.6.5",
    "jsx-loader": "~0.11.2",
    "http-server": "~0.7.1"
  }
}
```

What we just did was to add 3 commands that can be run through npm run <cmd>.

> serve - npm run serve - just starts an http-server serving files from our local dir, running on port 8080 (it serves index.html).
>
> dev - npm run dev - starts webpack-dev-server on port 8090 which serves both the webpack-dev-server.js runtime and our bundle.js file.
>
> start - npm run start - command simply executes serve first and then starts the dev server.

Launch【运行】

Now we are ready:

```bash
$ npm run start
```

If everything is fine, you should open localhost:8080

