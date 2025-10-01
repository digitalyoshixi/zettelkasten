---
tags:
  - esolang
---
When two [[Tacit Link|Tacit Links]] with different [[Programming/Arity]] are piped side by side, they form a link chain.
# Example 
`+H` has the link `+` with arity 2 and `H` with arity 1.
This is an example of a 2-1 chain.
If 1 argument is passed then is then evaluated as `n + n/2`
You can read `+H` as 'plus itself halved'
If 2 arguments are passed then it is evaluated as `(a+b) / 2`
# Chain Types
### Niladic Chain
Since nilads are mostly literals, you would pass the nilad across the chain.
### Monadic Chain
- If the chain starts with a nilad, bring the nilad down the chain
- Always bring the single input - denoted as `w` down the chain aswell
Lets try `v` as the result on the chain `+²×`
As there is no nilad, we just say v is the input. `v = w`
Then, `v = w + w^2` for the monad `+²`
Then, `v = (w + w^2) × w`
### Dyadic Chain
For every odd dyad in the chain, it is evaluated as `(<input1> <dyad> <input2>)`
If `λ` is input1 and `ρ` is input2.
For example: `+×÷H`
`+` is evaluated first. `(λ + p)`
`×` is evaluated next. `(λ + p) × `
`÷` is evaluated next. `(λ + p) × (λ ÷ p)`
`H` is evaluated next. `(λ + p) × (λ ÷ p) / 2`

