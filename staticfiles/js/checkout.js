let useAddressButtons = document.getElementsByClassName('use-address')
let chooseCurrentAddressBtn = document.getElementById('choose-current-address')
let enterNewAddressBtn = document.getElementById('enter-new-address')
let form = document.getElementById('form')

let formLabelField = document.getElementById('id_label')


enterNewAddressBtn.addEventListener('click', function (event) {
    form.style.display = 'block'
    formLabelField.style.display = "none"
})

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
        let formLabelField = document.getElementById('id_label')


        form.style.display = 'none'
        formStateRegionField.value = savedStateRegionField
        formCityField.value = savedCityField
        formAddressField.value = savedAddressField
        formZipCodeField.value = savedZipCodeField


    })
}