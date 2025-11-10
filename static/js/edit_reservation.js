// Edit Reservation Modal
document.addEventListener('DOMContentLoaded', function() {
  const editButtons = document.querySelectorAll('.edit-btn');
  const editModalEl = document.getElementById('editReservationModal');
  const editForm = document.getElementById('edit-reservation-form');

  const confirmModalEl = document.getElementById('confirmUpdateModal');
  const confirmModal = confirmModalEl ? new bootstrap.Modal(confirmModalEl) : null;

  if (!editButtons.length || !editModalEl || !editForm) return;

  const bookingIdField = editForm.querySelector('input[name="booking_id"]');
  const editGuestName  = editForm.querySelector('#id_guest_name');
  const editGuestEmail = editForm.querySelector('#id_guest_email');
  const editGuestPhone = editForm.querySelector('#id_guest_phone');
  const editDate = editForm.querySelector('#id_date');
  const editTimeSlot = editForm.querySelector('#id_time_slot');
  const editGuestNo = editForm.querySelector('#id_guests');
  const editSpecialRequests = editForm.querySelector('#id_special_requests');
  const editAllergyCheckboxes = document.querySelectorAll('.allergy-checkbox');
  const clearAllergiesBtn = document.getElementById('clear-allergies-button');

  // Clear allergies button
  if (clearAllergiesBtn) {
    clearAllergiesBtn.addEventListener('click', function() {
      editAllergyCheckboxes.forEach(cb => cb.checked = false);
    });
  }

  // Handle edit button clicks
  editButtons.forEach(button => {
    button.addEventListener('click', function() {
      const bookingId = this.dataset.bookingId;
      const bookingName  = this.dataset.bookingName  || "";
      const bookingEmail = this.dataset.bookingEmail || "";
      const bookingPhone = this.dataset.bookingPhone || "";
      const date = this.dataset.date;
      const time = this.dataset.time;
      const guests = this.dataset.guests;
      const special = this.dataset.specialRequests || "";
      const allergies = this.dataset.allergies ? this.dataset.allergies.split(',') : [];

      if (bookingIdField) bookingIdField.value = bookingId;
      if (editGuestName)  editGuestName.value  = bookingName;
      if (editGuestEmail) editGuestEmail.value = bookingEmail;
      if (editGuestPhone) editGuestPhone.value = bookingPhone;
      if (editDate) editDate.value = date;
      if (editTimeSlot) editTimeSlot.value = time;
      if (editGuestNo) editGuestNo.value = guests;
      if (editSpecialRequests) editSpecialRequests.value = special.trim();

      // Reset allergies
      editAllergyCheckboxes.forEach(cb => cb.checked = false);
      allergies.forEach(id => {
        const checkbox = document.getElementById(`allergen_${id}`);
        if (checkbox) checkbox.checked = true;
      });
    });
  });

  // Delete Reservation Modal
  const deleteButtons = document.querySelectorAll(".delete-btn");
  const deleteForm = document.getElementById("delete-form");

  if (deleteButtons.length && deleteForm) {
    deleteButtons.forEach(button => {
      button.addEventListener("click", function() {
        const bookingId = this.dataset.bookingId;
        deleteForm.action = `/my_reservations/delete_reservation/${bookingId}/`;
      });
    });
  }

  // Don't allow people to book dates in the past — allow today
  function setMinDate() {
    const dateInput = document.getElementById('id_date');
    if (!dateInput) return;
    const today = new Date().toLocaleDateString('en-CA'); // e.g. 2025-11-06
    dateInput.setAttribute('min', today);
  }

  setMinDate();

  const editModal = document.getElementById('editReservationModal');
  if (editModal) {
    editModal.addEventListener('shown.bs.modal', setMinDate);
  }
});
