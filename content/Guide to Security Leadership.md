---
tags:
  - security
---
A talk at [[Toronto Area Security Klatch|TASK]] by Spencer Dossett
# Notes
- Three currencies: Money, Attention, Political capital
- Talk works best if your org is under 1000 humans, can have 1:1 decision makers, able to directly negotiate with vendors
- Money: budgets, spend, ROI
- Attention: shared, finite. Can earn, spend, but can over-use
	- How much effort you are asking decision makers to spend on this
- Political capital: Interpersonal trust within the organization. Must be built over-time.
### Money
- To gain trust:
	- Adopt orphan tools, you take it on. Now you manage that tool.
	- Example tool is 15k worth, you take it on, you are now worth 15k more
	- Become a responsible owner
- If you get a tool, then you need to allocate a budget. Your job is to find a precision of the budget, there is no way for you to get a deviation less than 10% from the actual budget.
	- Never bake-in discounts in budget
	- If they request more precise budget, just add more padding
	- Break down the budget into individual segments, so you can argue for each item individually
		- Azure -> AD Licenses, Defender. Break it down so you can have real conversations
	- Anything under $1000 a year, put it under the 'other tools' bucket
	- Break budget down into monthly
- If everything got approved - you asked for too little. You need to have a roadmap more than you can possibly afford. They need a rolling list of what they need when they talk to investors, customers, etc...

Example budget backlog format:

| Priority | Tool     | Category  | Per Month | Year   | Status   |
| -------- | -------- | --------- | --------- | ------ | -------- |
| Critical | EDR Tool | Detection | 1100      | 13,200 | Approved |

### Attention
- Security people bother people all the time, nobody wants to deal with security but they have to
- If people are glazing their eyes, just stop talking
- You are inherently asking somebody to change their mind to something that they believe in as a core
	- Some people dont believe in SSO, MFA
	- Beliefs require mental model reshaping, hard ask to rethink things
- Complex decisions are hard
	- A or B (easy)
	- A impacts x,y,z B impacts a,b,c (hard)
	- Simplify as much as possible
	- Give people shorter documents
- First mention you do is a casual one "this is what im thinking about"
- Keep stakeholders questions, use them when discussing to vendors, address them in next meeting
- If you have three things: A, B, C, Just ask for the biggest thing, i.e the most expensive ask
- Drop all the jargon, use simple words, jargon forces people to think
- Once you get the yes, remind 