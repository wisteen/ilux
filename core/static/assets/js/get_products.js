// document.addEventListener("DOMContentLoaded", function () {
//     // const slider = document.getElementById("price-slider");
//     // const sliderMinValue = document.getElementById("slider-min-value");
//     // const sliderMaxValue = document.getElementById("slider-max-value");
//     const productsContainer = document.getElementById("products-container");
//     const ratingCheckboxes = document.querySelectorAll(".rating-checkbox");

//     let selectedRating = null;

//     // Handle rating filter change
//     ratingCheckboxes.forEach((filter) => {
//         filter.addEventListener("change", function () {
//             selectedRating = this.value; // Get the selected rating
//             // const [minPrice, maxPrice] = slider.noUiSlider.get();
//             // fetchProducts(Math.round(minPrice), Math.round(maxPrice), selectedRating);
//             fetchProducts(selectedRating);
//         });
//     });

//     // Function to fetch and update products
//     // async function fetchProducts(minPrice, maxPrice, rating) {
//     async function fetchProducts(rating) {
//         try {
//             // const response = await fetch(`/filter?min_price=${minPrice}&max_price=${maxPrice}&rating=${rating || ''}`);
//             const response = await fetch(`/filter?rating=${rating}`);
//             if (!response.ok) {
//                 throw new Error("Failed to fetch products");
//             }
//             const data = await response.text();
//             productsContainer.innerHTML = data; // Populate products container
//         } catch (error) {
//             console.error(error.message);
//         }
//     }

//     // Initialize noUiSlider
//     // noUiSlider.create(slider, {
//     //     start: [0, 10000], // Initial range values
//     //     connect: true,
//     //     range: {
//     //         min: 0,
//     //         max: 10000,
//     //     },
//     //     step: 100,
//     // });

//     // Handle slider updates
//     // slider.noUiSlider.on("update", function (values) {
//     //     sliderMinValue.textContent = Math.round(values[0]);
//     //     sliderMaxValue.textContent = Math.round(values[1]);
//     // });

//     // Handle slider change (trigger AJAX)
//     // slider.noUiSlider.on("change", function (values) {
//     //     const minPrice = Math.round(values[0]);
//     //     const maxPrice = Math.round(values[1]);
//     //     fetchProducts(minPrice, maxPrice, selectedRating);
//     // });
// });

document.addEventListener("DOMContentLoaded", function () {
    // Get all checkboxes
    const ratingCheckboxes = document.querySelectorAll(".rating-checkbox");
    const categoriesCheckboxes = document.querySelectorAll(".categories");
    const searchCategories = document.querySelector(".search-categories");
    const productsContainer = document.getElementById("product-container");
    const slider = document.getElementById("slider");
    const minValueElement = document.getElementById('min-value');
    const maxValueElement = document.getElementById('max-value');
    const stores = JSON.parse(document.getElementById("stores").textContent);

    let minValue = null;
    let maxValue = null;

    // noUiSllder
    noUiSlider.create(slider, {
        start: [200, 800],
        connect: true,
        range: {
            'min': 0,
            'max': 1000
        }
    });

    // Display the default values on page load
    slider.noUiSlider.on('update', function (values) {
        // Set the minimum and maximum values
        minValue = Math.floor(values[0]);
        maxValue = Math.ceil(values[1]);

        minValueElement.textContent = `$ ${minValue} -`;
        maxValueElement.textContent = `$ ${maxValue}`;
    });

    if (stores) {
        // Handles header search bar on page load.
        productsContainer.innerHTML = '';

        stores.forEach((product) => {
            const productCard = getProductCard(product)
            productsContainer.innerHTML += productCard;
        });

        // Scroll to top of the page.
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        // Fetches products on page load if not via header search bar.
        fetchProducts(stores);
    }

    // Attach event listener to the categories search box
    searchCategories.addEventListener("keydown", (event) => {
        handleSearchCategoriesFilter(event);
    });

    // Attach event listeners to each rating checkbox
    ratingCheckboxes.forEach(checkbox => {
        checkbox.addEventListener("change", makeRequest);
    });

    // Attach event listeners to each categories checkbox
    categoriesCheckboxes.forEach(checkbox => {
        checkbox.addEventListener("change", makeRequest);
    });

    // Runs after the user finishes interacting the slider.
    slider.noUiSlider.on('set', makeRequest);

    function makeRequest() {
        // Get selected ratings
        const selectedRatings = Array.from(ratingCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        // Get selected categories
        const selectedCategories = Array.from(categoriesCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        // Create query parameters
        const params = new URLSearchParams({
            ratings: selectedRatings.join(","),
            categories: selectedCategories.join(","),
            min_price: minValue,
            max_price: maxValue
        });

        // Submit request to the server
        fetch(`/api/filter/?${params}`, {
            method: "GET",
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error("Network response was not ok");
                }
            })
            .then(data => {
                console.log("Data from server:", data);
                // Update your UI with server response if necessary
                productsArray = data.products.products;

                productsContainer.innerHTML = '';
                productsArray.forEach((product) => {
                    // const productCard = `
                    //   <div class="col">
                    //     <div class="card card-product">
                    //       <div class="card-body">
                    //         <div class="text-center position-relative">
                    //           ${
                    //             product.badge
                    //               ? `<div class="position-absolute top-0 start-0">
                    //                    <span class="badge bg-${product.badge.type}">${product.badge.text}</span>
                    //                  </div>`
                    //               : ''
                    //           }
                    //           <a href="shop-single.html?id=${product.id}">
                    //             <img src="${product.image}" alt="${product.name}" class="mb-3 img-fluid" />
                    //           </a>
                    //           <div class="card-product-action">
                    //             <a href="#!" class="btn-action" data-bs-toggle="modal" data-bs-target="#quickViewModal">
                    //               <i class="bi bi-eye" data-bs-toggle="tooltip" title="Quick View"></i>
                    //             </a>
                    //             <a href="shop-wishlist.html" class="btn-action" data-bs-toggle="tooltip" title="Wishlist">
                    //               <i class="bi bi-heart"></i>
                    //             </a>
                    //             <a href="#!" class="btn-action" data-bs-toggle="tooltip" title="Compare">
                    //               <i class="bi bi-arrow-left-right"></i>
                    //             </a>
                    //           </div>
                    //         </div>
                    //         <div class="text-small mb-1">
                    //           <a href="#!" class="text-decoration-none text-muted">
                    //             <small>${product.category}</small>
                    //           </a>
                    //         </div>
                    //         <h2 class="fs-6">
                    //           <a href="shop-single.html?id=${product.id}" class="text-inherit text-decoration-none">
                    //             ${product.name}
                    //           </a>
                    //         </h2>
                    //         <div>
                    //           <small class="text-warning">
                    //             ${generateStars(product.rating)}
                    //           </small>
                    //           <span class="text-muted small">${product.rating} (${product.reviewsCount})</span>
                    //         </div>
                    //         <div class="d-flex justify-content-between align-items-center mt-3">
                    //           <div>
                    //             <span class="text-dark">$${product.price}</span>
                    //             ${
                    //               product.originalPrice
                    //                 ? `<span class="text-decoration-line-through text-muted">$${product.originalPrice}</span>`
                    //                 : ''
                    //             }
                    //           </div>
                    //           <div>
                    //             <a href="#!" class="btn btn-primary btn-sm">
                    //               <svg
                    //                 xmlns="http://www.w3.org/2000/svg"
                    //                 width="16"
                    //                 height="16"
                    //                 viewBox="0 0 24 24"
                    //                 fill="none"
                    //                 stroke="currentColor"
                    //                 stroke-width="2"
                    //                 stroke-linecap="round"
                    //                 stroke-linejoin="round"
                    //                 class="feather feather-plus">
                    //                 <line x1="12" y1="5" x2="12" y2="19"></line>
                    //                 <line x1="5" y1="12" x2="19" y2="12"></line>
                    //               </svg>
                    //               Add
                    //             </a>
                    //           </div>
                    //         </div>
                    //       </div>
                    //     </div>
                    //   </div>
                    // `;


                    const productCard = getProductCard(product);
              
                    productsContainer.innerHTML += productCard;
                });

                // Scroll to top of the page.
                window.scrollTo({ top: 0, behavior: 'smooth' });

                  // Helper function to generate star ratings
                function generateStars(rating) {
                    const fullStars = Math.floor(rating);
                    const halfStar = rating % 1 >= 0.5 ? 1 : 0;
                    const emptyStars = 5 - fullStars - halfStar;
                
                    return (
                    '<i class="bi bi-star-fill"></i>'.repeat(fullStars) +
                    '<i class="bi bi-star-half"></i>'.repeat(halfStar) +
                    '<i class="bi bi-star"></i>'.repeat(emptyStars)
                    );
                }
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
            });
    }

    function fetchProducts() {
        fetch('/api/filter/', {
            method: "GET",
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error("Network response was not ok");
                }
            })
            .then(data => {
                console.log("Data from server:", data);
                // Update your UI with server response if necessary
                productsArray = data.products.products;
    
                productsContainer.innerHTML = '';
                productsArray.forEach((product) => {
                    const productCard = getProductCard(product)
              
                    productsContainer.innerHTML += productCard;
                });
    
                // Scroll to top of the page.
                window.scrollTo({ top: 0, behavior: 'smooth' });
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
            });
    }

    function handleSearchCategoriesFilter(event) {
        if (event.key === 'Enter') {

            fetch(`/api/filter/?search=${searchCategories.value}`, {
                method: "GET",
            })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error("Network response was not ok");
                    }
                })
                .then(data => {
                    console.log("Data from server:", data);
                    // Update your UI with server response if necessary
                    productsArray = data.products.products;
        
                    productsContainer.innerHTML = '';
                    productsArray.forEach((product) => {
                        const productCard = getProductCard(product)
                  
                        productsContainer.innerHTML += productCard;
                    });
        
                    // Scroll to top of the page.
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                })
                .catch(error => {
                    console.error("There was a problem with the fetch operation:", error);
                });
        }
    }

    function getProductCard(product) {
        const productCard = `
            <div class="col-xs-12 col-md-3 mb-4"> <!-- Adjust column size (col-md-4 for 3 cards per row) -->
                <div class="card">
                    <img src="${product.image}" class="card-img-top" alt="${product.name}">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <div>
                            <small class="text-warning">
                                ${generateStars(product.average_rating)}
                            </small>
                            <span class="text-muted small ms-2">${product.average_rating}</span>
                        </div>
                        <p class="card-text">Price: $${product.price}</p>
                    </div>
                </div>
            </div>
        `;

        return productCard;
    }

    // Helper function to generate star ratings
    function generateStars(rating) {
        const fullStars = Math.floor(rating);
        const halfStar = rating % 1 >= 0.5 ? 1 : 0;
        const emptyStars = 5 - fullStars - halfStar;
    
        return (
        '<i class="bi bi-star-fill"></i>'.repeat(fullStars) +
        '<i class="bi bi-star-half"></i>'.repeat(halfStar) +
        '<i class="bi bi-star"></i>'.repeat(emptyStars)
        );
    }
});

