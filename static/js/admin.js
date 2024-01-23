
function toggleSubMenu(submenuId) {
  const submenu = document.getElementById(submenuId);
  const isExpanded = submenu.classList.contains('show');

  // Recolhe todos os submenus
  const allSubmenus = document.querySelectorAll('.nav-pills .collapse');
  allSubmenus.forEach(submenu => {
    if (submenu.id !== submenuId) {
      submenu.classList.remove('show');
    }
  });

  // Alterna a visibilidade do submenu clicado
  if (isExpanded) {
    submenu.classList.remove('show');
    document.getElementById('pesquisaForm').style.display = 'none';
    document.getElementById('cadastrar-jogo-form').style.display = 'none';
  } else {
    submenu.classList.add('show');

    // Se o submenu "Pesquisa" for clicado, exibe o formulário de registro
    if (submenuId === 'submenu-jogos') {
      document.getElementById('pesquisaForm').style.display = 'block';
    } else {
      document.getElementById('pesquisaForm').style.display = 'none';
    }

    // Se o submenu "Cadastrar jogo" for clicado, exibe o formulário de cadastro de jogo
    if (submenuId === 'submenu-jogos' && isExpanded) {
      document.getElementById('cadastrar-jogo-form').style.display = 'block';
    } else {
      document.getElementById('cadastrar-jogo-form').style.display = 'none';
    }
  }
}

// Função para exibir formulários específicos
function showForm(formId) {
  document.getElementById('pesquisaForm').style.display = 'none';
  document.getElementById('cadastrar-jogo-form').style.display = 'none';
  document.getElementById(formId).style.display = 'block';
}
