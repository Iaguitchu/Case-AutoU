const botao = document.getElementById("botao_mensagem");
const composeForm = document.getElementById("composeForm");
const fechar = document.getElementById("fechar-email");

botao.addEventListener("click", () => {
  if (composeForm.style.display === "flex") {
    composeForm.style.display = "none";
  } else {
    composeForm.style.display = "flex";
  }
});

fechar.addEventListener("click", () => {
    composeForm.reset();
    composeForm.style.display = "none";
});