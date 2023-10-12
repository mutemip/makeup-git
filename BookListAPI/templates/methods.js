// GET call
fetch('http://127.0.0.1:8000/api/menu-items')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

// POST, PUT and PATCH Calls
const payload = {
    "title": "Ambrosia Ice cream",
    "price": 5.00,
    "inventory": 100
}
const endpoint = 'http://127.0.0.1:8000/api/menu-items'
fetch(endpoint,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

// For PUT and PATCH calls, you just change the method from POST to PUT or PATCH. These requests typically operate on a single resource, which is identified by including an ID in the URL. Everything else remains the same. 



// 
const endpint = 'http://127.0.0.1:8000/api/menu-items/17'
fetch(endpoint,
    {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })


// Making authenticated calls with tokens
const endpont = 'http://127.0.0.1:8000/api/menu-items/17'
const token = “Some token”
fetch(endpoint,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authentictation': 'Bearer ' + token
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
