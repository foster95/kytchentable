document.addEventListener('DOMContentLoaded', function () {
  // Find the reservation date field on the main booking form
  const dateInput = document.getElementById('id_reservation_date');
  if (!dateInput) return;

  // Get today's date
  const today = new Date();

  // Format as YYYY-MM-DD
  const minDate = today.toISOString().split('T')[0];

  // Set the minimum date to today
  dateInput.setAttribute('min', minDate);
});