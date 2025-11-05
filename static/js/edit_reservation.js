document.addEventListener('DOMContentLoaded', function() {
  const editButtons = document.querySelectorAll('.edit-btn');
  const editModalEl = document.getElementById('editReservationModal');
  const editForm = document.getElementById('edit-reservation-form');

  if (!editButtons.length || !editModalEl || !editForm) return;

  const bookingIdField = editForm.querySelector('input[name="booking_id"]');
  const editDate = editForm.querySelector('#id_date');
  const editTimeSlot = editForm.querySelector('#id_time_slot');
  const editGuestNo = editForm.querySelector('#id_guests');
  const editSpecialRequests = editForm.querySelector('#id_special_requests');

  // Listen for edit button clicks
  editButtons.forEach(button => {
    button.addEventListener('click', function() {
      const bookingId = this.dataset.bookingId;
      const date = this.dataset.date;
      const time = this.dataset.time;
      const guests = this.dataset.guests;
      const special = this.dataset.specialRequests;

      // Fill modal fields
      if (bookingIdField) bookingIdField.value = bookingId;
      if (editDate) editDate.value = date;
      if (editTimeSlot) editTimeSlot.value = time;
      if (editGuestNo) editGuestNo.value = guests;
      if (editSpecialRequests) editSpecialRequests.value = special;

    });
  });
});

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
