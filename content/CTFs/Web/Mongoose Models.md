---
tags:
  - node
---
These are js files usually stored under a `models` folder.
![[Mongoose Models-20241027195131799.webp]]
Used as templates for objects stored in [[MongoDB]] to follow.
# Example Model Template
```js
const mongoose = require('mongoose')

const ProductSchema = mongoose.Schema(
    {
        name : {
            type : String,
            required : [true, "Product name is required"]
        },

        quantity : {
            type : Number,
            required : true,
            default : 0
        },

        price : {
            type : Number,
            require: true,
            default : 0
        },

        image : {
            type : String,
            required : false,
        }

    },
    {
        timestamps : true
    }

);

const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;
```
# Built-in Methods
Mongoose models have built-in methods to communicate with the mongodb database.
### model.create()
Input is a json which should match a similar structure to the product schema.
If it matches the product schema, then that input is created in the database
```js
const model = await Model.create({"hi" : "hello"});
```
### model.find()
Takes a query input and then searches the mongodb database for that input.
```node
const results = await Model.find({});
```
```node
const results = await Model.find({"name" : "david"})
```
### model.findById(id)
Takes the model's id and then returns the one it found.
```js
const results = await Model.findByID(id);
```
### model.findByIDAndUpdate(id, newvalue)
```js
const results = await Model.findByIDAndUpdate(id, newvalue);
```
### model.findByIDAndDelete(id)
```js
const results = await Model.findByIDAndDelete(id);
```