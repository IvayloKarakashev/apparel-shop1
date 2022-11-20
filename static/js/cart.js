let updateButtons = document.getElementsByClassName('update-cart')
let addToWishListButton = document.getElementById('add-to-wishlist')

for (let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        if (user === 'AnonymousUser') {
            console.log('anon')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

addToWishListButton.addEventListener('click', function () {
    let productId = this.dataset.product

    if (user === 'AnonymousUser') {
        console.log('anon')
    } else {
        updateUserWishList(productId)
    }
})

function updateUserOrder(productId, action) {
    let url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId, 'action': action
        })
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}

function updateUserWishList(productId) {
    let url = '/update-wishlist/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId
        })
    })
        .then((response) => {
            return response.json()
        })
}