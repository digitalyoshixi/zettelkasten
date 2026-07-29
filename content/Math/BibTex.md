---
tags:
  - math
  - academia
---
A tool and file format to describe references in conjunction with latex documents.
# Format
```
@entry{citekey,
	key1 = "value1",
	key2 = "value2"
}
```
- `entry` is an entry type, case insensitive
- `citekey` is the unique identifying key
- `keyN`,`valueN` are the value pairs
### Entry Types
- **[article](https://www.bibtex.com/e/article-entry/)**: any article published in a periodical like a journal article or magazine article
- **[book](https://www.bibtex.com/e/book-entry/)**: a book
- **booklet**: like a book but without a designated publisher
- **conference**: a conference paper
- **inbook**: a section or chapter in a book
- **incollection**: an article in a collection
- **inproceedings**: a conference paper (same as the conference entry type)
- **manual**: a technical manual
- **masterthesis**: a Masters thesis
- **misc**: used if nothing else fits
- **phdthesis**: a PhD thesis
- **proceedings**: the whole conference proceedings
- **techreport**: a technical report, government report or white paper
- unpublished:a work that has not yet been officially published
###