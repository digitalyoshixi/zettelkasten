---
tags:
  - rust
---
# Installation
`cargo add regex`
# Usage
```rust
 let re = Regex::new(r"mul\(\d*,\d*\)").unwrap();
    //let lines : Vec<_> = file_contents.split("\n").collect();
    let matches: Vec<&str> = re.find_iter(&file_contents).map(|m| m.as_str()).collect();
    println!("{:?}", matches);
    for matched in matches{
		println!("{}", matched);
	}

```