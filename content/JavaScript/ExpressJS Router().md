---
tags:
  - javascript
---
Can define behavior after recieving requests at a given route
# Route With Different Request Methods
```js
import express from 'express'

const router = express.router()
router.route("/")
	.get( (req, res) => res.send("hello world"))
	.post(UpdateDB)
```
# Route With URL Parameters
```js
import express from 'express'

const router = express.router()
router.route("/:id")
```
# Specific Requests
### Post
```node
// add a product
router.post('/', async (req, res) =>{
  try {
    const product = await Product.create(req.body);
    console.log(req.body)
    res.status(200).json(product);
  } catch (error) {
    res.status(500).json({message : error.message});
  }
});
```
### Get
```node
//get all products
router.get('/', async (req, res) => {
  try {
    const products = await Product.find({});
    res.status(200).json(products);
  } catch (error){
    res.status(500).json({message : error.message});
  }
```
### Put
```node
router.put('/:id', async (req, res) => {
  try {
    const { id } = req.params;  
    const product = await Product.findByIdAndUpdate(id, req.body); 
    if (!product){
      res.status(404).json({message : "product not found"});
      return 
    }
    const updatedProduct = await Product.findById(id);
    res.status(200).json(updatedProduct)
  } catch (error) {
      res.status(500).json({message : error.message})
  }
}
)
```
### Delete
```node
// delete a product
router.delete('/:id', async (req, res) => {
  try {
    const {id} = req.params; 
    const product = await Product.findByIdAndDelete(id);
    if (!product){
      res.status(404).json({message : "product not found"});
      return 
    }
    res.status(200).json(product);

  } catch (error) {
      res.status(500).json({message : error.message})
  }
}
)
```