document.addEventListener("click", function (e) {
  // RESTAURAR
  var btnExcluir = e.target.closest(".btn-lixeira");
  if (btnExcluir) {
    var id = btnExcluir.dataset.id;

    if (!confirm("Excluir DEFINITIVAMENTE este e-mail? Esta ação não pode ser desfeita.")) {
      return;
    }

    fetch("/emails/" + id + "/apagar", {     // nome da rota sugerido
      method: "POST",
      headers: { "X-Requested-With": "fetch" }
    })
    .then(function (resp) {
      if (!resp.ok) throw new Error("Falha ao excluir definitivamente");
      location.reload();
    })
    .catch(function (err) {
      console.error(err);
      alert("Não foi possível excluir. Tente novamente.");
    });
  }
});