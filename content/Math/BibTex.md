---
tags:
  - math
  - academia
---
A tool and file format to describe references in conjunction with latex documents.
# Format
```
@entry{citekey,
	key1 = {value1},
	key2 = {value2}
}
```
- `entry` is an entry type, case insensitive
- `citekey` is the unique identifying key
- `keyN`,`valueN` are the value pairs
### Entry Types
- `article`: any article published in a periodical like a journal article or magazine article
- `book`: a book
- `booklet`: like a book but without a designated publisher
- `conference`: a conference paper
- `inbook`: a section or chapter in a book
- `incollection`: an article in a collection
- `inproceedings`: a conference paper (same as the conference entry type)
- `manual`: a technical manual
- `masterthesis`: a Masters thesis
- `misc`: used if nothing else fits
- `phdthesis`: a PhD thesis
- `proceedings`: the whole conference proceedings
- `techreport`: a technical report, government report or white paper
- `unpublished`: a work that has not yet been officially published
### Citekey
Most common format is:
```
lastname_of_first_author_yearnumber
```
### Field Types
- `address`: address of the publisher or the institution
- `annote`: an annotation
- `author`: list of authors of the work
- `booktitle`: title of the book
- `chapter`: number of a chapter in a book
- `edition`: edition number of a book
- `editor`: list of editors of a book
- `howpublished`: a publication notice for unusual publications
- `institution`: name of the institution that published and/or sponsored the report
- `journal`: name of the journal or magazine the article was published in
- `month`: the month during the work was published
- `note`: notes about the reference
- `number`: number of the report or the issue number for a journal article
- `organization`: name of the institution that organized or sponsored the conference or that published the manual
- `pages`: page numbers or a page range
- `publisher`: name of the publisher
- `school`: name of the university or degree awarding institution
- `series`: name of the series or set of books
- `title`: title of the work
- `type`: type of the technical report or thesis
- `volume`: volume number
- `year`: year the work was published
- `doi`: DOI number (like 10.1038/d41586-018-07848-2)
- `issn`: ISSN number (like 1476-4687)
- `isbn`: ISBN number (like 9780201896831)
- `url`: URL of a web page