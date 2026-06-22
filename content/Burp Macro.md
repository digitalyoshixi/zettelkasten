---
tags:
  - security
  - web
---
A tool to automate requests.
# Setup Automation
1. `Settings > Sessions > Macros > Add Macro > Select Requests`
2. If you want to derive custom parameters: `Click request > Configure Item > Add Parameter > Add > Highlight for it to automatically make regex > OK`, Configure next request but in `Parameter Handling > Click Param Name > Derive from previous request` this will replace url/body parameters with the corresponding name you set
3. `Settings > Sessions > Add Rule > Rule Actions > Add > Macro > Add the macro > OK > Scope > Set intruder only > Set URL scope > OK > OK`
4. Run intruder