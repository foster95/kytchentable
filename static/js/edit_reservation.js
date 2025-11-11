// ===========================
// EDIT RESERVATION (AJAX)
// ===========================
document.addEventListener("DOMContentLoaded", function () {

    const editButtons = document.querySelectorAll(".edit-btn");
    const modalEl = document.getElementById("editReservationModal");
    const modal = new bootstrap.Modal(modalEl);

    const editForm = document.getElementById("edit-reservation-form");

    // --- All modal fields (STRICTLY inside modal) ---
    const bookingIdField = modalEl.querySelector('input[name="booking_id"]');
    const guestNameField = modalEl.querySelector("#id_guest_name");
    const guestEmailField = modalEl.querySelector("#id_guest_email");
    const guestPhoneField = modalEl.querySelector("#id_guest_phone");
    const dateField = modalEl.querySelector("#id_date");
    const timeField = modalEl.querySelector("#id_time_slot");
    const guestsField = modalEl.querySelector("#id_guests");
    const specialField = modalEl.querySelector("#id_special_requests");
    const allergyBoxes = modalEl.querySelectorAll(".allergy-checkbox");
    const clearBtn = modalEl.querySelector("#clear-allergies-button");

    // -------------------------------------------------
    // PREFILL WHEN "EDIT" IS CLICKED
    // -------------------------------------------------
    editButtons.forEach(btn => {
        btn.addEventListener("click", function () {

            // Text fields
            bookingIdField.value = this.dataset.bookingId;
            guestNameField.value = this.dataset.bookingName || "";
            guestEmailField.value = this.dataset.bookingEmail || "";
            guestPhoneField.value = this.dataset.bookingPhone || "";
            dateField.value = this.dataset.date || "";
            timeField.value = this.dataset.time || "";
            guestsField.value = this.dataset.guests || "";
            specialField.value = (this.dataset.specialRequests || "").trim();

            // Allergies
            allergyBoxes.forEach(cb => cb.checked = false);

            const allergies = this.dataset.allergies
                ? this.dataset.allergies.split(",")
                : [];

            allergies.forEach(id => {
                const box = modalEl.querySelector(`#allergen_${id}`);
                if (box) box.checked = true;
            });
        });
    });

    // -------------------------------------------------
    // CLEAR ALLERGIES
    // -------------------------------------------------
    if (clearBtn) {
        clearBtn.addEventListener("click", () => {
            allergyBoxes.forEach(cb => (cb.checked = false));
        });
    }

    // -------------------------------------------------
    // AJAX SAVE
    // -------------------------------------------------
    editForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(editForm);

        fetch(editForm.action, {
            method: "POST",
            body: formData,
            headers: { "X-Requested-With": "XMLHttpRequest" },
        })
            .then(res => res.json())
            .then(data => {

                const errorBox = modalEl.querySelector("#modal-errors");
                errorBox.innerHTML = "";

                if (data.success) {
                    modal.hide();
                    window.location.reload();
                    return;
                }

                // Show errors
                Object.entries(data.errors).forEach(([field, messages]) => {
                  messages.forEach(msg => {
                        errorBox.insertAdjacentHTML(
                            "beforeend",
                            `<div class="alert alert-danger py-1 mb-2">${msg}</div>`
                        );
                    });
                });
            })
    });

    // -------------------------------------------------
    // PREVENT PAST DATES
    // -------------------------------------------------
    const setMinDate = () => {
        const today = new Date().toLocaleDateString("en-CA");
        dateField.setAttribute("min", today);
    };

    setMinDate();
    modalEl.addEventListener("shown.bs.modal", setMinDate);
});
