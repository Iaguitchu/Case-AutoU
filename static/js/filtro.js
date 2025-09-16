document.addEventListener("click", (e) => {
  if (e.target.classList.contains("btn-eye")) {
    const tr = e.target.closest("tr");
    tr.classList.toggle("expandido");
  }
});
