console.log("✅ edit_reservation.js loaded");

// Edit Reservation Modal
document.addEventListener('DOMContentLoaded', function() {
  const editButtons = document.querySelectorAll('.edit-btn');
  const editModalEl = document.getElementById('editReservationModal');
  const editForm = document.getElementById('edit-reservation-form');

  const confirmModalEl = document.getElementById('confirmUpdateModal');
  const confirmModal = confirmModalEl ? new bootstrap.Modal(confirmModalEl) : null;
  const confirmUpdateBtn = document.getElementById('confirm-update-btn');

  if (!editButtons.length || !editModalEl || !editForm) return;

  const bookingIdField = editForm.querySelector('input[name="booking_id"]');
  const editDate = editForm.querySelector('#id_date');
  const editTimeSlot = editForm.querySelector('#id_time_slot');
  const editGuestNo = editForm.querySelector('#id_guests');
  const editSpecialRequests = editForm.querySelector('#id_special_requests');
  const editAllergyCheckboxes = document.querySelectorAll('.allergy-checkbox');
  const clearAllergiesBtn = document.getElementById('clear-allergies-button'); //

  // Clear allergies button — no confirmation
  if (clearAllergiesBtn) {
    clearAllergiesBtn.addEventListener('click', function() {
      editAllergyCheckboxes.forEach(cb => cb.checked = false);
      console.log("All allergies cleared instantly.");
    });
  }

  // Handle edit button clicks
  editButtons.forEach(button => {
    button.addEventListener('click', function() {
      const bookingId = this.dataset.bookingId;
      const date = this.dataset.date;
      const time = this.dataset.time;
      const guests = this.dataset.guests;
      const special = this.dataset.specialRequests || "";
      const allergies = this.dataset.allergies ? this.dataset.allergies.split(',') : [];

      // Fill modal fields
      if (bookingIdField) bookingIdField.value = bookingId;
      if (editDate) editDate.value = date;
      if (editTimeSlot) editTimeSlot.value = time;
      if (editGuestNo) editGuestNo.value = guests;
      if (editSpecialRequests) editSpecialRequests.value = special.trim();

      // Clear all checkboxes first
      editAllergyCheckboxes.forEach(cb => cb.checked = false);

      // Re-check existing allergies
      allergies.forEach(id => {
        const checkbox = document.getElementById(`allergen_${id}`);
        if (checkbox) checkbox.checked = true;
      });

      console.log("Editing booking:", bookingId);
      console.log("Loaded allergies:", allergies);
    });
  });

  // Confirm before submitting edits
  editForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Stop default submit

    if (confirmModal) {
      confirmModal.show(); 
    } else {
      if (confirm("Are you sure you want to update this reservation?")) {
        editForm.submit();
      }
    }
  });

  // When confirm modal "Yes" is clicked
  if (confirmUpdateBtn) {
    confirmUpdateBtn.addEventListener('click', function() {
      confirmModal.hide();
      editForm.submit();
    });
  }
});

// Delete Reservation Modal
const deleteButtons = document.querySelectorAll(".delete-btn");
const deleteForm = document.getElementById("delete-form");

if (deleteButtons.length && deleteForm) {
  deleteButtons.forEach(button => {
    button.addEventListener("click", function() {
      const bookingId = this.dataset.bookingId;
      deleteForm.action = `/my_reservations/delete_reservation/${bookingId}/`;
      console.log("Deleting booking:", bookingId);
    });
  });
}

// Don't allow people to book dates in the past — allow today
document.addEventListener('DOMContentLoaded', function () {
  function setMinDate() {
    const dateInput = document.getElementById('id_date');
    if (!dateInput) return;
    const today = new Date().toLocaleDateString('en-CA'); // e.g. 2025-11-06
    dateInput.setAttribute('min', today);
    console.log("📅 Min date set to:", today);
  }

  // 1️⃣ Run immediately (in case the element already exists)
  setMinDate();

  // 2️⃣ Also run every time the modal opens
  const editModal = document.getElementById('editReservationModal');
  if (editModal) {
    editModal.addEventListener('shown.bs.modal', setMinDate);
  }
});
