---
tags:
  - programming
---
This is a [[Lazy Evaluation|Lazy Loading]] [[Statically Typed]] [[Functional Programming]] language with [[Type Inference]].
`.hs` [[File Extension]].
# Installation
```
sudo pacman -S ghc cabal-install ghc-static
```
# Compile & Link
```
ghc -dynamic file.hs
```
# Interactive [[Read-eval-print-loop|Repl]]
```
ghci
```
# Boilerplate
```haskell
module Main where

main :: IO ()
main = do  
    putStrLn "What's your name?"  
    name <- getLine 
    putStrLn ("Hello " ++ name) 
```
in `Main.hs`
# Concepts
- [[Referential Transparency]]
- [[Side Effects]]
- [[Glasgow Haskell Compiler Interactive|ghci]]
- [[Haskell Interface File]]
- [[Hoogle]]
### Essential
- [[Haskell Operations]]
- [[Haskell Type]]
- [[Haskell Boxed Types]]
- [[Haskell Unboxed Type|Haskell Primative]]
- [[Haskell Unit]]
- [[Haskell Typeclass]]
- [[Haskell Type Synonym]]
- [[Haskell data|Haskell Data Constructor]]
- [[Runtime System|RTS]]
- [[Haskell Monad]]
- [[Glasgow Haskell Compiler Interactive|ghci]]
- [[Haskell Tuple]]
- [[Haskell Pair]]
- [[Haskell List]]
- [[Haskell Polymorphism]]
- [[Haskell IO]]
- [[Haskell Variable]]
- [[Haskell Conditional]]
- [[Haskell Comment]]
- [[Haskell String]]
- [[Haskell Currying]]
- [[Haskell Pattern Matching]]
- [[Haskell Guards]]
- [[Haskell Let]]
- [[Haskell Where]]
- [[Haskell Import]]
- [[Haskell Section]]
### FP
- [[Haskell $]]
- [[Haskell Function]]
- [[Haskell Anonymous Functions]]
- [[Haskell Function Composition]]
### Specific [[Haskell Typeclass]]
- [[Haskell Show]]
- [[Haskell Maybe]]
### Haskell Libraries
- [[Haskell base]]
### Specific Functions
- [[Haskell succ]]
- [[Haskell min]]
- [[Haskell max]]
- [[Haskell div]]
- [[Haskell odd]]
- [[Haskell even]]
- [[Haskell compare]]
- [[Haskell sqrt]]
- [[Haskell head]]
- [[Haskell tail]]
- [[Haskell take]]
- [[Haskell drop]]
- [[Haskell fst]]
- [[Haskell snd]]
- [[Haskell lines]]
- [[Haskell readfile]]
- [[Haskell mod]]
- [[Haskell print]]
- [[Haskell null]]
- [[Haskell length]]
- [[Haskell data]]
- [[Haskell flip]]
- [[Haskell ap]]
- [[Haskell fix]]
- [[Haskell rec]]
- [[Haskell map]]
- [[Haskell zipWith]]
- [[Haskell filter]]
- [[Haskell concat]]
- [[Haskell Colon Operator]]
- [[Haskell choose]]
- [[Haskell swap]]