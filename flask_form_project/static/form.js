document.addEventListener('DOMContentLoaded', function() {
    const divisionSelect = document.getElementById('division');
    const productSelect = document.getElementById('product');
    const osSelect = document.getElementById('os');
    const osVersionSelect = document.getElementById('osVersion');
    const regionSelect = document.getElementById('region');
    const requesterInput = document.getElementById('requester'); // Requester field

    // Handle Division change (populate Product)
    divisionSelect.addEventListener('change', function() {
        updateProductOptions();
    });

    // Handle OS change (populate OS Version)
    osSelect.addEventListener('change', function() {
        updateOSVersionOptions();
    });

    // Handle Product change (populate Region)
    productSelect.addEventListener('change', function() {
        updateRegionOptions();
    });

    // Initial population of dropdowns based on default values
    updateProductOptions();
    updateOSVersionOptions();
    updateRegionOptions();

    // Function to update Product options based on selected Division
    function updateProductOptions() {
        const division = divisionSelect.value;
        let productOptions = [];

        if (division === 'abc') {
            productOptions = ['abc1', 'abc2'];
        } else if (division === 'xyz') {
            productOptions = ['xyz1', 'xyz2'];
        } else if (division === 'lol') {
            productOptions = ['lol1', 'lol2'];
        }

        // Clear current product options
        productSelect.innerHTML = '';
        // Add new options
        productOptions.forEach(function(option) {
            let optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            productSelect.appendChild(optionElement);
        });
    }

    // Function to update OS Version options based on selected OS
    function updateOSVersionOptions() {
        const os = osSelect.value;
        let osVersionOptions = [];

        if (os === 'Redhat') {
            osVersionOptions = ['8', '9'];
        } else if (os === 'Windows') {
            osVersionOptions = ['2023', '2025'];
        }

        // Clear current OS version options
        osVersionSelect.innerHTML = '';
        // Add new options
        osVersionOptions.forEach(function(option) {
            let optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            osVersionSelect.appendChild(optionElement);
        });
    }

    // Function to update Region options based on selected Product
    function updateRegionOptions() {
        const product = productSelect.value;
        let regionOptions = ['us-east-1', 'ap-south-1'];

        // Clear current region options
        regionSelect.innerHTML = '';
        // Add new options
        regionOptions.forEach(function(option) {
            let optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            regionSelect.appendChild(optionElement);
        });
    }

    // Handle form submission
    document.getElementById('requestForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        var formData = new FormData(this);

        // Add custom fields (checkboxes)
        formData.append('monitoring', document.getElementById('monitoring').checked ? 'true' : 'false');
        formData.append('backup', document.getElementById('backup').checked ? 'true' : 'false');

        // Convert FormData to JSON
        var formDataObj = {};
        formData.forEach(function(value, key) {
            formDataObj[key] = value;
        });

        // Log the data to the console for debugging
        console.log("Form Data:", formDataObj);

        // Send the data to the server (or save it to a file)
        // For example, you can use fetch() to send this data to your server:
        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formDataObj)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Form successfully submitted', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

