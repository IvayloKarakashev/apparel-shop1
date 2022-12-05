let updateCartButtons = document.getElementsByClassName('update-cart')


for (let i = 0; i < updateCartButtons.length; i++) {
    updateCartButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        let quantity = document.getElementsByClassName('input-number')[0].value
        console.log(quantity)


        if (user === 'AnonymousUser') {
            console.log('anon')
        } else {
            addProductToCart(productId, action, quantity)
        }
    })
}


function addProductToCart(productId, action, quantity) {
    let url = '/add-to-cart/'
    let selectedSize = document.querySelector("div.size-box li[class='active'] a")
    let temp
    try {
        temp = selectedSize.dataset.size
    } catch {
        alert('Please select size.')
        return
    }
    let size = temp

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            // 'action': action,
            'size': size,
            'quantity': quantity
        })
    })
        .then((response) => {
            return response.json()
        })
        // .then(() => {
        //     location.reload()
        // })
}

