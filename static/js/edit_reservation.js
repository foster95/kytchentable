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

      console.log("Editing booking:", bookingId);
      console.log("Time from button:", time);
      console.log("Guest count from button:", guests);
      console.log("Time options:", Array.from(editTimeSlot.options).map(o => o.value));
      console.log("Guest options:", Array.from(editGuestNo.options).map(o => o.value));

      console.log("Editing booking:", bookingId); 
    });
  });
});
