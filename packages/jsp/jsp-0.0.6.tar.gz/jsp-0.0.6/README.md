## JSONPath CLI tool with syntax highlight

Basic example scenarios:

```shell
$ cat sample.json | jsp $.store.bicycle.color
"red"

$ cat sample.json | jsp $.store.book[*].title
"Sayings of the Century"
"Sword of Honour"
"Moby Dick"
"The Lord of the Rings"

$ cat sample.json | jsp $..book[?(@.category='fiction')].isbn
"0-553-21311-3"
"0-395-19395-8"
```

Simply format JSON input without specifying a JSONPath expression (also handles multiple JSON objects):
```shell
cat sample-multi.json | jsp
{"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95}
{"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99}
{"category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99}
{"category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99}
```

The original name of this project was meant to be JPT as JsonPath Tools, but PyPI had a same-named obsolete package. Therefore for now, this will run by the name JSP - hopefully noone remembers Java Server Pages anymore anyway 😀 