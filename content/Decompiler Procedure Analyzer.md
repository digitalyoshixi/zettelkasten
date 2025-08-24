---
tags:
  - reverse_engineering
aliases:
  - CFG Analyzer
  - CFG Generator
  - Procedure Analyzer
---
A tool used to generate [[Control Flow Graph]].
# Motivation
A single instruction cannot be evaluated independently. This is because:
- Other instructions may affect the registers used in the current instruction
- Other instructions may branch to this instruction
![[Decompiler Procedure Analyzer-20250824150436830.webp]]
![[Decompiler Procedure Analyzer-20250824150446864.webp]]
# Process
### Finding Basic Blocks
We can find all [[Basic Block|Basic Blocks]] aswell as their predecessor and sucessors blocks with the pseudocode:
```c
Block *get_block_at(Address start_address)
{
    Block *block = find in BlockList a block for start_address
    if block == not found
	block = new Block at start_address
        blockList += block
    return block
}

CreateBasicBlocks(current_procedure)
{
    current_address = current_procedure->entry_address
    block = get_block_at(current_address)
    current_procedure->entry_block = block
    workList.push = current_address
    while workList not empty
        current_address = workList.pop
        block = get_block_at(current_address)
next:
        label = find label at address higher than current_address
        branch = find branch at address higher than current_address

        if label->address < branch->address_after_branch
            block->length = label->address - block->address
            current_address = label->address
	    next_block = get_block_at(current_address)
            next_block->preds += block
            block->succs += next_block
            block = next_block
	    goto next
	end if

	block->length = branch->address_after_branch - block->address
        if branch is return	// returns have no known destination
	    continue
        end if

	next_block = get_block_at(branch->destination)
        next_block->preds += block
        block->succs += next_block
        workList.push = branch->destination
        if branch is not conditional
            continue           // will resume from branch destination
        end if
	next_block = get_block_at(branch->address_after_branch)
        next_block->preds += block
        block->succs += next_block
        block = next_block
        current_address = block->address
        goto next
    end while

    sort blockList by block's start address
}
```