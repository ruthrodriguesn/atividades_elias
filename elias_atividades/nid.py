<!DOCTYPE html>
.table-actions .btn{ padding: 8px 10px; font-size: 12px; border-radius: 8px; }


/* Responsivo */
@media (max-width: 900px){
.col-6{ grid-column: span 12; }
.col-4{ grid-column: span 12; }
.col-8{ grid-column: span 12; }
.form-header{ flex-direction: column; align-items: flex-start; }
.search-bar{ flex-direction: column; }
.search-bar input{ max-width: none; }
}
</style>
</head>
<body>
<!-- Topbar -->
<header class="topbar">
<div class="brand">
<div class="logo">SG</div>
<div>
<div class="title">SGU • Sistema de Gerenciamento de Usuários</div>
<small style="opacity:.8">Módulo: Cadastro & Lista de Usuários</small>
</div>
</div>
<nav>
<button class="nav-btn">Dashboard</button>
<button class="nav-btn" style="background: rgba(255,255,255,.12);">Usuários</button>
<button class="nav-btn">Equipamentos</button>
<button class="nav-btn">Sair</button>
</nav>
</header>


<main class="container">
<div class="section-title">Cadastro de Usuários</div>
<section class="card form-card">
<div class="form-header">
<h2>Cadastro de Usuários</h2>
<div class="actions">
<button class="btn secondary">Limpar</button>
<button class="btn primary">Cadastrar Usuário</button>
</div>
</div>


<div class="form-grid">
<div class="col-6">
<label for="nome">Nome Completo</label>
<input type="text" id="nome" placeholder="Ex.: Ana Silva" />
</div>
<div class="col-6">
<label for="email">E-mail</label>
<input type="email" id="email" placeholder="ana@empresa.com" />
</div>


<div class="col-4">
<label for="perfil">Perfil</label>
<select id="perfil">
<option value="">Selecione...</option>
<option>Administrador</option>
<option>Gestor</option>
<option>Operacional</option>
<option>Leitura</option>
</select>
</div>
<div class="col-4">
<label for="senha">Senha</label>
<input type="password" id="senha" placeholder="********" />
</div>
<div class="col-4">
<label for="confirmar">Confirmar Senha</label>
<input type="password" id="confirmar" placeholder="********" />
</div>


<div class="col-8">
<label for="departamento">Departamento (opcional)</label>
<input type="text" id="departamento" placeholder="Ex.: TI / Manutenção" />
</div>
<div class="col-4">
<label for="status">Status</label>
<select id="status">