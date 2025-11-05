document.addEventListener('DOMContentLoaded', function() {
  const editModal = document.getElementById('editBookingModal');
  const editButtons = document.getElementsByClassName('edit-btn'); // plural!
  const editForm = document.getElementById('edit-reservation-form');

  if (!editModal || !editForm) return;

  const bootstrapModal = new bootstrap.Modal(editModal);

  const editDate = editForm.querySelector("#id_date");
  const editTimeSlot = editForm.querySelector("#id_time_slot");
  const editGuestNo = editForm.querySelector("#id_guests");
  const editAllergies = editForm.querySelector("#id_allergies");
  const editSpecialRequests = editForm.querySelector("#id_special_requests");

  // Delete modal setup
  const deleteModalEl = document.getElementById("deleteModal");
  const deleteButtons = document.getElementsByClassName("delete-btn");
  const deleteConfirm = document.getElementById("deleteConfirm");
  const deleteModal = deleteModalEl ? new bootstrap.Modal(deleteModalEl) : null;

  // Attach event listeners to all Edit buttons
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const bookingId = e.currentTarget.getAttribute("data-booking-id");
      const date = e.currentTarget.getAttribute("data-date");
      const time = e.currentTarget.getAttribute("data-time");
      const guests = e.currentTarget.getAttribute("data-guests");
      const special = e.currentTarget.getAttribute("data-special-requests");

      // Populate modal fields
      if (editDate) editDate.value = date;
      if (editTimeSlot) editTimeSlot.value = time;
      if (editGuestNo) editGuestNo.value = guests;
      if (editSpecialRequests) editSpecialRequests.value = special;

      // Store booking ID in a hidden field for the form
      const hiddenIdField = editForm.querySelector('input[name="booking_id"]');
      if (hiddenIdField) hiddenIdField.value = bookingId;

      // Show modal
      bootstrapModal.show();
    });
  }

  // Ask user to confirm deletion
  if (deleteConfirm && deleteModal) {
    for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
        const bookingId = e.currentTarget.getAttribute("data-booking-id");
        deleteConfirm.setAttribute("data-booking-id", bookingId);
        deleteModal.show();
      });
    }

    deleteConfirm.addEventListener("click", () => {
      const bookingId = deleteConfirm.getAttribute("data-booking-id");
    });
  }
});
