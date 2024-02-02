// Função para verificar o estado do submenu ao carregar a página
function checkSubmenuState() {
  const submenuId = localStorage.getItem('submenuId');
  if (submenuId) {
    toggleSubMenu(submenuId);
  }
}

// Chame a função checkSubmenuState ao carregar a página
window.addEventListener('load', checkSubmenuState);

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
  

  if (submenuId === 'submenu-jogos' && clickedElementId !== 'pesquisa-jogo-btn') {
    // Exibe ou oculta o formulário de pesquisa conforme necessário
    document.getElementById('pesquisaForm').style.display = isExpanded ? 'none' : 'block';
  } else {
    document.getElementById('pesquisaForm').style.display = 'none';
  }


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
  const pesquisaForm = document.getElementById('pesquisaForm');
  const cadastrarJogoForm = document.getElementById('cadastrar-jogo-form');
  const resultadosPesquisa = document.getElementById('resultadosPesquisa');

  // Esconder todos os formulários e resultados de pesquisa
  pesquisaForm.style.display = 'none';
  cadastrarJogoForm.style.display = 'none';
  resultadosPesquisa.style.display = 'none';

  // Mostrar o formulário ou resultado específico com base no ID fornecido
  if (formId === 'pesquisaForm') {
    pesquisaForm.style.display = 'block';
    resultadosPesquisa.style.display = 'block'; // Mostrar resultados ao exibir o formulário de pesquisa
  } else if (formId === 'cadastrar-jogo-form') {
    cadastrarJogoForm.style.display = 'block';
  }

  // Limpar o campo de pesquisa sempre que o formulário de cadastro de jogo for exibido
  if (formId === 'cadastrar-jogo-form') {
    document.getElementById('termo_pesquisa').value = '';
  }


  // Armazene o estado do submenu no armazenamento local
  localStorage.setItem('submenuId', isExpanded ? '' : submenuId);
}



// Chame a função checkSubmenuState ao carregar a página
window.addEventListener('load', checkSubmenuState);

// Função para alternar a visibilidade do submenu
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


    // Se o submenu "Pesquisa Usuario" for clicado, exibe o formulário de registro
    if (submenuId === 'submenu-usuario') {
      document.getElementById('pesquisaFormUser').style.display = 'block';
    } else {
      document.getElementById('pesquisaFormUser').style.display = 'none';
    }
  // Armazene o estado do submenu no armazenamento local
  localStorage.setItem('submenuId', isExpanded ? '' : submenuId);
}

// function preencherFormularioEdicao(jogo_id,nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao) {
//   document.getElementById('nome_edicao'+jogo_id).value = nome;
//   document.getElementById('classificacao_edicao'+jogo_id).value = classificacao;
//   document.getElementById('ano_lancamento_edicao'+jogo_id).value = ano_lancamento;
//   document.getElementById('genero_edicao'+jogo_id).value = genero;
//   document.getElementById('modo_de_jogo_edicao'+jogo_id).value = modo_de_jogo;
//   document.getElementById('plataforma_edicao'+jogo_id).value = plataforma;
//   document.getElementById('publicadoras_edicao'+jogo_id).value = publicadoras;
//   document.getElementById('descricao_edicao'+jogo_id).value = descricao;

//   // Exibir o formulário de edição
//     document.getElementById('formularioEdicao'+jogo_id).style.display = 'block';
  

// }

// Exibe formulario de edição
function toggleFormularioEdicao(jogo_id, nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao) {
  // Obtenha a referência ao formulário de edição usando o ID
  var formularioEdicao = document.getElementById('formularioEdicao' + jogo_id);

  // Verifique se o formulário está atualmente visível
  var isVisivel = formularioEdicao.style.display === 'block';

  if (!isVisivel) {
    // Se o formulário não estiver visível, preencha os campos
    document.getElementById('nome_edicao' + jogo_id).value = nome;
    document.getElementById('classificacao_edicao' + jogo_id).value = classificacao;
    document.getElementById('ano_lancamento_edicao' + jogo_id).value = ano_lancamento;
    document.getElementById('genero_edicao' + jogo_id).value = genero;
    document.getElementById('modo_de_jogo_edicao' + jogo_id).value = modo_de_jogo;
    document.getElementById('plataforma_edicao' + jogo_id).value = plataforma;
    document.getElementById('publicadoras_edicao' + jogo_id).value = publicadoras;
    document.getElementById('descricao_edicao' + jogo_id).value = descricao;
  }

  // Alternar entre exibir e ocultar o formulário
  formularioEdicao.style.display = isVisivel ? 'none' : 'block';
}

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('atualizarBtn').addEventListener('click', function () {
    document.getElementById('formularioEdicao').style.display = 'none';
  });
});



function preencherFormularioEdicaoUsuario(email, nome, senha) {
// Obtenha a referência ao formulário de edição usando o ID
var formularioEdicaoUser = document.getElementById('formularioEdicaoUsuario'+email);

// Verifique se o formulário está atualmente visível
var Visivel = formularioEdicaoUser.style.display === 'block';

  if (!Visivel) {
    document.getElementById('email_edicao'+email).value = email;
    document.getElementById('nome_edicao'+email).value = nome;
    document.getElementById('senha_edicao'+email).value = senha;
  }

formularioEdicaoUser.style.display = Visivel ? 'none' : 'block';
  // Exibir o formulário de edição
}