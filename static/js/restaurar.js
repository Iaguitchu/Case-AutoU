document.addEventListener("click", function (e) {
  // RESTAURAR
  var btnRestaurar = e.target.closest(".btn-restaurar");
  if (btnRestaurar) {
    var id = btnRestaurar.dataset.id;

    fetch("/emails/" + id + "/restaurar", {
      method: "POST",
      headers: { "X-Requested-With": "fetch" }
    })
    .then(function (resp) {
      if (!resp.ok) throw new Error("Falha ao restaurar");
      // Atualiza a página pra refletir o estado
      location.reload();
    })
    .catch(function (err) {
      console.error(err);
      alert("Não foi possível restaurar. Tente novamente.");
    });
  }})