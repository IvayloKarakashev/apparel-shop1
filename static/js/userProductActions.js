let updateCartButtons = document.getElementsByClassName('update-cart')
let updateWishListButtons = document.getElementsByClassName('update-wishlist')

// for (let i = 0; i < selectedSize.length; i++) {
//     selectedSize[i].addEventListener('click', function () {
//         let size = this.dataset.size
//         console.log(size)
//     })
// }

for (let i = 0; i < updateCartButtons.length; i++) {
    updateCartButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action


        if (user === 'AnonymousUser') {
            console.log('anon')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

for (let i = 0; i < updateWishListButtons.length; i++) {
    updateWishListButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action

        if (user === 'AnonymousUser') {
            console.log('anon')
        } else {
            updateUserWishList(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    let url = '/update-item/'
    let selectedSize = document.querySelector("div.size-box li[class='active'] a")
    let size = selectedSize.dataset.size

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
            'size': size
        })
    })
        .then((response) => {
            return response.json()
        })
        .then(() => {
            location.reload()
        })
}

function updateUserWishList(productId, action) {
    let url = '/update-wishlist/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
        .then((response) => {
            return response.json()
        })
        .then(() => {
            location.reload()
        })
}