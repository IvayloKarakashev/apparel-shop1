let selectAddressBtns = document.getElementsByClassName('select-address-btn')

for (let i = 0; i < selectAddressBtns.length; i++) {
    selectAddressBtns[i].addEventListener('click', function () {
        let addressId = this.dataset.addressid
        let url = '/select-address/'
        let redirect_url = '/checkout/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'addressId': addressId,
            })
        })
            // .then((response) => {
            //     return response.json()
            // })
            .then(() => {
                window.location.href = redirect_url
            })
    })
}