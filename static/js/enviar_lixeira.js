document.querySelectorAll(".btn-lixeira").forEach(function(btn) {
  btn.addEventListener("click", function() {
    var id = btn.dataset.id;
    console.log(id)

    fetch("/emails/" + id + "/excluir", {
      method: "POST",
      headers: { "X-Requested-With": "fetch" }
    })
    .then(function(response) {
      if (!response.ok) {
        throw new Error("Erro ao excluir");
      }
       location.reload();
    })
    .catch(function(error) {
      alert("Erro ao excluir. Veja o console.");
      console.error(error);
    });
  });
});
