---
tags:
  - cpp
---
In a campaign to avoid using short and long integers, we declare our own widths.
Exists within the [[stdint.h]] header
They will have the same size on any architecture.

| Name | Type | Range | Notes |
| ---- | ---- | ---- | ---- |
| std::int8_t | 1 byte signed | -128 to 127 | Treated like a signed char on many systems. See note below. |
| std::uint8_t | 1 byte unsigned | 0 to 255 | Treated like an unsigned char on many systems. See note below. |
| std::int16_t | 2 byte signed | -32,768 to 32,767 |  |
| std::uint16_t | 2 byte unsigned | 0 to 65,535 |  |
| std::int32_t | 4 byte signed | -2,147,483,648 to 2,147,483,647 |  |
| std::uint32_t | 4 byte unsigned | 0 to 4,294,967,295 |  |
| std::int64_t | 8 byte signed | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |  |
| std::uint64_t | 8 byte unsigned | 0 to 18,446,744,073,709,551,615 |  |

# Fast Integers
C++ has these default integer datatypes.
std::int_fast#\_t and std::uint_fast#\_t
**\#** is the number of bytes you want your digit in.
Fast wont always allocate the exact # of bytes you want, it will allocate the quickest that will contain AT LEAST the # of bytes you wanted.

For example, std::int_fast16_t will result in 32bits being allocated.
# Least Integers
std::int_least#\_t and std::uint_least#\_t
do a similar checking method to fast, however this time, they are looking to see if its possible to follow your rule 100%.

For example, std::int_fast16_t will usually just allocate 16 bits.


Fast and least integers are often confused with Char types. Dont use these if you can choose not to.