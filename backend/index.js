// app.js
const express = require('express');
const mongoose = require('mongoose');
const Product = require('./models/productModel');

const PORT = process.env.PORT || 3005;
const cors = require('cors');
const app = express();
app.use(express.json());
app.use(cors());
// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/grocerystore', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log('MongoDB Connection Error: ', err));

// Define routes
// Example:
  app.get('/getall', async (req, res) => {
    try {
      const products = await Product.find();
      res.json(products);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  });

app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Define a GET endpoint to check the number of units of a particular stock by its name
app.get('/stock/:name/units', async (req, res) => {
  try {
      const productName = req.params.name;
      const product = await Product.findOne({ name: productName });
      if (!product) {
          return res.status(404).json({ message: 'Product not found' });
      }
      res.json({ units: product.quantity });
  } catch (err) {
      res.status(500).json({ message: err.message });
  }
});



app.get('/stock/:name/expiry', async (req, res) => {
    try {
      const productName = req.params.name;
      const product = await Product.findOne({name: productName});
      if (!product) {
        return res.status(404).json({ message: 'Product not found' });
      }
      const today = new Date();
      const expiryDate = new Date(product.expiryDate);
      if (expiryDate < today) {
        return res.json({ expired: true });
      } else { 
        return res.json({ expired: false });
      }
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  });
  
app.post('/createproduct', async (req, res) => {
    try {
      const { name, price, expiryDate, manufactureDate, quantity } = req.body;
      const product = new Product({ name, price, expiryDate ,manufactureDate, quantity });
      await product.save();
      res.status(201).json(product);
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
});
  


// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
