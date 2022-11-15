let useAddressButtons = document.getElementsByClassName('use-address')

for (let i = 0; i < useAddressButtons.length; i++) {
    useAddressButtons[i].addEventListener('click', function (event) {

        let savedStateRegionField = event.target.parentElement.parentElement.querySelector('#saved-state-region').textContent
        let savedCityField = event.target.parentElement.parentElement.querySelector('#saved-city').textContent
        let savedAddressField = event.target.parentElement.parentElement.querySelector('#saved-address').textContent
        let savedZipCodeField = event.target.parentElement.parentElement.querySelector('#saved-zip-code').textContent

        let formStateRegionField = document.getElementById('id_state_region')
        let formCityField = document.getElementById('id_city')
        let formAddressField = document.getElementById('id_address')
        let formZipCodeField = document.getElementById('id_zip_code')

        formStateRegionField.value = savedStateRegionField
        formCityField.value = savedCityField
        formAddressField.value = savedAddressField
        formZipCodeField.value = savedZipCodeField

        console.log(event.target.parentElement.parentElement.dataset.profile)

    })
}