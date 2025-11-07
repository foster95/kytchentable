document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('reservation-form');
  const dateInput = document.getElementById('id_reservation_date');

  // --- Set min date to today's LOCAL date ---
  if (dateInput) {
    // Make sure it's a date input
    if (dateInput.type !== 'date') dateInput.setAttribute('type', 'date');

    const d = new Date();
    const yyyy = d.getFullYear();
    const mm = String(d.getMonth() + 1).padStart(2, '0');
    const dd = String(d.getDate()).padStart(2, '0');
    const today = `${yyyy}-${mm}-${dd}`;

    dateInput.min = today;

    // If there's an initial value in the past, bump it up to today
    if (dateInput.value && dateInput.value < today) {
      dateInput.value = today;
    }

    // Guard against manual typing of past dates
    dateInput.addEventListener('change', function () {
      if (dateInput.value && dateInput.value < today) {
        dateInput.value = today;
        alert('You cannot choose a past date.');
      }
    });
  }

  // --- Form validation ---
  if (form) {
    form.addEventListener('submit', function (e) {
      if (!form.checkValidity()) {
        e.preventDefault();

        // Force tooltip to appear for validation
        const firstInvalid = form.querySelector(':invalid');
        if (firstInvalid) {
          firstInvalid.focus();
          firstInvalid.reportValidity();
        } else {
          form.reportValidity();
        }
      }
    });
  }
});


