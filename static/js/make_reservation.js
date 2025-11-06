document.addEventListener('DOMContentLoaded', function () {
  const dateInput = document.getElementById('id_reservation_date');
  if (!dateInput) return;

  const today = new Date();
  const minDate = today.toISOString().split('T')[0];

  dateInput.setAttribute('min', minDate);
});