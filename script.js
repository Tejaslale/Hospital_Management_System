document.addEventListener('DOMContentLoaded', function() {
    const addPatientForm = document.getElementById('add-patient-form');
    const searchPatientForm = document.getElementById('search-patient-form');
    const displayPatientsButton = document.getElementById('display-patients');

    addPatientForm.addEventListener('submit', function(event) {
        event.preventDefault();
        // Collect form data and send it to your backend
        const formData = new FormData(addPatientForm);
        fetch('/add-patient', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(data => {
              alert('Patient added successfully!');
              addPatientForm.reset();
          }).catch(error => {
              console.error('Error:', error);
          });
    });

    searchPatientForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const patientId = document.getElementById('search-id').value;
        fetch(`/search-patient?id=${patientId}`)
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('search-results');
                resultsDiv.innerHTML = `<p>Patient ID: ${data.id}</p>
                                        <p>Name: ${data.name}</p>
                                        <p>Email: ${data.email}</p>
                                        <p>Phone: ${data.phone}</p>
                                        <p>Address: ${data.address}</p>
                                        <p>Disease: ${data.disease}</p>`;
            }).catch(error => {
                console.error('Error:', error);
            });
    });

    displayPatientsButton.addEventListener('click', function() {
        fetch('/display-patients')
            .then(response => response.json())
            .then(data => {
                const listDiv = document.getElementById('patient-list');
                listDiv.innerHTML = data.map(patient => `<p>ID: ${patient.id}, Name: ${patient.name}</p>`).join('');
            }).catch(error => {
                console.error('Error:', error);
            });
    });
});
