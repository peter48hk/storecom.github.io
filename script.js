// Function to add products to cart (simple demo)
let cart = [];

function addToCart(productName, productPrice) {
  cart.push({ name: productName, price: productPrice });
  alert(`${productName} has been added to your cart!`);
  console.log(cart); // For debugging, view cart in console
}
