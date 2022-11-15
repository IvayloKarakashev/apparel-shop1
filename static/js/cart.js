let updateButtons = document.getElementsByClassName('update-cart')

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


// addToCartBtn.addEventListener('click', function () {
//     let productId = this.dataset.product
//     let action = this.dataset.action
//     console.log('productId:', productId, 'action:', action)
//
//     if (user === 'AnonymousUser') {
//         console.log('anon')
//     } else {
//         updateUserOrder(productId, action)
//     }
// })

function updateUserOrder(productId, action) {
    let url = '/update_item/'

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