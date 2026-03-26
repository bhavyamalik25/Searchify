document.addEventListener("DOMContentLoaded", () => {

  // ── Theme toggle ──────────────────────────────
  const saved = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", saved);
  updateToggleLabel(saved);

  document.getElementById("theme-toggle").addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
    updateToggleLabel(next);
  });

  function updateToggleLabel(theme) {
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = theme === "dark" ? "Light mode" : "Dark mode";
  }

  // ── Search box focus ──────────────────────────
  const box = document.querySelector(".search-box");
  if (box) box.focus();

  // ── Animate result cards ──────────────────────
  document.querySelectorAll(".result-card").forEach((card, i) => {
    card.style.opacity = 0;
    card.style.transform = "translateY(12px)";
    setTimeout(() => {
      card.style.transition = "opacity 0.3s ease, transform 0.3s ease";
      card.style.opacity = 1;
      card.style.transform = "translateY(0)";
    }, i * 80);
  });

});