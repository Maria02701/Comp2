#Importando a biblioteca Tkinter
import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image
import csv
import re
import os
from datetime import datetime

# Classe para a janela de login
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login de Usuário")
        self.geometry("350x150")
        self.resizable(False, False)
        
        self.login_attempts = 0

        self.create_widgets()

    def login(self):
        # Função para realizar o login do usuário
        username = self.user_entry.get()
        password = self.password_entry.get()

        if username == "user" and password == "123" or self.check_psicologo(username, password):
            self.destroy()
            MainWindow()
        else:
            self.login_attempts += 1
            if self.login_attempts == 3:
                messagebox.showerror("Erro", "Número máximo de tentativas excedido.")
                self.destroy()
            else:
                messagebox.showwarning("Aviso", "Credenciais inválidas. Tente novamente.")
                
    def limparlogin(self):
        # Função para limpar os campos de login
        self.user_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def check_psicologo(self, username, password):
        # Função para verificar se o usuário é um psicólogo válido
        with open('psicólogos.txt', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[4] == username and row[5] == password:
                    return True
        return False

    def encerrar_aplicacao(self):
        # Função para encerrar a aplicação
        self.destroy()

    def create_widgets(self):
        # Imagem do lado esquerdo
        self.photo = tk.PhotoImage(file="Trabalho Final/Imagens/Login-32.png")
        img_label = tk.Label(self, image=self.photo)
        img_label.image = self.photo
        img_label.place(x=10, y=45)

        # LabelFrame para inserir os dados de login
        login_frame = tk.LabelFrame(self, text="Insira seus dados", padx=10, pady=10)
        login_frame.place(x=53, y=7)

        # Campo de entrada do usuário
        user_label = tk.Label(login_frame, text="Usuário:")
        user_label.grid(row=0, column=0, pady=3, sticky="e")

        self.user_entry = tk.Entry(login_frame, width=27, relief="groove", borderwidth=2)
        self.user_entry.grid(row=0, column=1, pady=3)

        # Campo de entrada da senha
        password_label = tk.Label(login_frame, text="Senha:")
        password_label.grid(row=1, column=0, pady=3, sticky="e")

        self.password_entry = tk.Entry(login_frame, show="*", width=27, relief="groove", borderwidth=2)
        self.password_entry.grid(row=1, column=1, pady=3)
        
        # Botão invisível
        botaologin = tk.Label(login_frame, text="")  
        botaologin.grid(row=2, column=1,padx=5, pady=7)

        # Botão Login
        self.btlogin = Image.open("Trabalho Final/Imagens/check.png")  #Não achei a imagem no drive
        self.btlogin = self.btlogin.resize((25,25))
        self.btlogin = ImageTk.PhotoImage(self.btlogin)
        botaologin = tk.Button(login_frame, text="  Login", relief=GROOVE, width=70, image=self.btlogin, compound="left", command=self.login)  
        botaologin.place(x=17, y=60)
        
        # Botão Cancelar
        self.app_lg = Image.open("Trabalho Final/Imagens/cancelar.png")
        self.app_lg = self.app_lg.resize((25,25))
        self.app_lg = ImageTk.PhotoImage(self.app_lg)
        app_logo = tk.Button(login_frame, image=self.app_lg, relief=GROOVE, text="  Cancelar", width=80, compound="left", command=self.encerrar_aplicacao)  
        app_logo.place(x=130, y=60)

# Classe para a janela principal
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Consultório de Psicologia")
        self.geometry("600x400")
        self.resizable(False, False)
        self.ficarbonitinho()

        self.create_menus()
        
    def ficarbonitinho(self):
        # Função para adicionar uma imagem de fundo personalizada
        self.foto = Image.open("Trabalho Final/Imagens/Consultório de Psicologia.png")
        self.foto = self.foto.resize((596,395))
        self.foto = ImageTk.PhotoImage(self.foto)
        img_label = tk.Label(self, image=self.foto)
        img_label.image = self.foto
        img_label.place(x=0, y=0)
    
    def create_menus(self):
        # Função para criar os menus da janela principal
        # Menu principal
        menu_bar = tk.Menu(self)

        # Menu Cadastros
        cadastros_menu = tk.Menu(menu_bar, tearoff=0)
        cadastros_menu.add_command(label="Pacientes", command=self.cadastrar_paciente)
        cadastros_menu.add_command(label="Anamnese", command=self.cadastrar_anamnese)
        cadastros_menu.add_command(label="Sessões", command=self.cadastrar_sessao)
        menu_bar.add_cascade(label="Cadastros", menu=cadastros_menu)

        # Menu Processos
        processos_menu = tk.Menu(menu_bar, tearoff=0)
        processos_menu.add_command(label="Agendamento", command=self.agendar_consulta)
        menu_bar.add_cascade(label="Processos", menu=processos_menu)

        # Menu Configurações
        configuracoes_menu = tk.Menu(menu_bar, tearoff=0)
        configuracoes_menu.add_command(label="Cadastrar Psicólogo", command=self.cadastrar_psicologo)
        menu_bar.add_cascade(label="Configurações", menu=configuracoes_menu)

        # Menu Relatórios
        relatorios_menu = tk.Menu(menu_bar, tearoff=0)
        relatorios_menu.add_command(label="Histórico Clínico", command=self.gerar_relatorio)
        menu_bar.add_cascade(label="Relatórios", menu=relatorios_menu)

        # Menu Ajuda
        ajuda_menu = tk.Menu(menu_bar, tearoff=0)
        ajuda_menu.add_command(label="Sobre", command=self.mostrar_sobre)
        menu_bar.add_cascade(label="Ajuda", menu=ajuda_menu)

        self.config(menu=menu_bar)

    def cadastrar_paciente(self):
        # Função para abrir ajanela de cadastro de pacientes
        paciente_window = PacienteWindow(self)

    def cadastrar_anamnese(self):
        # Função para abrir a janela de cadastro de anamneses
        anamnesse_window = AnamnesseWindow(self)

    def cadastrar_sessao(self):
        messagebox.showinfo("Cadastro de Sessão", "Funcionalidade em desenvolvimento.")

    def agendar_consulta(self):
        messagebox.showinfo("Agendamento", "Funcionalidade em desenvolvimento.")

    def cadastrar_psicologo(self):
         psicologo_window = PsicologoWindow(self)
         
    def gerar_relatorio(self):
        messagebox.showinfo("Histórico Clínico", "Funcionalidade em desenvolvimento.")

    def mostrar_sobre(self):
        about_window = AboutWindow()

# Classe para a janela de cadastro de pacientes
class PacienteWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Cadastro de Pacientes")
        self.geometry("600x400")
        self.resizable(False, False)

        self.create_widgets()
        
    def create_widgets(self):
        # Título
        title_label = tk.Label(self, text="Cadastro de Pacientes", font=("bold", 14))
        title_label.place(x=200, y=13)

        # LabelFrame Dados
        self.dados_frame = tk.LabelFrame(self, text="Dados", padx=10, pady=10)
        self.dados_frame.place(x=30, y=45)

        # Caixa de entrada Nome completo
        nome_label = tk.Label(self.dados_frame, text="Nome completo:")
        nome_label.grid(row=0, column=0, pady=2, sticky="e")
        
        self.nome_text= tk.Text(self.dados_frame, height=1, width=38, relief="groove", borderwidth=2)
        self.nome_text.grid(row=0, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada CPF
        cpf_label = tk.Label(self.dados_frame, text="CPF:")
        cpf_label.grid(row=1, column=0, pady=2, sticky="e")
        
        self.cpf_text = tk.Text(self.dados_frame,height=1, width=17, relief="groove", borderwidth=2)
        self.cpf_text.grid(row=1, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Data
        data_label = tk.Label(self.dados_frame, text="Data:")
        data_label.grid(row=2, column=0, pady=2, sticky="e")
        
        self.data_text = tk.Text(self.dados_frame, height=1, width=17, relief="groove", borderwidth=2)
        self.data_text.grid(row=2, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Radiobutton Sexo
        sexo_label = tk.Label(self.dados_frame, text="Sexo:")
        sexo_label.grid(row=3, column=0, pady=5, sticky="e")
        
        self.sexo_var = tk.StringVar()
        self.sexo_var.set("feminino")
        
        rb_masculino = tk.Radiobutton(self.dados_frame, text="Masculino", value="masculino", variable=self.sexo_var)
        rb_masculino.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        rb_feminino = tk.Radiobutton(self.dados_frame, text="Feminino", value="feminino", variable=self.sexo_var)
        rb_feminino.grid(row=3, column=1, padx=95, pady=5, sticky="w")
        
        # Caixa de entrada Endereço
        endereco_label = tk.Label(self.dados_frame, text="Endereço:")
        endereco_label.grid(row=4, column=0, pady=2, sticky="e")
        
        self.endereco_text = tk.Text(self.dados_frame, height=1, width=38, relief="groove", borderwidth=2)
        self.endereco_text.grid(row=4, column=1,padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Telefone
        telefone_label = tk.Label(self.dados_frame, text="Telefone:")
        telefone_label.grid(row=5, column=0, pady=2, sticky="e")
        
        self.telefone_text = tk.Text(self.dados_frame, height=1, width=17, relief="groove", borderwidth=2)
        self.telefone_text.grid(row=5, column=1,padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Combobox Plano de saúde
        plano_label = tk.Label(self.dados_frame, text="Plano de saúde:")
        plano_label.grid(row=6, column=0,  pady=2, sticky="e")
        
        self.plano_combobox = ttk.Combobox(self.dados_frame, values=["Amil", "Bradesco Saúde", "Porto Seguro", "Unimed", "SulAmérica"])
        self.plano_combobox.grid(row=6, column=1, padx=5,  pady=2, sticky="w")  # Adicionado sticky="w"

        # Caixa de entrada Observações
        obs_label = tk.Label(self.dados_frame, text="Observações:")
        obs_label.grid(row=7, column=0, pady=2, sticky="ne")
        
        self.obs_text = tk.Text(self.dados_frame, height=3, width=50,  relief="groove", borderwidth=2)
        self.obs_text.grid(row=7, column=1, padx=5, pady=4, sticky="w")
        
        # Botão de carregar imagem
        imagem_label = tk.Label(self.dados_frame, text="Fotografia")
        imagem_label.place(x=435, y=0)
        
        self.botaocarregar = Image.open("Trabalho Final/Imagens/Up_32.png")
        self.botaocarregar = self.botaocarregar.resize((22,22))
        self.botaocarregar = ImageTk.PhotoImage(self.botaocarregar)
        btcarregar = Button(self.dados_frame, text="  Upload", image=self.botaocarregar, width=80, relief="groove", borderwidth=2, compound="left", anchor=CENTER, command=self.escolher)
        btcarregar.place(x=420, y=145)
        
        # Botão - Novo
        self.botaonovo = Image.open("Trabalho Final/Imagens/new-32.png")
        self.botaonovo = self.botaonovo.resize((25,25))
        self.botaonovo = ImageTk.PhotoImage(self.botaonovo)
        btnovo = Button(self, text= "    Novo", image=self.botaonovo, width=80, relief="groove", borderwidth=2, compound="left", anchor=CENTER, command=self.limpar_formulario)
        btnovo.place(x=100, y=355)
        
        # Botão - Salvar
        self.botaosalvar = Image.open("Trabalho Final/Imagens/Save_32.png")
        self.botaosalvar = self.botaosalvar.resize((25,25))
        self.botaosalvar = ImageTk.PhotoImage(self.botaosalvar)
        btsalvar = Button(self, text="    Salvar", image=self.botaosalvar, width=80, relief="groove", borderwidth=2, compound="left", anchor=CENTER, command=self.salvar_paciente)
        btsalvar.place(x=260, y=355)
        
        # Botão - Sair
        self.botaosair = Image.open("Trabalho Final/Imagens/Cancel-32.png")
        self.botaosair = self.botaosair.resize((25,25))
        self.botaosair = ImageTk.PhotoImage(self.botaosair)
        btsair = Button(self, text="    Sair", image=self.botaosair, relief="groove", borderwidth=2, width=80, compound="left", anchor=CENTER, command=self.fechar_janela)
        btsair.place(x=420, y=355)
        
             
    def escolher(self):
        # Função para selecionar uma imagem
        filepath = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        
        # Verificando se um arquivo foi selecionado
        if filepath:
            imagem = Image.open(filepath)
            imagem = imagem.resize((81, 105))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = tk.Label(self.dados_frame, image=imagem,  relief="groove", borderwidth=2)
            l_imagem.image = imagem  # Mantém uma referência para a imagem para evitar que seja coletada pelo garbage collector
            l_imagem.place(x=420, y=20)
            

    def carregar_imagem(self):
        # Função para carregar uma imagem
        filepath = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        # Aqui você pode exibir a imagem carregada em um Label, se desejar
    
    def limpar_formulario(self):
        # Função para limpar todos os campos do formulário
        self.nome_text.delete("1.0", tk.END)
        self.cpf_text.delete("1.0", tk.END)
        self.data_text.delete("1.0", tk.END)
        self.sexo_var.set("feminino")
        self.endereco_text.delete("1.0", tk.END)
        self.telefone_text.delete("1.0", tk.END)
        self.plano_combobox.set("")
        self.obs_text.delete("1.0", tk.END)

    @staticmethod
    def validar_cpf(cpf):
        # Função para validar um CPF
        try:
            # Remove todos os caracteres que não são dígitos
            cpf = re.sub('[^0-9]', '', cpf)

            if len(cpf) != 11:
                raise ValueError("CPF inválido. O CPF deve conter 11 dígitos.")

            # Verifica se todos os dígitos são iguais
            if cpf == cpf[0] * 11:
                raise ValueError("CPF inválido. O CPF não pode ter todos os dígitos iguais.")

            # Calcula o primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            if int(cpf[9]) != dv1:
                raise ValueError("CPF inválido. O primeiro dígito verificador está incorreto.")

            # Calcula o segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto

            # Verifica o segundo dígito verificador
            if int(cpf[10]) != dv2:
                raise ValueError("CPF inválido. O segundo dígito verificador está incorreto.")

            # CPF válido
            return True

        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            return False

    def validar_data(self, data):
        # Função para validar uma data no formato dd/mm/yyyy
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            messagebox.showwarning("Aviso", "Data inválido.")
            return False
        
    @staticmethod
    def validar_telefone(telefone):
        # Função para validar um número de telefone com 11 dígitos
        telefone = re.sub('[^0-9]', '', telefone)

        if len(telefone) != 11:
            raise ValueError("Telefone inválido. Adicione seu DDD.")

        return True

    def salvar_paciente(self):
        # Função para salvar os dados do paciente
        nome = self.nome_text.get("1.0", "end-1c")     
        cpf = self.cpf_text.get("1.0", "end-1c")   
        data = self.data_text.get("1.0", "end-1c")
        sexo = self.sexo_var.get()
        endereco = self.endereco_text.get("1.0", "end-1c")
        telefone = self.telefone_text.get("1.0", "end-1c")
        plano = self.plano_combobox.get()
        observacoes = self.obs_text.get("1.0", "end-1c")
        
        if not self.validar_cpf (cpf):
            return 
        
        if not self.validar_data (data):
            return 
        
        try:
            if not self.validar_telefone(telefone):
                return
        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            return
        
        paciente = [(nome), (cpf) , (data) , (sexo) , (endereco) , (telefone), (plano), (observacoes)]
 
        if nome and cpf and data and sexo and endereco and telefone and plano and observacoes:
            with open('Trabalho Final/Texts/pacientes.txt', 'w', newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(paciente)

            messagebox.showinfo("Sucesso", "Paciente salvo com sucesso!")
            self.limpar_formulario()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
        
    
    def fechar_janela(self):
        # Função para fechar a janela
        self.destroy()

# Classe para a janela Cadastro de Psicologo
class PsicologoWindow (tk.Toplevel):
    def __init__(self, psico):
        super().__init__()
        self.psico = psico
        self.title("Cadastro de Psicologo")
        self.geometry("450x290")
        self.resizable(False, False)

        self.create_widgets()
        
    def create_widgets(self):
        # Título
        title_label = tk.Label(self, text="Cadastro de Psicólogo", font=("bold", 14))
        title_label.place(x=125, y=13)

        # LabelFrame Dados
        self.dados_frame_psico = tk.LabelFrame(self, text="Dados", padx=10, pady=10)
        self.dados_frame_psico.place(x=30, y=45)

        # Caixa de entrada Nome completo
        nomepsico_label = tk.Label(self.dados_frame_psico, text="Nome completo:")
        nomepsico_label.grid(row=0, column=0, pady=2, sticky="e")
        
        self.nomepsico_entry = tk.Entry(self.dados_frame_psico, width=43, relief="groove", borderwidth=2)
        self.nomepsico_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada CPF
        cpfpsico_label = tk.Label(self.dados_frame_psico, text="CPF:")
        cpfpsico_label.grid(row=1, column=0, pady=2, sticky="e")
        
        self.cpfpsico_entry = tk.Entry(self.dados_frame_psico, relief="groove", borderwidth=2)
        self.cpfpsico_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Data
        crppsico_label = tk.Label(self.dados_frame_psico, text="CRP:")
        crppsico_label.grid(row=2, column=0, pady=2, sticky="e")
        
        self.crppsico_entry = tk.Entry(self.dados_frame_psico, relief="groove", borderwidth=2)
        self.crppsico_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Telefone
        telefonepsico_label = tk.Label(self.dados_frame_psico, text="Telefone:")
        telefonepsico_label.grid(row=3, column=0, pady=2, sticky="e")
        
        self.telefonepsico_entry = tk.Entry(self.dados_frame_psico, relief="groove", borderwidth=2)
        self.telefonepsico_entry.grid(row=3, column=1,padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Login
        login_label = tk.Label(self.dados_frame_psico, text="Login:")
        login_label.grid(row=4, column=0, pady=2, sticky="e")
        
        self.login_entry = tk.Entry(self.dados_frame_psico, relief="groove", borderwidth=2)
        self.login_entry.grid(row=4, column=1,padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        # Caixa de entrada Senha 
        senha_label = tk.Label(self.dados_frame_psico, text="Senha:")
        senha_label.grid(row=5, column=0, pady=2, sticky="e")
        
        self.senha_entry = tk.Entry(self.dados_frame_psico, relief="groove", borderwidth=2)
        self.senha_entry.grid(row=5, column=1,padx=5, pady=2, sticky="w")  # Adicionado sticky="w"
        
        #Botão - Novo
        self.botaonovo2 = Image.open("Trabalho Final/Imagens/new-32.png")
        self.botaonovo2 = self.botaonovo2.resize((22,22))
        self.botaonovo2 = ImageTk.PhotoImage(self.botaonovo2)
        btnovo2 = Button(self, text="    Novo", image=self.botaonovo2, width=80, compound="left", anchor=CENTER, relief=GROOVE, command=self.limparpsico_formulario)
        btnovo2.place(x=60, y=245)
        
        #Botão - Salvar
        self.botaosalvar = Image.open("Trabalho Final/Imagens/Save_32.png")
        self.botaosalvar = self.botaosalvar.resize((22,22))
        self.botaosalvar = ImageTk.PhotoImage(self.botaosalvar)
        btsalvar = Button(self, text="    Salvar", image=self.botaosalvar, width=80, compound="left", anchor=CENTER, relief=GROOVE, command=self.salvar_psico)
        btsalvar.place(x=185, y=245)
        
        #Botão - Sair
        self.botaosair = Image.open("Trabalho Final/Imagens/Cancel-32.png")
        self.botaosair = self.botaosair.resize((22,22))
        self.botaosair = ImageTk.PhotoImage(self.botaosair)
        btsair = Button(self, text="    Sair", image=self.botaosair, width=80, compound="left", anchor=CENTER, relief=GROOVE, command=self.fechar_janelapsico)
        btsair.place(x=310, y=245)
         
        
    def limparpsico_formulario(self):
        # Função para limpar todos os campos do formulário do psicólogo
        self.nomepsico_entry.delete(0, tk.END)
        self.cpfpsico_entry.delete(0, tk.END)
        self.crppsico_entry.delete(0, tk.END)
        self.telefonepsico_entry.delete(0, tk.END)
        self.login_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)

    @staticmethod
    def validar_cpf(cpf):
        # Função para validar um CPF
        try:
            # Remove todos os caracteres que não são dígitos
            cpf = re.sub('[^0-9]', '', cpf)

            if len(cpf) != 11:
                raise ValueError("CPF inválido. O CPF deve conter 11 dígitos.")

            # Verifica se todos os dígitos são iguais
            if cpf == cpf[0] * 11:
                raise ValueError("CPF inválido. O CPF não pode ter todos os dígitos iguais.")

            # Calcula o primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            if int(cpf[9]) != dv1:
                raise ValueError("CPF inválido. O primeiro dígito verificador está incorreto.")

            # Calcula o segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto

            # Verifica o segundo dígito verificador
            if int(cpf[10]) != dv2:
                raise ValueError("CPF inválido. O segundo dígito verificador está incorreto.")

            # CPF válido
            return True

        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            return False
        
    @staticmethod
    def validar_telefone(telefonepsico):
         # Função para validar um número de telefone com 11 dígitos
        telefonepsico = re.sub('[^0-9]', '', telefonepsico)

        if len(telefonepsico) != 11:
            raise ValueError("Telefone inválido. Adicione seu DDD.")

        return True

    def salvar_psico(self):
         # Função para salvar os dados do psicólogo
        nomepsico = self.nomepsico_entry.get()
        cpf = self.cpfpsico_entry.get()
        crppsico = self.crppsico_entry.get()
        telefonepsico = self.telefonepsico_entry.get()
        login = self.login_entry.get()
        senha = self.senha_entry.get()
        
        try:
            if not self.validar_telefone(telefonepsico):
                return
        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            return
        
        if not self.validar_cpf (cpf):
            return 

        psicologo = [(nomepsico), (cpf) , (crppsico) , (telefonepsico) , (login) , (senha)]

        with open('Trabalho Final/Texts/psicólogos.txt', 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(psicologo)

        messagebox.showinfo("Sucesso", "Psicólogo registrado com sucesso!")

        self.nomepsico_entry.delete(0, tk.END)
        self.cpfpsico_entry.delete(0, tk.END)
        self.crppsico_entry.delete(0, tk.END)
        self.telefonepsico_entry.delete(0, tk.END)
        self.login_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
        
        
    def fechar_janelapsico(self):
        # Função para fechar a janela de cadastro de psicólogo
        self.destroy()

# Classe para cadastro de anamnese do paciente
class AnamnesseWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Cadastro de Anamnesse")
        self.geometry("635x455")
        self.resizable(False, False)

        self.create_widgets()
        
    def create_widgets(self):
        try:
            #frame de cima
            frame_logo = Frame(self, width=600, height=150)
            frame_logo.place(x=7,y=45)
            
            #frame de baixo
            frame_dados=Frame(self)
            frame_dados.place(x=0,y=96)
            
            # Título
            title_label = tk.Label(self, text="Cadastro de Anamnesse", font=("bold", 14))
            title_label.place(x=200, y=13)
            
            # Combobox Paciente
            paciente_label = tk.Label(frame_logo, text="Paciente: ")
            paciente_label.grid(row=0, column=0, pady=3, sticky="e")
            
            pacientes = self.load_pacientes()
            self.paciente_combobox = ttk.Combobox(frame_logo, values=pacientes)
            self.paciente_combobox.grid(row=0, column=1, padx=5,  pady=3, sticky="w")  # Adicionado sticky="w"
            
            # Combobox Psicologo
            psicologo_label = tk.Label(frame_logo, text="Psicologo: ")
            psicologo_label.grid(row=1, column=0, pady=3, sticky="e")

            psicologos = self.load_psicologos()
            self.psicologo_combobox = ttk.Combobox(frame_logo, values=psicologos)
            self.psicologo_combobox.grid(row=1, column=1, padx=5, pady=3, sticky="w")
            
            # Notebook (Abas)
            notebook = ttk.Notebook(frame_dados)
            notebook.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Primeira aba
            page1 = tk.Frame(notebook)
            notebook.add(page1, text="Antecedentes")
            
            # Segunda aba
            page21 = tk.Frame(notebook)
            notebook.add(page21, text="Rotina")
            
            # Terceira aba
            page31 = tk.Frame(notebook)
            notebook.add(page31, text="Comportamento")
            
             # Quarta aba
            page41 = tk.Frame(notebook)
            notebook.add(page41, text="Outros")
            
            # Página 1
            self.page1_frame = tk.LabelFrame(page1, text="Dados", padx=10, pady=10)
            self.page1_frame.pack(padx=5, pady=3)
            
            # Widgets na página 1
            #queixas
            queixas_label = tk.Label(self.page1_frame, text="Queixas: ")
            queixas_label.grid(row=0, column=0, pady=0, sticky="ne")
            
            self.queixas_entry = tk.Text(self.page1_frame, width=57, height=2,  relief="groove", borderwidth=2)
            self.queixas_entry.grid(row=0, column=1, padx=0, pady=0, sticky="ne")  
           
            #sintomas
            sintomas_label = tk.Label(self.page1_frame, text="Sintomas: ")
            sintomas_label.grid(row=1, column=0, pady=7, sticky="ne")
            
            self.sintomas_entry = tk.Text(self.page1_frame, width=57, height=2,  relief="groove", borderwidth=2)
            self.sintomas_entry.grid(row=1, column=1,  pady=7, sticky="ne")
            
            #tratamentos
            Tratamentos_label = tk.Label(self.page1_frame, text="Tratamentos\n   Anteriores: ")
            Tratamentos_label.grid(row=2, column=0, pady=0, sticky="ne")
            
            self.tratamentos_entry = tk.Text(self.page1_frame, width=57, height=2,  relief="groove", borderwidth=2)
            self.tratamentos_entry.grid(row=2, column=1, padx=0, pady=0, sticky="w")
            
            #medicamentos
            medicamentos_label = tk.Label(self.page1_frame, text="Medicamentos ")
            medicamentos_label.grid(row=3, column=0, pady=7, sticky="ne")
            
            self.medicamentos_entry = tk.Text(self.page1_frame, width=57, height=2,  relief="groove", borderwidth=2)
            self.medicamentos_entry.grid(row=3, column=1, padx=0, pady=7, sticky="w")
            
            #infancia
            infancia_label = tk.Label(self.page1_frame, text="Infância: ")
            infancia_label.grid(row=4, column=0, pady=0, sticky="ne")
            
            self.infancia_entry = tk.Text(self.page1_frame, width=57, height=2,  relief="groove", borderwidth=2)
            self.infancia_entry.grid(row=4, column=1, padx=0, pady=0, sticky="w")

            #Widgets na página 2
        
            page2=Frame(page21)
            page2.place(x=15,y=22)
            
            #rotina        
            rotina_label = tk.Label(page2, text="Rotina: ")
            rotina_label.grid(row=0, column=0, pady=0, sticky=NE)
        
            self.rotina_entry = tk.Text(page2, width=60, height=2,  relief="groove", borderwidth=2)
            self.rotina_entry.grid(row=0, column=1, padx=0, pady=0, sticky=NE)  # Adicionado sticky="w"

            #vicios
            vicios_label = tk.Label(page2, text="Vicios: ")
            vicios_label.grid(row=1, column=0, pady=8, sticky=NE)
        
            self.vicios_entry = tk.Text(page2, width=60, height=2,  relief="groove", borderwidth=2)
            self.vicios_entry.grid(row=1, column=1, padx=0, pady=8, sticky=NE)  # Adicionado sticky="w"
        
            #hobbies
            Hobbies_label = tk.Label(page2, text="Hobbies: ")
            Hobbies_label.grid(row=2, column=0, pady=0, sticky=NE)
        
            self.Hobbies_entry = tk.Text(page2, width=60, height=2,  relief="groove", borderwidth=2)
            self.Hobbies_entry.grid(row=2, column=1, padx=0, pady=0, sticky="w")  # Adicionado sticky="w"
        
            #trabalho
            trabalho_label = tk.Label(page2, text="Trabalho: ")
            trabalho_label.grid(row=3, column=0, pady=8, sticky=NE)
        
            self.trabalho_entry = tk.Text(page2, width=60, height=2,  relief="groove", borderwidth=2)
            self.trabalho_entry.grid(row=3, column=1, padx=0, pady=8, sticky="w")  # Adicionado sticky="w"
        
            #historico
            historico_label = tk.Label(page2, text="Histórioco\n    Familiar: ")
            historico_label.grid(row=4, column=0, pady=0, sticky=NE)
        
            self.historico_entry = tk.Text(page2, width=60, height=2,  relief="groove", borderwidth=2)
            self.historico_entry.grid(row=4, column=1, padx=0, pady=0, sticky="w")
        
            # Widgets na página 3
        
            page3=Frame(page31)
            page3.place(x=15,y=22)
        
            #comportamento
            comportamento_label = tk.Label(page3, text="Comportamento: ")
            comportamento_label.grid(row=0, column=0, pady=0, sticky=NE)
        
            self.comportamento_entry = tk.Text(page3, width=53, height=2,  relief="groove", borderwidth=2)
            self.comportamento_entry.grid(row=0, column=1, padx=0, pady=0, sticky=NE)  # Adicionado sticky="w"

            #linguagem
            linguagem_label = tk.Label(page3, text="Linguagem: ")
            linguagem_label.grid(row=1, column=0, pady=8, sticky=NE)
        
            self.linguagem_entry = tk.Text(page3, width=53, height=2,  relief="groove", borderwidth=2)
            self.linguagem_entry.grid(row=1, column=1, padx=0, pady=8, sticky=NE)  # Adicionado sticky="w"
        
            #humor
            humor_label = tk.Label(page3, text="Humor: ")
            humor_label.grid(row=2, column=0, pady=0, sticky=NE)
        
            self.humor_entry = tk.Text(page3, width=53, height=2,  relief="groove", borderwidth=2)
            self.humor_entry.grid(row=2, column=1, padx=0, pady=0, sticky="w")  # Adicionado sticky="w"
        
            #hipotese
            hipotese_label = tk.Label(page3, text="Hipotese diágnostica: ")
            hipotese_label.grid(row=3, column=0, pady=8, sticky=NE)
        
            self.hipotese_entry = tk.Text(page3, width=53, height=2, relief="groove", borderwidth=2)
            self.hipotese_entry.grid(row=3, column=1, padx=0, pady=8, sticky="w")  # Adicionado sticky="w"
        

            # Exemplo de widgets na página 4
        
            page4=Frame(page41)
            page4.place(x=15,y=22)
        
            # Spinbox Número de sessões
            sessoes_label = tk.Label(page4, borderwidth=3, text="Numero de Sessões: ")
            sessoes_label.grid(row=0, column=0,  pady=0, sticky="e")
        
            valores =[str(i) for i in range(0, 501)]

            self.sessoes = tk.Spinbox(page4, width=19, values=valores, relief="groove", borderwidth=2)
            self.sessoes.grid(row=0, column=1, padx=0,  pady=0, sticky="w") 
        
            #Valor
            valor_label =tk.Label(page4, text="Valor sessão: ")
            valor_label.grid(row=1, column=0, pady=8, sticky="e")
        
            self.valor_entry = tk.Entry(page4, width=21, relief="groove", borderwidth=2)
            self.valor_entry.grid(row=1, column=1, padx=0, pady=8, sticky="w")
        
            # Combobox Psicologo
            periodicidade_label = tk.Label(page4, text="Periodicidade: ")
            periodicidade_label.grid(row=2, column=0,  pady=0, sticky="e")
        
            self.periodicidade_combobox = ttk.Combobox(page4, values=["Diário", "Semanal", "Quinzenal", "Mensal", "Anual"])
            self.periodicidade_combobox.grid(row=2, column=1, padx=0,  pady=0, sticky="w")  # Adicionado sticky="w"

            #obs
            observaçoes_label = tk.Label(page4, text="Observações: ")
            observaçoes_label.grid(row=3, column=0, pady=8, sticky=NE)
        
            self.observacao_entry = tk.Text (page4, relief="groove", borderwidth=2, width=50, height=3)
            self.observacao_entry.grid(row=3, column=1, padx=0, pady=8)

            #Botão - Novo
            self.botaonovo = Image.open("Trabalho Final/Imagens/new-32.png")
            self.botaonovo = self.botaonovo.resize((28,28))
            self.botaonovo = ImageTk.PhotoImage(self.botaonovo)
            btnovo = tk.Button(self, text="    Novo", image=self.botaonovo,  relief=GROOVE, compound="left", width=90, command=self.limpar_formulario)
            btnovo.place(x=100, y=405)
        
            #Botão - Salvar
            self.botaosalvar = Image.open("Trabalho Final/Imagens/Save_32.png")
            self.botaosalvar = self.botaosalvar.resize((28,28))
            self.botaosalvar = ImageTk.PhotoImage(self.botaosalvar)
            btsalvar = tk.Button(self, text="    Salvar", image=self.botaosalvar,  relief=GROOVE, width=90,  compound="left", command=self.salvar_antecedentes)
            btsalvar.place(x=260, y=405)
        
            #Botão - Sair
            self.botaosair = Image.open("Trabalho Final/Imagens/Cancel-32.png")
            self.botaosair = self.botaosair.resize((28,28))
            self.botaosair = ImageTk.PhotoImage(self.botaosair)
            btsair = tk.Button(self, text="    Sair", image=self.botaosair,  relief=GROOVE, width=90, compound="left", command=self.fechar_janela)
            btsair.place(x=420, y=405)
        
        #tratamento de exceção
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def load_pacientes(self):
        #Lê um arquivo chamado "pacientes.txt" e retorna uma lista com os nomes dos pacientes
        try:
            with open("Trabalho Final/Texts/pacientes.txt", "r") as file:
                pacientes = [line.strip().split()[0] for line in file]
            if not pacientes:
                raise IndexError("Lista de pacientes vazia.")
            return pacientes
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception("Erro ao carregar pacientes: " + str(e))
    
    def load_psicologos(self):
        #Lê um arquivo chamado "psicólogos.txt" e retorna uma lista com os nomes dos psicólogos.
        try:
            with open("Trabalho Final/Texts/psicólogos.txt", "r") as file:
                psicologos = [line.strip().split()[0] for line in file]
            if not psicologos:
                raise IndexError("Lista de psicólogos vazia.")
            return psicologos
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception("Erro ao carregar psicólogos: " + str(e))    
        
    def limpar_formulario(self):
        #Limpa todos os campos de entrada de texto da janela
        self.paciente_combobox.set("")
        self.psicologo_combobox.set("")
        self.queixas_entry.delete("1.0", "end")
        self.sintomas_entry.delete("1.0", "end")
        self.tratamentos_entry.delete("1.0", "end")
        self.medicamentos_entry.delete("1.0", "end")
        self.infancia_entry.delete("1.0", "end")
        self.rotina_entry.delete("1.0", "end")
        self.vicios_entry.delete("1.0", "end")
        self.Hobbies_entry.delete("1.0", "end")
        self.trabalho_entry.delete("1.0", "end")
        self.historico_entry.delete("1.0", "end")
        self.comportamento_entry.delete("1.0", "end")
        self.linguagem_entry.delete("1.0", "end")
        self.humor_entry.delete("1.0", "end")
        self.hipotese_entry.delete("1.0", "end")
        self.valor_entry.delete(0, "end")
        self.observacao_entry.delete("1.0", "end")
        self.periodicidade_combobox.set("")
        self.sessoes.delete(0, tk.END)

    def salvar_antecedentes(self):
        #Salva todos os campos de entrada de texto
        paciente = self.paciente_combobox.get()
        psicologo = self.psicologo_combobox.get()
        queixas = self.queixas_entry.get("1.0", "end-1c")
        sintomas = self.sintomas_entry.get("1.0", "end-1c")
        tratamentos = self.tratamentos_entry.get("1.0", "end-1c")
        medicamentos = self.medicamentos_entry.get("1.0", "end-1c")
        infancia = self.infancia_entry.get("1.0", "end-1c")
        rotina = self.rotina_entry.get("1.0", "end-1c")
        vicio = self.rotina_entry.get("1.0", "end-1c")
        hobbies = self.Hobbies_entry.get("1.0", "end-1c")
        trabalho = self.trabalho_entry.get("1.0", "end-1c")
        historico = self.historico_entry.get("1.0", "end-1c")
        comportamento = self.comportamento_entry.get("1.0", "end-1c")
        linguagem = self.linguagem_entry.get("1.0", "end-1c")
        humor = self.humor_entry.get("1.0", "end-1c")
        hipotese = self.hipotese_entry.get("1.0", "end-1c")
        sessoes = self.sessoes.get()
        valor = self.valor_entry.get()
        periodicidade = self.periodicidade_combobox.get()
        observação = self.observacao_entry.get("1.0", "end-1c")
        
        if paciente and psicologo:
            with open("Trabalho Final/Texts/antecedentes.txt", "a") as file:
            # Escreva os antecedentes no arquivo
                file.write(f"Paciente: {paciente}\n")
                file.write(f"Psicologo: {psicologo}\n")
                file.write(f"Queixas: {queixas}\n")
                file.write(f"Sintomas: {sintomas}\n")
                file.write(f"Tratamentos anteriores: {tratamentos}\n")
                file.write(f"Medicamentos: {medicamentos}\n")
                file.write(f"Infancia: {infancia}\n")
                file.write(f"Rotina: {rotina}\n")
                file.write(f"Vicio: {vicio}\n")
                file.write(f"Hobbies: {hobbies}\n")
                file.write(f"Trabalho: {trabalho}\n")
                file.write(f"Historico Familiar: {historico}\n")
                file.write(f"Comportamento: {comportamento}\n")
                file.write(f"Linguagem: {linguagem}\n")
                file.write(f"Humor: {humor}\n")
                file.write(f"Hipotese diágnostica: {hipotese}\n")
                file.write(f"Numero de sessoes: {sessoes}\n")
                file.write(f"Valor sessao: {valor}\n")
                file.write(f"Periodicidade: {periodicidade}\n")
                file.write(f"Observacoes: {observação}\n")
                file.write("-" * 30 + "\n")
            
            messagebox.showinfo("Sucesso", "Antecedentes salvos!")
            self.limpar_formulario()
            
        else:
            messagebox.showwarning("Aviso", "Preencha os campos Paciente e Psicólogo.")


    def fechar_janela(self):
        #Fecha a janela atual
        self.destroy()


# Classe para a janela de informações do projeto
class AboutWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Sobre")
        self.geometry("300x129")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Rótulos com as informações
        
        tk.Label(self, text="Disciplina: Computação 2").pack()
        tk.Label(self, text="Semestre: Segundo Semestre ").pack()
        tk.Label(self, text="Aluno: Maria Luiza Sousa Martins Americo").pack()
        tk.Label(self, text="Matricula: 122168778").pack() 

        # Botão Fechar
        close_button = tk.Button(self, text="Fechar", command=self.destroy)
        close_button.pack(pady=5)

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
