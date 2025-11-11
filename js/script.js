document.addEventListener("DOMContentLoaded", () => {
  // Load Header
  fetch("components/header.html")
    .then(res => res.text())
    .then(html => {
      document.getElementById("header-placeholder").innerHTML = html;

      // 🌍 Language Dropdown
      const langBtn = document.getElementById("lang-btn");
      const langMenu = document.getElementById("lang-menu");

      if (langBtn && langMenu) {
        langBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          langMenu.classList.toggle("show");
        });
        document.addEventListener("click", () => langMenu.classList.remove("show"));
      }

      // 🌀 Smooth Scroll for Header Nav
      document.querySelectorAll('.nav-links a[href^="#"], .get-started[href^="#"]').forEach(link => {
        link.addEventListener("click", (e) => {
          e.preventDefault();
          const target = document.querySelector(link.getAttribute("href"));
          if (target) target.scrollIntoView({ behavior: "smooth" });
        });
      });
    });

  // Load Footer
  fetch("components/footer.html")
    .then(res => res.text())
    .then(html => {
      document.getElementById("footer-placeholder").innerHTML = html;

      // Smooth scroll for footer links
      document.querySelectorAll('.footer a[href^="#"]').forEach(link => {
        link.addEventListener("click", (e) => {
          e.preventDefault();
          const target = document.querySelector(link.getAttribute("href"));
          if (target) target.scrollIntoView({ behavior: "smooth" });
        });
      });
    });
});
