---
tags:
  - os
  - synchronization
---
There are a few problems that we face in synchronization that we combat with semaphores


### Bounded buffer problem/Producer consumer:

Suppose there is a buffer of n slots and each slot can store one unit of data. There are 2 processes: a producer process and a consumer process. The stipulations are as follows:

1. The producer can only insert data into an empty slot in the buffer.
    
2. The consumer can only remove data from a filled slot in the buffer.
    
3. Producer and consumer cannot insert and remove simultaneously.
    

  

To solve this problem we must use 3 semaphores:

1. m(mutex) - a binary semaphore for locking
    
2. Empty - a counting semaphore for the # of slots empty
    
3. Full - a counting semaphore for # of slots full.
    

Producer then follows these steps accordingly:

1. wait(empty) - wait for an empty slot
    
2. wait(mutex) - lock it
    
3. Add data
    
4. signal(mutex) - release lock
    
5. signal(full) - increment full
    

Consumer then follows these steps accordingly:

1. wait(full) - wait for a full slot
    
2. wait(mutex) - lock it
    
3. Remove data
    
4. signal(mutex) - release lock
    
5. signal(empty) increment empty
    

  

### Reader-Writers problem:

Suppose there is a database. There are some processes that read data, and others that write data. Stipulations are as follows:

1. Readers can only read data
    
2. Writers can only write data
    
3. If 2 readers read simultaneously, nothing is affected
    
4. If a writer and another reader/writer access the database simultaneously, data will be out of whack
    

To ensure that chaos does not ensue, we require writers to have exclusive access to the database.

  

To solve this problem we must use 2 semaphores and a integer value

1. m(mutex) - a binary semaphore for locking
    
2. wrt - a binary semaphore flag for writers
    
3. readcount - an integer variable that keeps track of how many processes are reading
    

Writer then follows these steps accordingly:

1. wait(wrt) - wait for write flag to open
    
2. Write data
    
3. signal(wrt) - allow another writer to write
    

Reader then follows these steps accordingly:

1. wait(mutex) - wait for someone to let you in
    
2. readcount++ - increment readcount
    
3. If readcount == 1 - only one reader
    
4. wait(wrt) - wait for writers to finish writing
    
5. signal(mutex) - allow other readers to read
    
6. Read data
    
7. wait(mutex) - other reader wants to read
    
8. readcount-- - decrement readcount
    
9. signal(wrt) - writer can write
    
10. signal(mutex) - another reader can read
    

  

### Dining-Philosophers problem:

Philosophers spend their whole life either thinking or eating. Suppose there are 5 philosophers, and 5 forks. The stipulations are as follows:

1. W![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9i_tmp_2c55726e6ed33a8f.png) hen philosophers are thinking, they don't interact.
    
2. If philosophers are eating, they must require 2 forks.
    
3. Philosopher cannot pick a fork that their neighbor is using
    
4. At most 2 philosophers can eat at the same time because there are 5 forks.
    

We must find a semaphore to allow us to make sure no 2 adjacent philosophers start eating

  

To solve this problem, we may use 5 semaphores. Each semaphore is a binary value for a fork. Represent each philosopher as a process and each fork as a semaphore.

Philosopher then follows these steps accordingly:

1. wait(fork[x]) - wait for a fork to be available
    
2. wait(fork[x+1%5]) - wait for a second fork to be available. Since we are 5 philosophers, the fifth philosopher grabs 1 and 5
    
3. Eat
    
4. signal(fork[x])
    
5. signal(fork[x+1%5])
    
6. Think
    

**But, this solution may also form a deadlock. Suppose all philosophers are hungry so they all grab their left fork. Now no forks are available and all philosophers are hungry. **

A solution you could have to the aforementioned deadlock is only allow 4 philosophers to sit. Always have more than 1 fork then there are philosophers.

An alternate solution could also not be a ravenous fool and checking if there are 2 forks beside you before picking them up.

Another last solution could be picking your right chopstick first.