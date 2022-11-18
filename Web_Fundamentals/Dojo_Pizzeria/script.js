sizes = ["Small", "Medium", "Large", "X-Large"];
crusties = [
    "Hand Tossed",
    "Handmade Pan",
    "Crunchy Thin Crust",
    "Gluten Free Crust",
    "Brooklyn Style",
];
saucies = [
    "Marinara",
    "Honey BBQ",
    "Garlic Parmesan",
    "Alfredo Sauce",
    "Ranch",
];
cheesies = ["Light", "Normal", "Extra"];
toppers = [
    "Ham",
    "Beef",
    "Salami",
    "Pepperoni",
    "Italian Sausage",
    "Chicken",
    "Bacon",
    "Philly Steak",
    "Jalapeno Peppers",
    "Onions",
    "Banana Peppers",
    "Diced Tomatoes",
    "Black Olives",
    "Mushrooms",
    "Pineapple",
    "Green Peppers",
    "Spinach",
    "Roasted Red Peppers",
];

function pizzaOven(crustType, sauceType, cheese, toppings) {
    var pizza = {};
    pizza.Crust = crustType;
    pizza.Sauce = sauceType;
    pizza.Cheeses = cheese;
    pizza.Toppings = toppings;
    return pizza;
}
function randomPizza() {
    var pizza = [];
    pizza.Size = sizes[Math.floor(Math.random() * sizes.length)];
    pizza.Crust = crusties[Math.floor(Math.random() * crusties.length)];
    pizza.Cheese = cheesies[Math.floor(Math.random() * cheesies.length)];
    pizza.Sauce = saucies[Math.floor(Math.random() * saucies.length)];
    pizza.Toppings = toppers[Math.floor(Math.random() * toppers.length)];
    return pizza;
}
var pie1 = pizzaOven(
    "deep dish",
    "traditional",
    ["mozzarella"],
    ["pepperoni", "sausage"]
);
var pie2 = pizzaOven(
    "hand tossed",
    "marinara",
    ["mozzarella", "feta"],
    ["mushrooms", "olives", "onions"]
);
var pie3 = pizzaOven(
    "thin crust",
    "BBQ",
    ["mozzarella"],
    ["chicken", "green onion", "onions"]
);
var pie4 = pizzaOven(
    "hand tossed",
    "marinara",
    ["mozzarella", "parmesan"],
    ["mushrooms", "olives", "pepperoni"]
);

// console.log(pie1);
// console.log(pie2);
// console.log(sizes[Math.floor(Math.random() * sizes.length)]);
// console.log(randomPizza());
