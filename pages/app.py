import customtkinter
from PIL import Image, ImageTk


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Estoque")
        self.geometry("1024x600")
        customtkinter.set_appearance_mode("dark")

        #Imagens/Fonts
        self.image_logo = customtkinter.CTkImage(dark_image=Image.open("./images/michelly.png"),
                                                 size=(140, 140))
        self.image_estoque = customtkinter.CTkImage(dark_image=Image.open("./images/estoque.png"),
                                                    size=(16, 16))
        self.image_historico = customtkinter.CTkImage(dark_image=Image.open("./images/historico.png"),
                                                    size=(16, 16))
        self.image_add_pedido = customtkinter.CTkImage(dark_image=Image.open("./images/add_pedido.png"),
                                                    size=(16, 16))
        self.image_config = customtkinter.CTkImage(dark_image=Image.open("./images/config.png"),
                                                    size=(16, 16))
        self.font_buttons = customtkinter.CTkFont(size=13, weight="bold")

        #Frames
        self.buttons_frame = customtkinter.CTkFrame(self)

        #Botões
        self.button_icone = customtkinter.CTkButton(self,
                                                    command=self.button_callback,
                                                    height=100,
                                                    width=100,
                                                    image=self.image_logo,
                                                    text='',
                                                    fg_color="#2b2b2b",
                                                    hover=False)
        self.button_estoque = customtkinter.CTkButton(self,
                                                      text="ESTOQUE",
                                                      command=self.button_callback,
                                                      height=35,
                                                      text_color="light gray",
                                                      font=self.font_buttons,
                                                      image=self.image_estoque)
        self.button_historico = customtkinter.CTkButton(self,
                                                        text="HISTORICO",
                                                        command=self.button_callback,
                                                        height=35,
                                                        text_color="light gray",
                                                        font=self.font_buttons,
                                                        image=self.image_historico)
        self.button_add_pedido = customtkinter.CTkButton(self,
                                                         text="NOVO PEDIDO",
                                                         command=self.button_callback,
                                                         height=35,
                                                         text_color="light gray",
                                                         font=self.font_buttons,
                                                         image=self.image_add_pedido)
        self.button_config = customtkinter.CTkButton(self,
                                                         text="CONFIGURAÇÃO",
                                                         command=self.button_callback,
                                                         height=35,
                                                         text_color="light gray",
                                                         font=customtkinter.CTkFont(size=11, weight="bold"),
                                                         image=self.image_config)

        #Posições
        self.buttons_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsw")
        self.button_icone.grid(row=0, column=0, padx=10, pady=25, sticky='n')
        self.button_estoque.grid(row=0, column=0, padx=10, pady=(190, 25), sticky='n')
        self.button_historico.grid(row=0, column=0, padx=10, pady=(230, 25), sticky='n')
        self.button_add_pedido.grid(row=0, column=0, padx=10, pady=(270, 25), sticky='n')
        self.button_config.grid(row=0, column=0, padx=10, pady=(310, 25), sticky='n')

    def button_callback(self):
        print("button pressed")
