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
  const editAllergyCheckboxes = document.querySelectorAll('.allergy-checkbox'); // ✅ fixed variable name

  // Loop through edit buttons
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

      // Clear all allergy checkboxes first
      editAllergyCheckboxes.forEach(cb => cb.checked = false);

      // Re-check the user’s existing allergies if they have them
      allergies.forEach(id => {
        const checkbox = document.getElementById(`allergen_${id}`);
        if (checkbox) checkbox.checked = true;
      });

      console.log("Editing booking:", bookingId);
      console.log("Loaded allergies:", allergies);
    });
  });

  //Confirm before submitting edits
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
  };
