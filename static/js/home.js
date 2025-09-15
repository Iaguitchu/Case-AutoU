const form   = document.getElementById("composeForm");
const enviar = document.getElementById("enviar");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  enviar.disabled = true;
  enviar.style.backgroundColor = "#4f7dc7";

  const fd = new FormData(form);

  fetch("/", { method: "POST", body: fd })
    .then((resp) => {
      if (!resp.ok) {
        return resp.json().then((err) => {
          throw new Error(err.message || "Erro ao enviar");
        }).catch(() => {
          throw new Error("Erro ao enviar");
        });
      }
      return resp.json(); // lê o JSON de sucesso
    })
    .then((data) => {
      alert(data.message || "Enviado!");
      window.location.reload();
    })
    .catch((err) => {
      alert(err.message || "Erro ao enviar");
    })
    .finally(() => {
      enviar.disabled = false;
      enviar.style.backgroundColor = "#0b57d0";
    });
});
