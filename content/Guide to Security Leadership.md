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
- Have a cut-line for budget for the tools you are unable to afford
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
- Once you get the yes, remind them that this is a good decision and give them space - kind of hard during crunch time
- The ask template:
	- Ask: I am requesting approval to purchase [TOOL] for [USE-case]
	- What is it: [Tool] is a [category] solution that [solves specific problem] addresses [gap/risk/inefficiency] we currently have with [current state]
	- Cost: annual: [annual], delta to budget
	- Alternatives considered: [Vendor B], [C], status quo
	- Next steps: upon approval, procurement step [date] -> on-boarding [date] -> live by [date]
- Email should be short
- If they are asking more questions, indicator that you missed something in the original email. If you are getting tons of questions back, signals that this might be a no.
- If little questions, you either get yes, or nothing. You get nothing if something happens in the company you don't get visibility in.
### Political Capital
- Doing a good job $\neq$ political capital
- Political capital is other people seeing/feeling you are doing a good job
- Sources:
	- Your role itself (cyber roles are expensive by default)
	- Incidents and events, when something bad happens and everyone looks to you
- Methods:
	- Radical transparency: show your whole process
		- Identify risks you are not going to solve, tell people you are going to accept those risks
	- Risk comparison technique: People understand small risks better than abstract structural ones. Use familiar risks as an anchor
		- X is a concern, but I am actually 10x more worried about this risk Y because ...
		- Establishes a baseline to measure other risks by
	- First 90 days:
		- Don't make big decisions unless you have to
		- Listen a lot, talk to people, map landscape (this never ends)
		- Open door policy, make time and space to talk to whoever wants to chat
			- Sometimes people just come to you with a massive problem that is super important
	- Security allies, you want to have 1:1s with:
		- Accounting (controlling ledger)
		- Legal (sign-off on contracts)
		- IT (owns infra)
		- HR (controls onboarding, offboarding)
	- Share all decisions as reluctant conclusions
		- Organization got to where it is based off blood sweat tears of others. When you change things you are stepping over their work
		- Developer team spends effort on a tool, new tool comes in, their previous work is for naught
	- Take feedback especially when it sucks
		- As soon as you change things you get feedback, even if you did everything perfect you are going to get feedback
		- Don't act like some feedback isn't helpful. Show that you accept all feedback
### Bonus
- Picking vendors:
	- Pick what solves the problem
	- Find out how to afford this, change budget, etc
	- Find other options and keep this as a comparison option for negotiating
	- Find middle-of-the-line options as back-up
- If you get a budget constraint, just bring those problems to the vendor, sometimes they can help you
- If you are buying, don't let them sell to you, tell them what you are buying
	- What you want, what you need from them
	- Actively buy
	- Be transparent, tell them you are going to other vendors as well, these are the problems, don't need anything else
	- Vendors that say they can't do X, then these vendors are showing you a level of transparency that is rare
	- Keep asking until they tell you know, find the edge
	- Tell them 'I am trying to find the edge of where your solution is, where does it end?'
	- Keep decision makers off the calls as they complicate things
		- Same as the reason why you don't review your own code
	- Always do a proof of concept/value. 9/10 it confirms things
		- Organization shows you what works, only way you can gut-check that things are there
		- Vendors that know what they are doing will comply with a POC
	- Push pricing near the end, ready to buy when you are ready to buy
- Never negotiate human prices (if you are paying for humans). If you pay cheap for humans, then you get low-quality human work
- Fixed-cost tools are better to negotiate
- Anything under 5K a year is not worth your time to negotiate
- Negotiate on exclusive feature sets, adding/removing more features is usually not that expensive for a vendor
- Use the cut line in budget as a negotiation tool, you tell them that you must weight this cut-line in this decision. We are not making up a false negotiation tactic
- Give them your problems, not all vulnerabilities and security incidents but a high-level overview
- Some vendors ask "what are you security gaps?" - don't tell them this is stupid. Ask them how they solve a specific problem
### Post-purchase
- Once you sign a deal, buyers remorse sets in, they start seeing the bills
- Keep selling internally, remind people when wins happen because of a vendor/solution
- Remind decision makers they feel good about this decision "we would have had a really bad time, but we now have an uncomfortable time because of X decision"
- Show the business the line of what you are getting
	- What they asked for: ...
	- What I asked for: ...
	- What i got: ...
- Evaluate the vendor on how they respond to problems
	- Are they transparent
	- Are they absorbing feedback about problems?