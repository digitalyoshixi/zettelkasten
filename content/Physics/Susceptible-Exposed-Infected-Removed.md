---
tags:
  - biology
aliases:
  - SEIR
---
A method for modeling [[Epidemics]].
![[Susceptible-Exposed-Infected-Removed-20250228030446061.webp]]
# Process
1. Susceptible ($S$) - No contact with the virus
2. Exposed ($E$) - Caught the disease, no signed of being able to infect others yet
3. Infectious ($I$) - Able to infect others
4. Recovered ($R$) - No trace of infectious disease left
# Population
With $N$ as the total population,
$$N = S + E + I + R$$
# Other Formulas
- The rate of recovery is proportional to the number of infected and time
  $$\triangle R \sim \gamma I \triangle t$$
- The rate of infection is equal to those not currently infected and the number of exposed and time 
  $$\triangle I \sim -\gamma I \triangle t + \alpha E \triangle T $$
- The rate of exposed is proportional to $\beta :$ number of contacts per person per day, times those susceptible and the percentage of infected with time, minus those already exposed
  $$\triangle E \sim \beta S \frac{I}{N} \triangle t - \alpha E \triangle t$$