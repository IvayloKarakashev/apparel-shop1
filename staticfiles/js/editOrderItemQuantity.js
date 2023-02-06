let updateCartButtons = document.getElementsByClassName('update-cart')


for (let i = 0; i < updateCartButtons.length; i++) {
    updateCartButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        let size = this.dataset.size


        if (user === 'AnonymousUser') {
            console.log('anon')
        } else {
            updateUserQuantity(productId, action, size)
        }
    })
}


function updateUserQuantity(productId, action, size) {
    let url = '/update-item-quantity/'

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

