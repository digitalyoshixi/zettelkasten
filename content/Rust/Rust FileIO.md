---
tags:
  - rust
---
# Read File as String
```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let file_contents = fs::read_to_string("info.txt")?;
    println!("info.txt content =\n{file_contents}");
    let lines : Vec<_> = file_contents.split("\n").collect();
    Ok(())
}
```