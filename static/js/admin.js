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

  // Armazene o estado do submenu no armazenamento local
  localStorage.setItem('submenuId', isExpanded ? '' : submenuId);
}


// function preencherFormularioEdicao(id, nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao) {
//   // Atualizar os campos do formulário com os dados do jogo
//   document.getElementById('jogo_id_edicao').value = id;
//   document.getElementById('nome_edicao').value = nome;
//   document.getElementById('classificacao_edicao').value = classificacao;
//   document.getElementById('ano_lancamento_edicao').value = ano_lancamento;
//   document.getElementById('genero_edicao').value = genero;
//   document.getElementById('modo_de_jogo_edicao').value = modo_de_jogo;
//   document.getElementById('plataforma_edicao').value = plataforma;
//   document.getElementById('publicadoras_edicao').value = publicadoras;
//   document.getElementById('descricao_edicao').value = descricao;

//   // Exibir o formulário de edição
//   document.getElementById('formularioEdicao').style.display = 'block';
// }


function preencherFormularioEdicao(nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao) {
  document.getElementById('nome_edicao').value = nome;
  document.getElementById('classificacao_edicao').value = classificacao;
  document.getElementById('ano_lancamento_edicao').value = ano_lancamento;
  document.getElementById('genero_edicao').value = genero;
  document.getElementById('modo_de_jogo_edicao').value = modo_de_jogo;
  document.getElementById('plataforma_edicao').value = plataforma;
  document.getElementById('publicadoras_edicao').value = publicadoras;
  document.getElementById('descricao_edicao').value = descricao;

  // Exibir o formulário de edição
  document.getElementById('formularioEdicao').style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function () {
  // Função para preencher o formulário de edição com dados do jogo
  
  // Adicione um manipulador de evento para o botão de atualização
  document.getElementById('atualizarBtn').addEventListener('click', function () {
    // Obtenha os dados do formulário de edição
    const dadosAtualizados = {
      jogo_id: document.getElementById('jogo_id_edicao').value,
      nome: document.getElementById('nome_edicao').value,
      classificacao: document.getElementById('classificacao_edicao').value,
      ano_lancamento: document.getElementById('ano_lancamento_edicao').value,
      genero: document.getElementById('genero_edicao').value,
      modo_de_jogo: document.getElementById('modo_de_jogo_edicao').value,
      plataforma: document.getElementById('plataforma_edicao').value,
      publicadoras: document.getElementById('publicadoras_edicao').value,
      descricao: document.getElementById('descricao_edicao').value,
    };

    fetch('/admin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dadosAtualizados),
    })
    fetch('/admin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dadosAtualizados),
    })
    .catch(error => {
      console.error('Erro na requisição:', error);
    });

    // Após a atualização, você pode ocultar o formulário de edição
    document.getElementById('formularioEdicao').style.display = 'none';
  });
});
