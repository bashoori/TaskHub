document.addEventListener("DOMContentLoaded", () => {
  // Find your Services section (adjust selector if needed)
  const serviceSection = document.querySelector("#service, .service, section.service");

  if (!serviceSection) {
    console.warn("Service section not found.");
    return;
  }

  // Create the wrapper div (for alignment like hero)
  const ctaDiv = document.createElement("div");
  ctaDiv.className = "cta-buttons";

  // Create the appointment button
  const appointmentBtn = document.createElement("a");
  appointmentBtn.href = "#contact"; // or link to your booking form/page
  appointmentBtn.className = "btn primary";
  appointmentBtn.textContent = "Make an Appointment";

  // Append the button inside the wrapper
  ctaDiv.appendChild(appointmentBtn);

  // Insert under the Service section
  serviceSection.appendChild(ctaDiv);
});
